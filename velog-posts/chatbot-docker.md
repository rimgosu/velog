<h1 id="chatbot-docker">chatbot-docker</h1>
<ul>
<li><p>results
<img alt="" src="https://velog.velcdn.com/images/rimgosu/post/b994ca37-2fc3-418d-a515-357effa4289b/image.png" />
<img alt="" src="https://velog.velcdn.com/images/rimgosu/post/5b5474a2-f5b7-43c9-a7b4-c626106c12ee/image.png" /></p>
</li>
<li><p>github: <a href="https://github.com/rimgosu/PythonScienceStudy/tree/master/chatbot">https://github.com/rimgosu/PythonScienceStudy/tree/master/chatbot</a></p>
</li>
</ul>
<h2 id="1-도커-챗봇-설정">1. 도커-챗봇 설정</h2>
<ul>
<li><a href="https://cafe.naver.com/aiclubcafe/647">https://cafe.naver.com/aiclubcafe/647</a><pre><code>docker pull apptools/chatbot-db:1.0
docker run --privileged -d -p 3306:3306 --name chatbot-db apptools/chatbot-db:1.0
docker exec -e LC_ALL=C.UTF-8 -it chatbot-db /bin/bash</code></pre></li>
</ul>
<h2 id="2-mysql">2. mysql</h2>
<h3 id="1-mysql-접속">1) mysql 접속</h3>
<pre><code>mysql -u root -p</code></pre><ul>
<li>password : apptools</li>
</ul>
<h3 id="2-db-생성">2) db 생성</h3>
<pre><code>create database flyai;
use flyai;</code></pre><pre><code>mysql&gt; show databases;
+--------------------+
| Database           |
+--------------------+
| flyai              |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)</code></pre><h3 id="3-테이블-추가">3) 테이블 추가</h3>
<pre><code>create table chatbot(
  num int not null auto_increment,
  type varchar(4),
  msg varchar(200),
  indate varchar(50),
  primary key(num)
);</code></pre><pre><code>mysql&gt; desc chatbot;
+--------+--------------+------+-----+---------+----------------+
| Field  | Type         | Null | Key | Default | Extra          |
+--------+--------------+------+-----+---------+----------------+
| num    | int          | NO   | PRI | NULL    | auto_increment |
| type   | varchar(4)   | YES  |     | NULL    |                |
| msg    | varchar(200) | YES  |     | NULL    |                |
| indate | varchar(50)  | YES  |     | NULL    |                |
+--------+--------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)</code></pre><h2 id="3-챗봇-학습-툴-만들기">3. 챗봇 학습 툴 만들기</h2>
<ul>
<li><a href="https://cafe.naver.com/aiclubcafe/708">https://cafe.naver.com/aiclubcafe/708</a></li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/5f180fda-2edc-41f3-90be-1398c8811542/image.png" /></p>
<h3 id="1-프로젝트-구조">1) 프로젝트 구조</h3>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/86d8c984-a45d-411c-8ab4-e1490c012ca7/image.png" /></p>
<h3 id="2-configdatabaseconfigpy">2) config/DatabaseConfig.py</h3>
<ul>
<li>DB_HOST : 명령 프롬프트에서 ipconfig 실행 후 무선 LAN IP 확인<pre><code>DB_HOST = &quot;172.23.254.237&quot;
DB_USER = &quot;root&quot;
DB_PASSWORD = &quot;apptools&quot;
DB_NAME = &quot;flyai&quot;
</code></pre></li>
</ul>
<p>def DatabaseConfig():
    global DB_HOST, DB_USER, DB_PASSWORD, DB_NAME</p>
<pre><code>
### 3) train_tools/qna/create_train_data_table.py</code></pre><p>import pymysql
import sys
sys.path.append('c:/flyai/chatbot')
from config.DatabaseConfig import * # DB 접속 정보 불러오기</p>
<p>db = None
try:
        db = pymysql.connect(
                    host=DB_HOST,
                    user=DB_USER,
                    passwd=DB_PASSWORD,
                    db=DB_NAME,
                    charset='utf8'
        )</p>
<pre><code>    # 테이블 생성 sql 정의
    sql = '''
        CREATE TABLE IF NOT EXISTS chatbot_train_data (
            id INT UNSIGNED NOT NULL AUTO_INCREMENT,
            intent VARCHAR(45) NULL,
            ner VARCHAR(1024) NULL,
            query TEXT NULL,
            answer TEXT NOT NULL,
            answer_image VARCHAR(2048) NULL,
            PRIMARY KEY (id)
        );
    '''

    # 테이블 생성
    with db.cursor() as cursor:
            cursor.execute(sql)</code></pre><p>except Exception as e:
        print(e)</p>
<p>finally:
        if db is not None:
                db.close()</p>
<pre><code>
- 실행 방법</code></pre><p>cd c:/flyai/chatbot/train_tools/qna
python ./create_train_data_table.py</p>
<pre><code>
### 4) train_tools/qna/train_data.xlsx
- 위 카페에서 다운로드 받아 경로에 넣자.

### 5) train_tools/qna/load_train_data.py
- xls =&gt; db
</code></pre><p>import pymysql
import openpyxl
import sys
sys.path.append('c:/flyai/chatbot')
from config.DatabaseConfig import * # DB 접속 정보 불러오기</p>
<h1 id="학습-데이터-초기화">학습 데이터 초기화</h1>
<p>def all_clear_train_data(db):
    # 기존 학습 데이터 삭제
    sql = '''
            delete from chatbot_train_data
        '''
    with db.cursor() as cursor:
        cursor.execute(sql)</p>
<pre><code># auto increment 초기화
sql = '''
ALTER TABLE chatbot_train_data AUTO_INCREMENT=1
'''
with db.cursor() as cursor:
    cursor.execute(sql)</code></pre><h1 id="db에-데이터-저장">db에 데이터 저장</h1>
<p>def insert_data(db, xls_row):
    intent, ner, query, answer, answer_img_url = xls_row</p>
<pre><code>sql = '''
    INSERT chatbot_train_data(intent, ner, query, answer, answer_image) 
    values(
     '%s', '%s', '%s', '%s', '%s'
    )
''' % (intent.value, ner.value, query.value, answer.value, answer_img_url.value)

# 엑셀에서 불러온 cell에 데이터가 없는 경우, null 로 치환
sql = sql.replace(&quot;'None'&quot;, &quot;null&quot;)

with db.cursor() as cursor:
    cursor.execute(sql)
    print('{} 저장'.format(query.value))
    db.commit()</code></pre><p>train_file = './train_data.xlsx'
db = None
try:
    db = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWORD,
        db=DB_NAME,
        charset='utf8'
    )</p>
<pre><code># 기존 학습 데이터 초기화
all_clear_train_data(db)

# 학습 엑셀 파일 불러오기
wb = openpyxl.load_workbook(train_file)
sheet = wb['Sheet1']
for row in sheet.iter_rows(min_row=2): # 해더는 불러오지 않음
    # 데이터 저장
    insert_data(db, row)

wb.close()</code></pre><p>except Exception as e:
    print(e)</p>
<p>finally:
    if db is not None:
        db.close()</p>
<pre><code>
- 실행 방법</code></pre><p>cd c:/flyai/chatbot/train_tools/qna
python ./load_train_data.py</p>
<pre><code></code></pre><p>mysql&gt; select id,intent, ner, query from chatbot_train_data;
+----+--------+-----------+--------------------------+
| id | intent | ner       | query                    |
+----+--------+-----------+--------------------------+
|  1 | 인사   | NULL      | 안녕하세요               |
|  2 | 인사   | NULL      | 반가워요                 |
|  3 | 주문   | B_FOOD    | {B_FOOD} 주문할게요      |
|  4 | 주문   | B_FOOD    | {B_FOOD} 주문할게요      |
|  5 | 예약   | B_DT,B_TI | {B_DT} 예약              |
|  6 | 욕설   | NULL      | NULL                     |
+----+--------+-----------+--------------------------+</p>
<pre><code>

## 4. 챗봇 엔진 만들기
- &lt;https://cafe.naver.com/aiclubcafe/709&gt;

### 1) 라이브러리 설치</code></pre><p>pip install konlpy
pip install seqeval
pip install tensorflow</p>
<pre><code>
### 2) utils/Preprocess.py</code></pre><p>from konlpy.tag import Komoran
import pickle</p>
<p>class Preprocess:
    # 생성자
    def <strong>init</strong>(self, word2index_dic=&quot;&quot;, userdic=None):
        # 단어 인덱스 사전 불러오기
        if word2index_dic != &quot;&quot;:
            f = open(word2index_dic, &quot;rb&quot;)
            self.word_index = pickle.load(f)
            f.close()
        else:
            self.word_index = None</p>
<pre><code>    # 형태소 분석기 초기화
    self.komoran = Komoran(userdic=userdic)

    # 제외할 품사
    # 참조: https://docs.komoran.kr/firststep/postypes.html
    self.exclusion_tags = [
        &quot;JKS&quot;, &quot;JKC&quot;, &quot;JKG&quot;, &quot;JKO&quot;, &quot;JKB&quot;, &quot;JKV&quot;, &quot;JKQ&quot;, &quot;JX&quot;, &quot;JC&quot;, # 관계언 제거
        &quot;SF&quot;, &quot;SP&quot;, &quot;SS&quot;, &quot;SE&quot;, &quot;SO&quot;, # 기호 제거
        &quot;EP&quot;, &quot;EF&quot;, &quot;EC&quot;, &quot;ETN&quot;, &quot;ETM&quot;, # 어미 제거
        &quot;XSN&quot;, &quot;XSV&quot;, &quot;XSA&quot;, # 접미사 제거
    ]

# 형태소 분석기 POS tagger (래퍼 함수)
def pos(self, sentence):
    return self.komoran.pos(sentence)

# 불용어 제거 후 필요한 품사 정보만 가져오기
def get_keywords(self, pos, without_tag=False):
    f = lambda x: x in self.exclusion_tags
    word_list = []
    for p in pos:
        if f(p[1]) is False: # 불용어 리스트에 없는 경우에만 저장
            word_list.append(p if without_tag is False else p[0])
    return word_list

# 키워드를 단어 인덱스 시퀀스로 변환
def get_wordidx_sequence(self, keywords):
    if self.word_index is None:
        return []
    w2i = []
    for word in keywords:
        try:
            w2i.append(self.word_index[word])
        except KeyError:
            # 해당 단어가 사전에 없는 경우 OOV 처리
            w2i.append(self.word_index[&quot;OOV&quot;])
    return w2i</code></pre><pre><code>
### 3) train_tools/dict/corpus.txt
- 위 사이트에서 corpus.txt 다운로드 후 붙여넣자.

### 4) train_tools/dict/create_dict.py</code></pre><p>import sys
sys.path.append('c:/flyai/chatbot')
from utils.Preprocess import Preprocess
from tensorflow.keras import preprocessing
import pickle</p>
<h1 id="말뭉치-데이터-읽어오기">말뭉치 데이터 읽어오기</h1>
<p>def read_corpus_data(filename):
    with open(filename, &quot;r&quot;, encoding='utf8') as f:
        data = [line.split(&quot;\t&quot;) for line in f.read().splitlines()]
        data = data[1:] # 헤더 제거
    return data</p>
<h1 id="말뭉치-데이터-가져오기">말뭉치 데이터 가져오기</h1>
<p>corpus_data = read_corpus_data(&quot;./corpus.txt&quot;)</p>
<h1 id="말뭉치-데이터에서-키워드만-추출해서-사전-리스트-생성">말뭉치 데이터에서 키워드만 추출해서 사전 리스트 생성</h1>
<p>p = Preprocess()
dict = []
for c in corpus_data:
    pos = p.pos(c[1])
    for k in pos:
        dict.append(k[0])</p>
<h1 id="사전에-사용될-단어-인덱스-딕셔너리word_index-생성">사전에 사용될 단어 인덱스 딕셔너리(word_index) 생성</h1>
<p>tokenizer = preprocessing.text.Tokenizer(oov_token=&quot;OOV&quot;)
tokenizer.fit_on_texts(dict)
word_index = tokenizer.word_index</p>
<h1 id="사전-파일-생성">사전 파일 생성</h1>
<p>f = open(&quot;chatbot_dict.bin&quot;, &quot;wb&quot;)
try:
    pickle.dump(word_index, f)
except Exception as e:
    print(e)
finally:
    f.close()</p>
<pre><code>

### 5) config/globalparams.py </code></pre><h1 id="단어-시퀀스-벡터-크기">단어 시퀀스 벡터 크기</h1>
<p>MAX_SEQ_LEN =15</p>
<p>def GlobalParams():
    global MAX_SEQ_LEN</p>
<pre><code>

### 6) model/intent/total_train_data.csv
- 위 사이트에서 다운로드 후 붙여넣자

### 7) utils/user_dic.tsv
- 그냥 생성하자.

### 8) model/intent/train_model.py
- 의도 분류 모델 학습</code></pre><h1 id="필요한-모듈-임포트">필요한 모듈 임포트</h1>
<p>import pandas as pd
import tensorflow as tf
from tensorflow.keras import preprocessing
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Dense, Dropout, Conv1D, GlobalMaxPool1D, concatenate</p>
<h1 id="데이터-읽어오기">데이터 읽어오기</h1>
<p>train_file = &quot;total_train_data.csv&quot;
data = pd.read_csv(train_file, delimiter=',')
queries = data['query'].tolist()
intents = data['intent'].tolist()</p>
<p>import sys
sys.path.append('c:/flyai/chatbot')
from utils.Preprocess import Preprocess
p = Preprocess(word2index_dic='../../train_tools/dict/chatbot_dict.bin',
               userdic='../../utils/user_dic.tsv')</p>
<h1 id="단어-시퀀스-생성">단어 시퀀스 생성</h1>
<p>sequences = []
for sentence in queries:
    pos = p.pos(sentence)
    keywords = p.get_keywords(pos, without_tag=True)
    seq = p.get_wordidx_sequence(keywords)
    sequences.append(seq)</p>
<h1 id="단어-인덱스-시퀀스-벡터">단어 인덱스 시퀀스 벡터</h1>
<h1 id="단어-시퀀스-벡터-크기-1">단어 시퀀스 벡터 크기</h1>
<p>from config.GlobalParams import MAX_SEQ_LEN
padded_seqs = preprocessing.sequence.pad_sequences(sequences, maxlen=MAX_SEQ_LEN, padding='post')</p>
<h1 id="105658-15">(105658, 15)</h1>
<p>print(padded_seqs.shape)
print(len(intents)) #105658</p>
<h1 id="학습용-검증용-테스트용-데이터셋-생성">학습용, 검증용, 테스트용 데이터셋 생성</h1>
<h1 id="학습셋검증셋테스트셋--721">학습셋:검증셋:테스트셋 = 7:2:1</h1>
<p>ds = tf.data.Dataset.from_tensor_slices((padded_seqs, intents))
ds = ds.shuffle(len(queries))</p>
<p>train_size = int(len(padded_seqs) * 0.7)
val_size = int(len(padded_seqs) * 0.2)
test_size = int(len(padded_seqs) * 0.1)</p>
<p>train_ds = ds.take(train_size).batch(20)
val_ds = ds.skip(train_size).take(val_size).batch(20)
test_ds = ds.skip(train_size + val_size).take(test_size).batch(20)</p>
<h1 id="하이퍼-파라미터-설정">하이퍼 파라미터 설정</h1>
<p>dropout_prob = 0.5
EMB_SIZE = 128
EPOCH = 5
VOCAB_SIZE = len(p.word_index) + 1 #전체 단어 개수</p>
<h1 id="cnn-모델-정의">CNN 모델 정의</h1>
<p>input_layer = Input(shape=(MAX_SEQ_LEN,))
embedding_layer = Embedding(VOCAB_SIZE, EMB_SIZE, input_length=MAX_SEQ_LEN)(input_layer)
dropout_emb = Dropout(rate=dropout_prob)(embedding_layer)</p>
<p>conv1 = Conv1D(
    filters=128,
    kernel_size=3,
    padding='valid',
    activation=tf.nn.relu)(dropout_emb)
pool1 = GlobalMaxPool1D()(conv1)</p>
<p>conv2 = Conv1D(
    filters=128,
    kernel_size=4,
    padding='valid',
    activation=tf.nn.relu)(dropout_emb)
pool2 = GlobalMaxPool1D()(conv2)</p>
<p>conv3 = Conv1D(
    filters=128,
    kernel_size=5,
    padding='valid',
    activation=tf.nn.relu)(dropout_emb)
pool3 = GlobalMaxPool1D()(conv3)</p>
<h1 id="345gram-이후-합치기">3,4,5gram 이후 합치기</h1>
<p>concat = concatenate([pool1, pool2, pool3])</p>
<p>hidden = Dense(128, activation=tf.nn.relu)(concat)
dropout_hidden = Dropout(rate=dropout_prob)(hidden)
logits = Dense(5, name='logits')(dropout_hidden)
predictions = Dense(5, activation=tf.nn.softmax)(logits)</p>
<h1 id="모델-생성">모델 생성</h1>
<p>model = Model(inputs=input_layer, outputs=predictions)
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])</p>
<h1 id="모델-학습">모델 학습</h1>
<p>model.fit(train_ds, validation_data=val_ds, epochs=EPOCH, verbose=1)</p>
<h1 id="모델-평가테스트-데이터-셋-이용">모델 평가(테스트 데이터 셋 이용)</h1>
<p>loss, accuracy = model.evaluate(test_ds, verbose=1)
print('Accuracy: %f' % (accuracy * 100))
print('loss: %f' % (loss))</p>
<h1 id="모델-저장">모델 저장</h1>
<p>model.save('intent_model.h5')</p>
<pre><code>
- 실행</code></pre><p>cd c:/flyai/chatbot/models/intent
python train_model.py</p>
<pre><code>

### 9) model/intent/intentModel.py
</code></pre><p>import tensorflow as tf
from tensorflow.keras.models import Model, load_model
from tensorflow.keras import preprocessing</p>
<h1 id="의도-분류-모델-모듈">의도 분류 모델 모듈</h1>
<p>class IntentModel:
    def <strong>init</strong>(self, model_name, proprocess):</p>
<pre><code>    # 의도 클래스 별 레이블
    self.labels = {0: &quot;인사&quot;, 1: &quot;욕설&quot;, 2: &quot;주문&quot;, 3: &quot;예약&quot;, 4: &quot;기타&quot;}

    # 의도 분류 모델 불러오기
    self.model = load_model(model_name)

    # 챗봇 Preprocess 객체
    self.p = proprocess


# 의도 클래스 예측
def predict_class(self, query):
    # 형태소 분석
    pos = self.p.pos(query)

    # 문장내 키워드 추출(불용어 제거)
    keywords = self.p.get_keywords(pos, without_tag=True)
    sequences = [self.p.get_wordidx_sequence(keywords)]

    # 단어 시퀀스 벡터 크기
    from config.GlobalParams import MAX_SEQ_LEN

    # 패딩처리
    padded_seqs = preprocessing.sequence.pad_sequences(sequences, maxlen=MAX_SEQ_LEN, padding='post')

    predict = self.model.predict(padded_seqs)
    predict_class = tf.math.argmax(predict, axis=1)
    return predict_class.numpy()[0]</code></pre><pre><code>

### 10) test/model_intent_test.py
</code></pre><p>import sys
sys.path.append('c:/flyai/chatbot')
from utils.Preprocess import Preprocess
from models.intent.IntentModel import IntentModel</p>
<p>p = Preprocess(word2index_dic='../train_tools/dict/chatbot_dict.bin',
               userdic='../utils/user_dic.tsv')</p>
<p>intent = IntentModel(model_name='../models/intent/intent_model.h5', proprocess=p)</p>
<p>query = &quot;씨벌 전화좀 받아라&quot;
predict = intent.predict_class(query)
predict_label = intent.labels[predict]</p>
<pre><code>
- 실행
</code></pre><p>cd c:/flyai/chatbot/test
python model_intent_test.py</p>
<pre><code>
- 결과
![](https://velog.velcdn.com/images/rimgosu/post/dddce49d-90c8-4ee0-90c5-e9b2be18093f/image.png)


## 5. 개체명 인식 모델 학습
### 1) models/ner/ner_train.txt
- 경로에 붙여넣기
![](https://velog.velcdn.com/images/rimgosu/post/e6b87a47-0e69-4e91-8072-7a5cd9c3885f/image.png)


### 2) /models/ner/train_model.py
</code></pre><p>import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import preprocessing
from sklearn.model_selection import train_test_split
import numpy as np
import sys
sys.path.append('c:/flyai/chatbot')
from utils.Preprocess import Preprocess</p>
<h1 id="학습-파일-불러오기">학습 파일 불러오기</h1>
<p>def read_file(file_name):
    sents = []
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for idx, l in enumerate(lines):
            if l[0] == ';' and lines[idx + 1][0] == '$':
                this_sent = []
            elif l[0] == '$' and lines[idx - 1][0] == ';':
                continue
            elif l[0] == '\n':
                sents.append(this_sent)
            else:
                this_sent.append(tuple(l.split()))
    return sents</p>
<p>p = Preprocess(word2index_dic='../../train_tools/dict/chatbot_dict.bin',
               userdic='../../utils/user_dic.tsv')</p>
<h1 id="학습용-말뭉치-데이터를-불러옴">학습용 말뭉치 데이터를 불러옴</h1>
<p>corpus = read_file('ner_train.txt')</p>
<h1 id="말뭉치-데이터에서-단어와-bio-태그만-불러와-학습용-데이터셋-생성">말뭉치 데이터에서 단어와 BIO 태그만 불러와 학습용 데이터셋 생성</h1>
<p>sentences, tags = [], []
for t in corpus:
    tagged_sentence = []
    sentence, bio_tag = [], []
    for w in t:
        tagged_sentence.append((w[1], w[3]))
        sentence.append(w[1])
        bio_tag.append(w[3])</p>
<pre><code>sentences.append(sentence)
tags.append(bio_tag)</code></pre><p>print(&quot;샘플 크기 : \n&quot;, len(sentences))
print(&quot;0번 째 샘플 단어 시퀀스 : \n&quot;, sentences[0])
print(&quot;0번 째 샘플 bio 태그 : \n&quot;, tags[0])
print(&quot;샘플 단어 시퀀스 최대 길이 :&quot;, max(len(l) for l in sentences))
print(&quot;샘플 단어 시퀀스 평균 길이 :&quot;, (sum(map(len, sentences))/len(sentences)))</p>
<h1 id="토크나이저-정의">토크나이저 정의</h1>
<p>tag_tokenizer = preprocessing.text.Tokenizer(lower=False) # 태그 정보는 lower=False 소문자로 변환하지 않는다.
tag_tokenizer.fit_on_texts(tags)</p>
<h1 id="단어사전-및-태그-사전-크기">단어사전 및 태그 사전 크기</h1>
<p>vocab_size = len(p.word_index) + 1
tag_size = len(tag_tokenizer.word_index) + 1
print(&quot;BIO 태그 사전 크기 :&quot;, tag_size)
print(&quot;단어 사전 크기 :&quot;, vocab_size)</p>
<h1 id="학습용-단어-시퀀스-생성">학습용 단어 시퀀스 생성</h1>
<p>x_train = [p.get_wordidx_sequence(sent) for sent in sentences]
y_train = tag_tokenizer.texts_to_sequences(tags)</p>
<p>index_to_ner = tag_tokenizer.index_word # 시퀀스 인덱스를 NER로 변환 하기 위해 사용
index_to_ner[0] = 'PAD'</p>
<h1 id="시퀀스-패딩-처리">시퀀스 패딩 처리</h1>
<p>max_len = 40
x_train = preprocessing.sequence.pad_sequences(x_train, padding='post', maxlen=max_len)
y_train = preprocessing.sequence.pad_sequences(y_train, padding='post', maxlen=max_len)</p>
<h1 id="학습-데이터와-테스트-데이터를-82의-비율로-분리">학습 데이터와 테스트 데이터를 8:2의 비율로 분리</h1>
<p>x_train, x_test, y_train, y_test = train_test_split(x_train, y_train,
                                                    test_size=.2,
                                                    random_state=1234)</p>
<h1 id="출력-데이터를-one-hot-encoding">출력 데이터를 one-hot encoding</h1>
<p>y_train = tf.keras.utils.to_categorical(y_train, num_classes=tag_size)
y_test = tf.keras.utils.to_categorical(y_test, num_classes=tag_size)</p>
<p>print(&quot;학습 샘플 시퀀스 형상 : &quot;, x_train.shape)
print(&quot;학습 샘플 레이블 형상 : &quot;, y_train.shape)
print(&quot;테스트 샘플 시퀀스 형상 : &quot;, x_test.shape)
print(&quot;테스트 샘플 레이블 형상 : &quot;, y_test.shape)</p>
<h1 id="모델-정의-bi-lstm">모델 정의 (Bi-LSTM)</h1>
<p>from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Embedding, Dense, TimeDistributed, Dropout, Bidirectional
from tensorflow.keras.optimizers import Adam</p>
<p>model = Sequential()
model.add(Embedding(input_dim=vocab_size, output_dim=30, input_length=max_len, mask_zero=True))
model.add(Bidirectional(LSTM(200, return_sequences=True, dropout=0.50, recurrent_dropout=0.25)))
model.add(TimeDistributed(Dense(tag_size, activation='softmax')))
model.compile(loss='categorical_crossentropy', optimizer=Adam(0.01), metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=128, epochs=10)</p>
<p>print(&quot;평가 결과 : &quot;, model.evaluate(x_test, y_test)[1])
model.save('ner_model.h5')</p>
<h1 id="시퀀스를-ner-태그로-변환">시퀀스를 NER 태그로 변환</h1>
<p>def sequences_to_tag(sequences):  # 예측값을 index_to_ner를 사용하여 태깅 정보로 변경하는 함수.
    result = []
    for sequence in sequences:  # 전체 시퀀스로부터 시퀀스를 하나씩 꺼낸다.
        temp = []
        for pred in sequence:  # 시퀀스로부터 예측값을 하나씩 꺼낸다.
            pred_index = np.argmax(pred)  # 예를 들어 [0, 0, 1, 0 ,0]라면 1의 인덱스인 2를 리턴한다.
            temp.append(index_to_ner[pred_index].replace(&quot;PAD&quot;, &quot;O&quot;))  # 'PAD'는 'O'로 변경
        result.append(temp)
    return result</p>
<h1 id="f1-스코어-계산을-위해-사용">f1 스코어 계산을 위해 사용</h1>
<p>from seqeval.metrics import f1_score, classification_report</p>
<h1 id="테스트-데이터셋의-ner-예측">테스트 데이터셋의 NER 예측</h1>
<p>y_predicted = model.predict(x_test)
pred_tags = sequences_to_tag(y_predicted) # 예측된 NER
test_tags = sequences_to_tag(y_test)    # 실제 NER</p>
<h1 id="f1-평가-결과">F1 평가 결과</h1>
<p>print(classification_report(test_tags, pred_tags))
print(&quot;F1-score: {:.1%}&quot;.format(f1_score(test_tags, pred_tags)))</p>
<pre><code>
- 실행
</code></pre><p>cd c:/flyai/chatbot/models/ner
python train_model.py</p>
<pre><code>


### 3) models/ner/NerModel.py
- 챗봇 엔진 NER 모델 모듈
</code></pre><p>import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Model, load_model
from tensorflow.keras import preprocessing</p>
<h1 id="개체명-인식-모델-모듈">개체명 인식 모델 모듈</h1>
<p>class NerModel:
    def <strong>init</strong>(self, model_name, proprocess):</p>
<pre><code>    # BIO 태그 클래스 별 레이블
    self.index_to_ner = {1: 'O', 2: 'B_DT', 3: 'B_FOOD', 4: 'I', 5: 'B_OG', 6: 'B_PS', 7: 'B_LC', 8: 'NNP', 9: 'B_TI', 0: 'PAD'}

    # 의도 분류 모델 불러오기
    self.model = load_model(model_name)

    # 챗봇 Preprocess 객체
    self.p = proprocess


# 개체명 클래스 예측
def predict(self, query):
    # 형태소 분석
    pos = self.p.pos(query)

    # 문장내 키워드 추출(불용어 제거)
    keywords = self.p.get_keywords(pos, without_tag=True)
    sequences = [self.p.get_wordidx_sequence(keywords)]

    # 패딩처리
    max_len = 40
    padded_seqs = preprocessing.sequence.pad_sequences(sequences, padding=&quot;post&quot;, value=0, maxlen=max_len)

    predict = self.model.predict(np.array([padded_seqs[0]]))
    predict_class = tf.math.argmax(predict, axis=-1)

    tags = [self.index_to_ner[i] for i in predict_class.numpy()[0]]
    return list(zip(keywords, tags))

def predict_tags(self, query):
    # 형태소 분석
    pos = self.p.pos(query)

    # 문장내 키워드 추출(불용어 제거)
    keywords = self.p.get_keywords(pos, without_tag=True)
    sequences = [self.p.get_wordidx_sequence(keywords)]

    # 패딩처리
    max_len = 40
    padded_seqs = preprocessing.sequence.pad_sequences(sequences, padding=&quot;post&quot;, value=0, maxlen=max_len)

    predict = self.model.predict(np.array([padded_seqs[0]]))
    predict_class = tf.math.argmax(predict, axis=-1)

    tags = []
    for tag_idx in predict_class.numpy()[0]:
        if tag_idx == 1: continue
        tags.append(self.index_to_ner[tag_idx])

    if len(tags) == 0: return None
    return tags</code></pre><pre><code>

### 4) test/model_ner_test.py
</code></pre><p>import sys
sys.path.append('c:/flyai/chatbot')
from utils.Preprocess import Preprocess
from models.ner.NerModel import NerModel</p>
<p>p = Preprocess(word2index_dic='../train_tools/dict/chatbot_dict.bin',
               userdic='../utils/user_dic.tsv')</p>
<p>ner = NerModel(model_name='../models/ner/ner_model.h5', proprocess=p)
query = '오늘 오전 13시 2분에 탕수육 주문 하고 싶어요'
predicts = ner.predict(query)
tags = ner.predict_tags(query)
print(predicts)
print(tags)</p>
<pre><code>
- 실행</code></pre><p>cd c:/flyai/chatbot/test
python model_ner_test.py
```</p>