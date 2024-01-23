<h2 id="pytorch-특징-및-장점">pytorch 특징 및 장점</h2>
<ul>
<li>요즘은 다 pytorch로 개발한다.</li>
<li>OpenAI <em>(텐서플로우는 Google이 만든 것)</em></li>
<li>print로 모델 찍으면 잘 찍힌다 <em>(텐서 플로우는 안찍힘)</em></li>
<li>디버깅 용이하다 <em>(텐서플로우는 학습중 디버깅 안됨)</em></li>
</ul>
<h3 id="텐서">텐서</h3>
<ul>
<li>파이토치의 데이터 형태</li>
<li>단일 데이터 형식으로 된 자료들의 다차원 행렬</li>
</ul>
<h3 id="동적-신경망">동적 신경망</h3>
<ul>
<li>훈련을 반복할 때마다 네트워크 변경이 가능한 신경망을 의미</li>
<li>예를들어 학습 중에 은닉층을 추가하거나 제거하는 등 모델의 네트워크 조작이 가능</li>
<li>연산 그래프를 정의하는 것과 동시에 값도 초기화되는 'Define by Run' 방식을 사용</li>
</ul>
<h3 id="torchautograd">torch.autograd</h3>
<ul>
<li>자동 미분 패키지</li>
<li>일반적으로 신경망에 사소한 변경이 있다면 신경망 구축을 처음부터 다시 시작해야되지만 쉽게 디버깅할 수 있음</li>
</ul>
<h3 id="torchnn">torch.nn</h3>
<ul>
<li>신경망을 쉽게 구축 가능</li>
</ul>
<h3 id="torchmultiprocessing">torch.multiprocessing</h3>
<ul>
<li>동일한 데이터에 다수가 접근 가능</li>
</ul>
<h3 id="torchutils">torch.utils</h3>
<ul>
<li>모델에 데이터를 제공해주는 역할</li>
</ul>
<h3 id="텐서를-메모리에-저장하기">텐서를 메모리에 저장하기</h3>
<ul>
<li>텐서는 1차원이든 N차원이든 메모리에 저장할 때는 1차원 배열 형태가 됨</li>
<li>변환된 1차원 배열을 <strong>스토리지</strong>라고 함</li>
<li>오프셋 / 스트라이드 개념 알아볼 것</li>
</ul>
<h2 id="anaconda에서-실습">anaconda에서 실습</h2>
<h3 id="가상환경-만들기">가상환경 만들기</h3>
<ul>
<li>python 3.10 이상을 설치하면 파이토치와 호환성 문제 있을 수 있어 3.9.0 버전으로 가상환경을 만들자.<pre><code>conda create -n torch_book python=3.9.0
conda activate torch_book</code></pre></li>
</ul>
<h4 id="가상환경-목록-확인">가상환경 목록 확인</h4>
<pre><code>conda env list</code></pre><h3 id="pytorch-설치">pytorch 설치</h3>
<pre><code>conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia</code></pre><h3 id="jupyter-notebook-설치">jupyter notebook 설치</h3>
<pre><code>pip install jupyter notebook
jupyter notebook</code></pre><h3 id="그-외-라이브러리-설치">그 외 라이브러리 설치</h3>
<pre><code>pip install matplotlib
pip install seaborn
pip install scikit-learn</code></pre><h2 id="pytorch-실습">pytorch 실습</h2>
<h3 id="데이터셋-다운로드">데이터셋 다운로드</h3>
<pre><code class="language-python">import torchvision.transforms as transforms

mnist_transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (1.0,))
]) #------ 평균 0.5, 표준편차 1.0으로 데이터를 정규화(normalize)하는 조정

from torchvision.datasets import MNIST
import requests

download_root = './chap02/data/MNIST_DATASET' #------ 내려받을 경로 지정

train_dataset = MNIST(download_root, transform=mnist_transform, train=True, download=True) #------ 학습(training) 데이터셋
valid_dataset = MNIST(download_root, transform=mnist_transform, train=False, download=True) #------ 검증(validation) 데이터셋
test_dataset = MNIST(download_root, transform=mnist_transform, train=False, download=True) #------ 테스트(test) 데이터셋
</code></pre>
<h3 id="신경망-만들기">신경망 만들기</h3>
<ul>
<li>계층(Layer) : 모듈 또는 모듈을 구성하는 한 개의 계층</li>
<li>모듈 : 한 개 이상의 계층이 모여서 구성된 것</li>
<li>모델 : 최종적으로 원하는 네트워크</li>
</ul>
<h3 id="npstack-vs-npconcat">np.stack vs np.concat</h3>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/694b9685-97dd-408c-83d1-f4feae6e0301/image.png" /></p>
<ul>
<li>stack을 늘리려면(차원을 늘리려면) 반드시 배열 크기 똑같아야한다.</li>
</ul>
<h3 id="np---torch">np -&gt; torch</h3>
<pre><code class="language-python">categorical_data = torch.tensor(categorical_data, dtype=torch.int64)
categorical_data[:10]</code></pre>
<h3 id="ravel-reshape-flatten">ravel(), reshape(), flatten()</h3>
<pre><code class="language-python">a = np.array([[1,2],[3,4]])
print(a.ravel())
print(a.reshape(-1))
print(a.flatten())</code></pre>
<ul>
<li>출력 결과<pre><code>[1 2 3 4]
[1 2 3 4]
[1 2 3 4]</code></pre></li>
</ul>
<h3 id="모델-네트워크-생성">모델 네트워크 생성</h3>
<pre><code class="language-python">class Model(nn.Module):
    def __init__(self, embedding_size, output_size, layers, p=0.4):
        super().__init__()
        self.all_embeddings = nn.ModuleList([nn.Embedding(ni, nf) for ni, nf in embedding_size])
        self.embedding_dropout = nn.Dropout(p)

        all_layers = []
        num_categorical_cols = sum((nf for ni, nf in embedding_size))
        input_size = num_categorical_cols

        for i in layers:
            all_layers.append(nn.Linear(input_size, i))
            all_layers.append(nn.ReLU(inplace=True))
            all_layers.append(nn.BatchNorm1d(i))
            all_layers.append(nn.Dropout(p))
            input_size = i

        all_layers.append(nn.Linear(layers[-1], output_size))
        self.layers = nn.Sequential(*all_layers)

    def forward(self, x_categorical):
        embeddings = []
        for i, e in enumerate(self.all_embeddings):
            embeddings.append(e(x_categorical[:, i]))
            x = torch.cat(embeddings, 1)
            x = self.embedding_dropout(x)
            x = self.layers(x)

            return x</code></pre>
<h3 id="모델-만들기">모델 만들기</h3>
<pre><code class="language-python">categorical_column_sizes = [len(dataset[column].cat.categories) for column in categorical_columns]
categorical_embedding_sizes = [(col_size, min(50, (col_size+1)//2)) for col_size in categorical_column_sizes]

total_records = 1728
test_records = int(total_records * .2)

categorical_train_data = categorical_data[:total_records - test_records]
categorical_test_data = categorical_data[total_records - test_records:total_records]
train_outputs = outputs[:total_records - test_records]
test_outputs = outputs[total_records - test_records:total_records]

print(categorical_embedding_sizes)

model = Model(categorical_embedding_sizes, 4, [200, 100, 50], p=0.4)
print(model)</code></pre>