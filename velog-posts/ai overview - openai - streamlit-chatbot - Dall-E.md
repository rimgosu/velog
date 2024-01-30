<h1 id="ai-overview">ai overview</h1>
<h2 id="chatgpt">chatGPT</h2>
<ul>
<li><a href="https://openai.com/product">https://openai.com/product</a></li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/c8070816-61ec-45ff-9960-94092c196365/image.png" /></p>
<ul>
<li>wisper같은 오픈 소스 있음.</li>
</ul>
<h3 id="rlhf">RLHF</h3>
<ul>
<li>비도덕적인건 대답 못하게 하나하나 강화학습을 했음.
<img alt="" src="https://velog.velcdn.com/images/rimgosu/post/7d41775c-0202-4214-a0d4-e3279ac233c3/image.png" /></li>
</ul>
<h3 id="models">models</h3>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/b29f6f90-62e2-45ae-9021-5119040c4a35/image.png" />
<img alt="" src="https://velog.velcdn.com/images/rimgosu/post/18bdc0d1-1bdf-4fe0-8511-3677a0021814/image.png" /></p>
<h2 id="midjourney">midjourney</h2>
<ul>
<li><a href="https://legacy.midjourney.com/showcase/recent/">https://legacy.midjourney.com/showcase/recent/</a></li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/6ea87e25-e4ad-4169-bf7c-7ebe2683ff05/image.png" /></p>
<h2 id="token">token</h2>
<ul>
<li><a href="https://platform.openai.com/tokenizer">https://platform.openai.com/tokenizer</a></li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/b982f664-2147-4620-982f-6ae7f7131b57/image.png" /></p>
<h2 id="comparison-if-revenue">comparison if revenue</h2>
<ul>
<li><a href="https://www.detectx.com.au/comparison-of-revenue-structure-and-breakdown-cost-of-last-q3-2022-results-of-amazon-apple-microsoft-google/">https://www.detectx.com.au/comparison-of-revenue-structure-and-breakdown-cost-of-last-q3-2022-results-of-amazon-apple-microsoft-google/</a></li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/9c88ed03-f420-45c6-80d0-1e37b2f25f19/image.png" /></p>
<h2 id="bing-creator">bing creator</h2>
<ul>
<li><a href="https://www.bing.com/images/create">https://www.bing.com/images/create</a></li>
<li>DAL-E 3 탑재되어있음.</li>
</ul>
<h2 id="streamlit">streamlit</h2>
<ul>
<li><a href="https://streamlit.io">https://streamlit.io</a></li>
</ul>
<h1 id="openai-모델-fine-tuning">openai 모델 fine tuning</h1>
<h2 id="의존성-설치">의존성 설치</h2>
<pre><code>pip install openai
pip install streamlit</code></pre><h2 id="azure-openai">azure openai</h2>
<ul>
<li>azure - 리소스그룹 만들기 - azure openai</li>
<li>지역: sweden central (최근 생긴 데이터 센터라 좋다)</li>
<li><strong>openai machine learning studio</strong> 공간이 따로 있어서, 그 공간에서 따로 작업할 수 있다.</li>
<li>키 및 엔드포인트에 있는 항목 복사 붙여넣기 해놓자. (실습시는 따로 공유받아서 사용할 것임)</li>
</ul>
<h2 id="openai-machine-learning-studio">openai machine learning studio</h2>
<ul>
<li>다음 공간에서 openai 파인튜닝 쉽게 가능하다.</li>
</ul>
<h2 id="samplepy">SAMPLE.PY</h2>
<pre><code>import openai
import os

OPENAI_API_KEY='6e65e9d2d05c4c9a8560cdc88595e14f'
OPENAI_API_ENDPOINT='https://sktfly2.openai.azure.com/'
OPENAI_API_TYPE = 'azure'
OEPNAI_API_VERSION = '2023-05-15'

openai.api_key = OPENAI_API_KEY
openai.azure_endpoint = OPENAI_API_ENDPOINT
openai.api_type = OPENAI_API_TYPE
openai.api_version = OEPNAI_API_VERSION

query = '나 지금 너무 힘들어.. 위로해줘'

# T의 대답
result = openai.chat.completions.create(
    model='dev-model',
    temperature=0,
    messages=[
        {'role':'system', 'content':'you are a helpful assistant.'},
        {'role':'user', 'content':query}
    ]
)

# F의 대답
result2 = openai.chat.completions.create(
    model='dev-model',
    temperature=1,
    messages=[
        {'role':'system', 'content':'you are a helpful assistant.'},
        {'role':'user', 'content':query}
    ]
)

print(result.choices[0].message.content)

print(result2.choices[0].message.content)</code></pre><h1 id="streamlit-1">streamlit</h1>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/b48143ea-7e42-44ee-bff0-c4c48a66275e/image.png" /></p>
<h2 id="streamlit-chatbot">streamlit-chatbot</h2>
<ul>
<li>실행</li>
</ul>
<pre><code>streamlit run streamlit-00.py</code></pre><ul>
<li><code>streamlit-chatbot.py</code><pre><code>import openai
import os
import streamlit as st
&quot;&quot;&quot;document
</code></pre></li>
</ul>
<p><a href="https://docs.streamlit.io/library/api-reference/widgets/st.text_input">https://docs.streamlit.io/library/api-reference/widgets/st.text_input</a>
<a href="https://docs.streamlit.io/library/api-reference/widgets/st.button">https://docs.streamlit.io/library/api-reference/widgets/st.button</a>
<a href="https://docs.streamlit.io/library/api-reference/status/st.spinner">https://docs.streamlit.io/library/api-reference/status/st.spinner</a>
&quot;&quot;&quot;</p>
<p>OPENAI_API_KEY='6e65e9d2d05c4c9a8560cdc88595e14f'
OPENAI_API_ENDPOINT='<a href="https://sktfly2.openai.azure.com/'">https://sktfly2.openai.azure.com/'</a>
OPENAI_API_TYPE = 'azure'
OEPNAI_API_VERSION = '2023-05-15'</p>
<p>openai.api_key = OPENAI_API_KEY
openai.azure_endpoint = OPENAI_API_ENDPOINT
openai.api_type = OPENAI_API_TYPE
openai.api_version = OEPNAI_API_VERSION</p>
<p>st.header('welcome to GPT Bot', divider='rainbow')
st.write('궁금한 것을 물어보세요!')</p>
<p>query = st.text_input('Query? ')
button_click = st.button(&quot;run&quot;)</p>
<p>if button_click:
    with st.spinner('please wait...'):</p>
<pre><code>    result = openai.chat.completions.create(
        model='dev-model',
        temperature=0,
        messages=[
            {'role':'system', 'content':'you are a helpful assistant.'},
            {'role':'user', 'content':query}
        ]
    )

    st.write(result.choices[0].message.content)
    st.success('done!')</code></pre><pre><code>
## streamlit-시 작성 봇
- `poem bot.py`</code></pre><p>import openai
import os
import streamlit as st
&quot;&quot;&quot;document</p>
<p>st.text_area : <a href="https://docs.streamlit.io/library/api-reference/widgets/st.text_area">https://docs.streamlit.io/library/api-reference/widgets/st.text_area</a>
&quot;&quot;&quot;</p>
<p>OPENAI_API_KEY='6e65e9d2d05c4c9a8560cdc88595e14f'
OPENAI_API_ENDPOINT='<a href="https://sktfly2.openai.azure.com/'">https://sktfly2.openai.azure.com/'</a>
OPENAI_API_TYPE = 'azure'
OEPNAI_API_VERSION = '2023-05-15'</p>
<p>openai.api_key = OPENAI_API_KEY
openai.azure_endpoint = OPENAI_API_ENDPOINT
openai.api_type = OPENAI_API_TYPE
openai.api_version = OEPNAI_API_VERSION</p>
<p>st.header('welcome to AI Poem', divider='rainbow')
st.write('아름다운 시를 함께 지어보아요')</p>
<p>name = st.text_input('작가의 이름을 입력하세요')
if name:
    st.write(f'{name}님 반갑습니다.')</p>
<p>subject = st.text_input('시의 주제를 입력하세요')
content = st.text_area('시의 내용을 입력하세요')</p>
<p>button_click = st.button(&quot;RUN&quot;)</p>
<p>if button_click:
    with st.spinner('please wait...'):</p>
<pre><code>    result = openai.chat.completions.create(
        model='dev-model',
        temperature=1,
        messages=[
            {'role':'system', 'content':'you are a helpful assistant.'},
            {'role':'user', 'content':f'작가의 이름은 {name}'},
            {'role':'user', 'content':f'시의 주제는 {subject}'},
            {'role':'user', 'content':f'시의 내용은 {content}'},
            {'role':'user', 'content':f'이 정보로 시를 생성해줘.'}
        ]
    )

    st.success('done!')
    st.write(result.choices[0].message.content)</code></pre><pre><code>
## 공식문서 보는법
- &lt;https://docs.streamlit.io/library/api-reference/write-magic/st.write&gt;
- 위 검색창에서 필요한 기능 검색 - 예제 복붙해서 사용



# Dall-E
![](https://velog.velcdn.com/images/rimgosu/post/bf3ad18b-8566-40a8-b5fa-1065503c1f04/image.png)
![](https://velog.velcdn.com/images/rimgosu/post/c68579b7-496d-484a-acb9-66f04c5bb966/image.png)
![](https://velog.velcdn.com/images/rimgosu/post/e3264bd5-717a-4066-b7d7-5e662ab677f4/image.png)
![](https://velog.velcdn.com/images/rimgosu/post/7ac81f4a-f133-450f-9d91-b2797eb90988/image.png)
![](https://velog.velcdn.com/images/rimgosu/post/dda92c61-f8eb-4694-9cb3-9ad072c0d88d/image.png)
![](https://velog.velcdn.com/images/rimgosu/post/9d99ea7a-36f1-4d5b-83ef-659dffd1b6f1/image.png)
![](https://velog.velcdn.com/images/rimgosu/post/662fca10-3339-44ba-adb7-19e2f7666467/image.png)
![](https://velog.velcdn.com/images/rimgosu/post/4b0a1d21-89d2-437b-b2c6-f6ffd010e239/image.png)
![](https://velog.velcdn.com/images/rimgosu/post/c3d6d3e8-252c-45ce-9fc9-2d06fdba007d/image.png)
![](https://velog.velcdn.com/images/rimgosu/post/fcef6a2c-a3be-4acc-9408-c3448448be64/image.png)
![](https://velog.velcdn.com/images/rimgosu/post/e3719255-e798-4d4c-a8dc-6430cd6f29f0/image.png)
![](https://velog.velcdn.com/images/rimgosu/post/5b9e39f2-0493-48e0-b490-75e1a2e63e97/image.png)</code></pre>