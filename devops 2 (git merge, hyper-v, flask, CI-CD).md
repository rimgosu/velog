<h1 id="git">git</h1>
<h2 id="깃허브와-원격으로-연동">깃허브와 원격으로 연동</h2>
<ul>
<li>토큰받아야함</li>
<li><a href="https://github.com/settings/tokens/new">https://github.com/settings/tokens/new</a></li>
<li>repo, workflow 권한 받음<ul>
<li>workflow : github action에 사용</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/d63d7b84-b2fa-4b8e-902e-05147051a761/image.png" /></p>
<h3 id="자격-증명">자격 증명</h3>
<ul>
<li>검색 - 자격증명 관리자 - 일반 자격 증명 추가<ul>
<li>인터넷 주소 : git:<a href="https://github.com">https://github.com</a></li>
<li>이름 : rimgosu</li>
<li>암호 : 깃허브에서 받은 토큰</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/5799dc7f-dc29-48f3-8e46-e3a52623d8e5/image.png" /></p>
<h3 id="sourcetree에서-연동">sourcetree에서 연동</h3>
<ul>
<li>도구 - 옵션 - 인증</li>
<li>원격! 클릭 후 저장소 연동할 수 있다. git remote add origin이랑 같은 역할을 할 수 있음.</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/2ca3b6f3-78eb-4dfb-b30a-0e60429c2dd8/image.png" /></p>
<h3 id="깃허브-저장소-만들기👍">깃허브 저장소 만들기👍</h3>
<ul>
<li>gitignore 탭에서 python, java 등 주 언어를 선택하면 자동으로 gitignore를 생성해준다 </li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/937b6bbc-3690-445c-aa7d-b8939bae86f8/image.png" /></p>
<h2 id="vs-코드-빠른-실행👍">vs 코드 빠른 실행👍</h2>
<ul>
<li>탐색기에서 cmd 검색</li>
<li>code . =&gt; vs 코드 폴더 선택하여 실행 할 수 있다.</li>
</ul>
<h2 id="octoverse">octoverse</h2>
<ul>
<li>귀여운 깃허브 캐릭터 모음</li>
<li><a href="https://octodex.github.com/">https://octodex.github.com/</a></li>
</ul>
<h1 id="hyper-v-ubuntu">hyper-v ubuntu</h1>
<h2 id="검사점-만들기">검사점 만들기</h2>
<ul>
<li>컴퓨터 끄기 - 우클릭 - 검사점 : 현 상태를 저장하는 스냅샷 만들기</li>
</ul>
<h2 id="복사-붙여넣기-설정">복사 붙여넣기 설정</h2>
<ul>
<li>원래 자동으로 되는데, 안되면 다음 설정을 참고할 것</li>
<li>ctrl+shift+c/v 로 복붙 가능하다.</li>
<li><a href="https://leemcse.tistory.com/entry/Hyper-V-%ED%98%B8%EC%8A%A4%ED%8A%B8%EC%99%80-%EA%B2%8C%EC%8A%A4%ED%8A%B8-%EC%BB%B4%ED%93%A8%ED%84%B0-%ED%8C%8C%EC%9D%BC-%EB%B3%B5%EC%82%AC-%EB%B0%A9%EB%B2%95">https://leemcse.tistory.com/entry/Hyper-V</a></li>
<li>고급 세션 설정 : <a href="https://lucidmaj7.tistory.com/343">https://lucidmaj7.tistory.com/343</a></li>
</ul>
<h2 id="가상환경에서-깃허브-push👍">가상환경에서 깃허브 push👍</h2>
<ul>
<li>push 할 때 username, password를 요구한다.</li>
<li>위의 &quot;깃허브와 원격으로 연동&quot; 메뉴를 참고하여 토큰을 발급받고, username에는 rimgosu, password에는 토큰을 넣으면 된다.</li>
<li>다음 명령을 통해 한 번 인증하면 다음부터는 인증을 요구하지 않는 설정을 할 수 있다.<pre><code>git config --global credential.helper cache</code></pre></li>
</ul>
<h1 id="flask">flask</h1>
<h2 id="flask-실행">flask 실행</h2>
<ul>
<li><a href="https://github.com/rimgosu/python-env-test">https://github.com/rimgosu/python-env-test</a></li>
<li>app.py<pre><code>from flask import Flask
app = Flask(__name__)
</code></pre></li>
</ul>
<p>@app.route(&quot;/&quot;)
def home():
    return &quot;Hello, Flask!&quot;</p>
<pre><code>- 실행
   - host 지정을 0.0.0.0으로 해야 외부에서 접속 가능하다. 
   컴퓨터의 모든 자원을 다쓰겠다는 의미.
   - http://127.0.0.1:5000 : 루프백 주소
   - http://172.23.253.76:5000 : 외부에서 접속 가능한 주소
</code></pre><p>$ python -m flask run --host=0.0.0.0 --port=5000
Running on all addresses (0.0.0.0)</p>
<ul>
<li>Running on <a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a></li>
<li>Running on <a href="http://172.23.253.76:5000">http://172.23.253.76:5000</a><pre><code></code></pre></li>
</ul>
<ul>
<li><p>가상환경에서 실행</p>
<pre><code>python3 -m flask run --host=0.0.0.0 --port=5000</code></pre></li>
<li><p>flask 기본 세팅</p>
</li>
<li><p>다음 문구를 추가하면 된다.</p>
</li>
</ul>
<pre><code>if __name__ == '__main__':
    app.run('0.0.0.0', 5000, True)</code></pre><pre><code>$ python3 app.py</code></pre><h2 id="return-데이터-가져오기">return 데이터 가져오기</h2>
<pre><code>$ curl 127.0.0.1:5000
Hello, Flask!</code></pre><h2 id="flask-snippets-설치">flask-snippets 설치</h2>
<ul>
<li>vs코드에서 flask-snippets 검색 후 설치하도록 하자.</li>
</ul>
<h2 id="wsgi-server-✅">WSGI Server ✅</h2>
<ul>
<li>python3 -m flask run --host=0.0.0.0 --port=5000 명령어로 실행하면 작은(개발자 전용) 서버를 배포해준다. 그럼으로 실제 배포에선 WSGI 같은 큰 서버에 배포를 해야한다.<pre><code>WARNING: This is a development server. 
Do not use it in a production deployment. 
Use a production WSGI server instead.</code></pre><h3 id="gunicorn">Gunicorn</h3>
</li>
<li>WSGI 서버 배포를 도와주는 녀석</li>
<li>아파치 tomcat 같은 녀석임.</li>
</ul>
<h2 id="인바운드-규칙-편집-✅">인바운드 규칙 편집 ✅</h2>
<ul>
<li>시작 - 고급 보안이 포함된 Window Defender 방화벽 - 인바운드 규칙 - 새 규칙 - 5000번 포트 TCP 추가</li>
<li>같은 와이파이 망 내에서 접속 가능하게 된다.</li>
</ul>
<h1 id="cicd">CI/CD</h1>
<ul>
<li>Continuous Integration/Continuous Delivery</li>
<li>애플리케이션 개발 단계를 자동화하여 애플리케이션을 더욱 짧은 주기로 고객에게 제공</li>
<li>devops 툴 보여주는 사이트 : <a href="https://landscape.cncf.io/">https://landscape.cncf.io/</a></li>
</ul>
<h2 id="github-action">github action</h2>
<ul>
<li>github - action - python application - configure</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/f8ff09b9-aeca-487d-b52f-ff79c72f97e0/image.png" /></p>
<h3 id="configuration">configuration</h3>
<ul>
<li><p>configuration docx : <a href="https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows">https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows</a></p>
</li>
<li><p>github action 명령어 검색 : <a href="https://github.com/actions">https://github.com/actions</a></p>
</li>
</ul>
<h3 id="python-appyml">python-app.yml</h3>
<pre><code># This workflow will install Python dependencies, run tests and lint with a single version of Python
# For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python

name: Python application

on:
  push:
    branches: [ &quot;master&quot; ]
  pull_request:
    branches: [ &quot;master&quot; ]

permissions:
  contents: read

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: &quot;3.10&quot;
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Lint with flake8
      run: |
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Test with pytest
      run: |
        pytest
</code></pre><ol>
<li>runs-on: ubuntu-latest : 컴퓨터 하나 새로 생성한다는 의미</li>
<li>uses: actions/checkout@v3 : checkout version 3 깃 클론으로 설치한다는 의미</li>
<li>uses : action/setup-python@v3 : python 설치하라는 의미</li>
</ol>
<h3 id="github-action-실습1">github action 실습1</h3>
<pre><code>name: Python application

on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: &quot;3.8&quot;
    - name: Display Python version
      run: python -c &quot;import sys; print(sys.version)&quot;</code></pre><h3 id="github-action-실습2">github action 실습2</h3>
<pre><code>name: Python application

on:
  push:
    branches: [ master ]

jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        python-version: ['3.6', '3.8']
        exclude:
          - os: macos-latest
            python-version: '3.8'
          - os: windows-latest
            python-version: '3.6'

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    - name: Display Python version
      run: python -c &quot;import sys; print(sys.version)&quot;</code></pre><h2 id="docker">docker</h2>
<ul>
<li>Dockerfile</li>
</ul>
<pre><code># syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ &quot;python3&quot;, &quot;-m&quot; , &quot;flask&quot;, &quot;run&quot;, &quot;--host=0.0.0.0&quot;]</code></pre><h3 id="docker-hub">docker hub</h3>
<ul>
<li><a href="https://hub.docker.com/">https://hub.docker.com/</a></li>
<li>docker 이미지 저장소임</li>
<li>github-actions-app으로 저장도 생성하자</li>
</ul>
<h3 id="github-action-실습3">github action 실습3</h3>
<ul>
<li>Docker Build &amp; Push Action</li>
<li>커밋하면 자동으로 Docker 이미지 생성</li>
</ul>
<pre><code>name: Python application

on:
  push:
    branches: [ main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: &quot;3.8&quot;
    - name: Display Python version
      run: python -c &quot;import sys; print(sys.version)&quot;
    - name: Build &amp; push Docker image
      uses: mr-smithers-excellent/docker-build-push@v5
      with:
        image: 도커허브 계정/github-actions-app
        tags: v3, latest
        registry: docker.io
        username: ${{ secrets.DOCKER_USERNAME }} # 또는 도커허브 계정
        password: ${{ secrets.DOCKER_PASSWORD }} # 또는 토큰</code></pre><ul>
<li>${{}} : 추후 github 세팅으로 환경변수 세팅해줄 수 있다.</li>
<li>토큰 : <a href="https://hub.docker.com/settings/security">https://hub.docker.com/settings/security</a> 에서 발급</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/4cee6a6e-5358-4d1f-85f7-725b556c1194/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/a72fe784-872f-4f57-813a-a4acf9c35e52/image.png" /></p>
<ul>
<li>커밋하면 바로 Docker hub 에 배포되는 것을 볼 수 있다.</li>
</ul>
<h2 id="젠킨스">젠킨스</h2>
<h3 id="젠킨스-설치">젠킨스 설치</h3>
<ul>
<li><p>hyper-v 환경</p>
</li>
<li><p>jdk 설치</p>
<pre><code>sudo apt-get install openjdk-11-jre</code></pre></li>
<li><p>jdk : 개발자들이 필요한거 다 필요하다</p>
</li>
<li><p>jre : 경량화되어 프로덕션 배포때 이걸로 설치하면된다.</p>
</li>
<li><p>젠킨스 설치(오류 발생)</p>
<ul>
<li>트러블 슈팅 : <a href="https://lonaru-burnout.tistory.com/5">https://lonaru-burnout.tistory.com/5</a><pre><code>$ wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
$ echo deb http://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list
$ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 5BA31D57EF5975CA
$ sudo apt-get update</code></pre></li>
</ul>
</li>
<li><p>설치 상태 보기</p>
<pre><code>sudo systemctl status jenkins</code></pre></li>
<li><p>초기 비밀번호 보기</p>
<pre><code>sudo cat /var/lib/jenkins/secrets/initialAdminPassword</code></pre></li>
</ul>
<h1 id="모니터링">모니터링</h1>
<ul>
<li>grafana : <a href="https://grafana.com/">https://grafana.com/</a></li>
<li><a href="https://play.grafana.org/d/000000012/grafana-play-home?orgId=1">https://play.grafana.org/d/000000012/grafana-play-home?orgId=1</a></li>
</ul>