<h2 id="✔️-todo">✔️ TODO</h2>
<ol>
<li>animated drawings windows =&gt; linux</li>
<li>감정 분석 백엔드 작업</li>
</ol>
<h2 id="✔️-animated-drawings">✔️ animated drawings</h2>
<h3 id="📋-libglso1-공유-객체-파일을-시스템에서-찾을-수-없음">📋 libGL.so.1 공유 객체 파일을 시스템에서 찾을 수 없음</h3>
<pre><code>sudo apt-get update
sudo apt-get install libgl1-mesa-glx</code></pre><h3 id="📋-opengl-문제">📋 opengl 문제</h3>
<ul>
<li><a href="https://github.com/facebookresearch/AnimatedDrawings/issues/99">https://github.com/facebookresearch/AnimatedDrawings/issues/99</a><pre><code>sudo apt-get install libosmesa6-dev freeglut3-dev
sudo apt-get install libglfw3-dev libgles2-mesa-dev
sudo apt-get install libosmesa6
export PYOPENGL_PLATFORM=osmesa
conda -c install conda-forge libstdcxx-ng</code></pre></li>
<li>해결되었다!</li>
</ul>
<h3 id="📋-docker-빌드">📋 docker 빌드</h3>
<ul>
<li>ubuntu 22.04 설치</li>
<li><a href="https://docs.docker.com/engine/install/ubuntu/">https://docs.docker.com/engine/install/ubuntu/</a></li>
</ul>
<h4 id="dockerignore"><code>.dockerignore</code></h4>
<pre><code># Git 관련 디렉토리와 파일
.git
.gitignore

# GitHub Actions 관련 디렉토리
.github

# PyCharm 프로젝트 디렉토리
.idea

# Python 가상 환경 디렉토리
venv

# pytest 캐시 디렉토리
.pytest_cache

# Python 바이트코드 파일
__pycache__

# 불필요한 큰 파일
anaconda.sh</code></pre><h4 id="dockerfile"><code>Dockerfile</code></h4>
<pre><code># Miniconda를 기반으로 하는 이미지 사용
FROM continuumio/miniconda3

# 환경 변수 설정으로 인터랙티브 모드를 비활성화하여 패키지 설치 중 사용자 입력 대기를 방지
ENV DEBIAN_FRONTEND=noninteractive

# 필요한 라이브러리 설치
RUN apt-get update &amp;&amp; apt-get install -y \
    libgl1-mesa-glx \
    libosmesa6-dev \
    freeglut3-dev \
    libglfw3-dev \
    libgles2-mesa-dev \
    libosmesa6 \
    &amp;&amp; apt-get clean \
    &amp;&amp; rm -rf /var/lib/apt/lists/*

# 작업 디렉토리 설정
WORKDIR /workdir

# Conda 환경 파일 및 현재 디렉토리의 소스 코드를 컨테이너로 복사
COPY . .

# Conda 환경 생성 및 활성화
RUN conda env create -f environment.yml

# Conda 환경을 실행 환경으로 설정
ENV PATH /opt/conda/envs/venv/bin:$PATH

# 환경 변수 설정으로 PyOpenGL이 osmesa를 사용하도록 설정
ENV PYOPENGL_PLATFORM=osmesa

# 컨테이너가 시작될 때 실행할 명령어 설정 (예: main.py 실행)
CMD [&quot;python&quot;, &quot;main.py&quot;]
</code></pre><h4 id="environmentyml"><code>environment.yml</code></h4>
<pre><code>name: venv
channels:
  - defaults
  - conda-forge
dependencies:
  - python=3.10
  - pip
  - pip:
      - -r /workdir/requirements.txt</code></pre><h2 id="✔️-감정분석-백엔드-api-만들기">✔️ 감정분석 백엔드 api 만들기</h2>
<h3 id="📋-wsl에서-gcc-컴파일러-설치">📋 wsl에서 gcc 컴파일러 설치</h3>
<pre><code>sudo apt-get update
sudo apt-get install build-essential
pip install Cython
</code></pre><h3 id="📋-fastapi-틀">📋 fastapi 틀</h3>
<ul>
<li><a href="https://github.com/tiangolo/full-stack-fastapi-postgresql/tree/master/src/backend/app">https://github.com/tiangolo/full-stack-fastapi-postgresql/tree/master/src/backend/app</a>    </li>
</ul>