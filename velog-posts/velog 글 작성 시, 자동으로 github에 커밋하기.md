<h1 id="velog-to-github">velog to github</h1>
<ul>
<li><a href="https://github.com/rimgosu/velog">https://github.com/rimgosu/velog</a></li>
<li>다음 레포지토리와 동일하게 셋팅 후, python 파일에서 자기 벨로그 주소를 적고, 권한 설정만 해주면 벨로그에 쓴 글을 자동으로 깃허브에 작성해준다.</li>
</ul>
<h2 id="1-github-새-레포지토리-만들기">1. github 새 레포지토리 만들기</h2>
<ul>
<li>public으로 다음과 같이 폴더를 구성해주고, github action을 위한 준비를 해주자.<pre><code>your-github-repo/
├── .github/
│   └── workflows/
│       └── update_blog.yml
├── scripts/
│   └── update_blog.py
└── ...</code></pre></li>
</ul>
<h2 id="2-github-action-작성">2. github action 작성</h2>
<ul>
<li><code>update_blog.yml</code></li>
</ul>
<pre><code>name: Update Blog Posts


on:
  push:
      branches:
        - master  # 또는 워크플로우를 트리거하고 싶은 브랜치 이름
  schedule:
    - cron: '0 0 * * *'  # 매일 자정에 실행

jobs:
  update_blog:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout
      uses: actions/checkout@v2

    - name: Push changes
      run: |
        git config --global user.name 'github-actions[bot]'
        git config --global user.email 'github-actions[bot]@users.noreply.github.com'
        git push https://${{ secrets.GH_PAT }}@github.com/rimgosu/velog.git

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        pip install feedparser gitpython

    - name: Run script
      run: python scripts/update_blog.py
</code></pre><ul>
<li>매일 자정 또는 해당 레포지토리가 push 될 때 파이썬 스크립트를 실행하는 코드이다.</li>
</ul>
<h2 id="3-파이썬-스크립트-작성">3. 파이썬 스크립트 작성</h2>
<ul>
<li><code>update_blog.py</code><pre><code>import feedparser
import git
import os
</code></pre></li>
</ul>
<h1 id="벨로그-rss-피드-url">벨로그 RSS 피드 URL</h1>
<h1 id="example--rss_url--httpsapivelogiorssrimgosu">example : rss_url = '<a href="https://api.velog.io/rss/@rimgosu'">https://api.velog.io/rss/@rimgosu'</a></h1>
<p>rss_url = '<a href="https://api.velog.io/rss/@%5B%EB%B2%A8%EB%A1%9C%EA%B7%B8">https://api.velog.io/rss/@[벨로그</a> 아이다]'</p>
<h1 id="깃허브-레포지토리-경로">깃허브 레포지토리 경로</h1>
<p>repo_path = '.'</p>
<h1 id="velog-posts-폴더-경로">'velog-posts' 폴더 경로</h1>
<p>posts_dir = os.path.join(repo_path, 'velog-posts')</p>
<h1 id="velog-posts-폴더가-없다면-생성">'velog-posts' 폴더가 없다면 생성</h1>
<p>if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)</p>
<h1 id="레포지토리-로드">레포지토리 로드</h1>
<p>repo = git.Repo(repo_path)</p>
<h1 id="rss-피드-파싱">RSS 피드 파싱</h1>
<p>feed = feedparser.parse(rss_url)</p>
<h1 id="각-글을-파일로-저장하고-커밋">각 글을 파일로 저장하고 커밋</h1>
<p>for entry in feed.entries:
    # 파일 이름에서 유효하지 않은 문자 제거 또는 대체
    file_name = entry.title
    file_name = file_name.replace('/', '-')  # 슬래시를 대시로 대체
    file_name = file_name.replace('\', '-')  # 백슬래시를 대시로 대체
    # 필요에 따라 추가 문자 대체
    file_name += '.md'
    file_path = os.path.join(posts_dir, file_name)</p>
<pre><code># 파일이 이미 존재하지 않으면 생성
if not os.path.exists(file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(entry.description)  # 글 내용을 파일에 작성

    # 깃허브 커밋
    repo.git.add(file_path)
    repo.git.commit('-m', f'Add post: {entry.title}')</code></pre><h1 id="변경-사항을-깃허브에-푸시">변경 사항을 깃허브에 푸시</h1>
<p>repo.git.push()</p>
<pre><code>

## 4. PAT 권한 받기
1. github 계정 - Settings - Developer Settings - Personal access tokens (classic) - Generate New Token - 이름 쓰고 repo, workflow 클릭 - Generate new token
2. 받은 토큰 복사 (한 번 보여주고 그 뒤로 보여주지 않으므로 꼭 복사해놓자)
3. 위에서 생성한 레포지토리 - Settings - Actions secrets and variables - Actions - New Repository Secret
4. Name : GH_PAT, Secret : [2번에서 발급받은 토큰]


## 5. 커밋 또는 자정까지 기다리기
- 레포지토리에 push를 진행하면 다음과 같이 `velog-posts` 폴더에 자동으로 .md 파일로 저장되는 것을 볼 수 있다.</code></pre>