<h2 id="1-overview">1. overview</h2>
<ul>
<li><a href="https://github.com/rimgosu/git-synchronize">https://github.com/rimgosu/git-synchronize</a><pre><code>┬ allclone.py 
└ runallclone.bat</code></pre></li>
</ul>
<h3 id="사전-준비물">사전 준비물</h3>
<ul>
<li>python 3.10 버전</li>
<li>git</li>
<li>windows 10 이상</li>
</ul>
<h2 id="2-python-라이브러리-설치">2. python 라이브러리 설치</h2>
<ul>
<li>GitPython의 설치가 필요하다.<pre><code>pip install requests GitPython</code></pre></li>
</ul>
<h2 id="3-파이썬-코드-작성">3. 파이썬 코드 작성</h2>
<ul>
<li><code>allclone.py</code></li>
</ul>
<pre><code>import requests
from git import Repo, GitCommandError
import os
from datetime import datetime

def get_user_repos(username, token):
    try:
        headers = {&quot;Authorization&quot;: f&quot;Bearer {token}&quot;}
        response = requests.get(f&quot;https://api.github.com/search/repositories?q=user:{username}&quot;, headers=headers)
        response.raise_for_status()
        repos = response.json()[&quot;items&quot;]
        return [repo['name'] for repo in repos]
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

def get_default_branch(username, repo, token):
    headers = {&quot;Authorization&quot;: f&quot;Bearer {token}&quot;}
    response = requests.get(f&quot;https://api.github.com/repos/{username}/{repo}&quot;, headers=headers)
    response.raise_for_status()
    repo_data = response.json()
    return repo_data['default_branch']

def clone_or_update_repo(username, repo, token):
    if os.path.isdir(repo):
        try:
            print(f&quot;Checking {repo}...&quot;)
            git_repo = Repo(repo)

            default_branch = get_default_branch(username, repo, token)

            if 'origin' not in git_repo.remotes:
                git_repo.create_remote('origin', url=f'https://github.com/{username}/{repo}.git')

            git_repo.git.pull('origin', default_branch)
            git_repo.git.add(A=True)
            git_repo.git.commit('-m', datetime.now().strftime(&quot;Update on %Y-%m-%d %H:%M:%S&quot;))
            git_repo.git.push('origin', default_branch)
        except GitCommandError as e:
            print(f&quot;Error updating {repo}: {e}&quot;)
    else:
        try:
            print(f&quot;Cloning {repo}...&quot;)
            Repo.clone_from(
                f&quot;https://x-access-token:{token}@github.com/{username}/{repo}.git&quot;,
                repo
            )
        except GitCommandError as e:
            print(f&quot;Error cloning {repo}: {e}&quot;)

token = os.environ.get('GITHUB_TOKEN')
username = &quot;[깃허브 사용자 닉네임 입력]&quot;
# ex ) username = &quot;rimgosu&quot;
repos = get_user_repos(username, token)
print(f&quot;{username}의 레포지토리 목록: {repos}&quot;)

for repo in repos:
    clone_or_update_repo(username, repo, token)</code></pre><ul>
<li>아래 username을 자기의 깃허브 닉네임으로 바꿔넣자.</li>
<li>private 상태의 레포지토리도 검색하여 모든 레포지토리의 이름을 담아둔다.</li>
<li>만약 해당 레포지토리의 폴더가 없으면 clone을, 해당 레포지토리의 폴더가 있으면 다음 명령어를 실행한다.</li>
</ul>
<pre><code class="language-bash">git pull origin [main/master]
git add .
git commit -m &quot;$(date)&quot;
git push origin master</code></pre>
<h2 id="4-배치파일-작성">4. 배치파일 작성</h2>
<ul>
<li><p><code>runallclone.bat</code></p>
<pre><code>python [경로를 입력하세요]/allclone.py
pause</code></pre></li>
<li><p>만약 실행된 내역을 보고싶지 않다면 pause를 삭제할 것.</p>
</li>
</ul>
<h2 id="5-github-pat-token-받기">5. github PAT token 받기</h2>
<ol>
<li>github 계정 - Settings - Developer Settings - Personal access tokens (classic) - Generate New Token - 이름 쓰고 repo, workflow 클릭 - Generate new token</li>
<li>받은 토큰 복사 (한 번 보여주고 그 뒤로 보여주지 않으므로 꼭 복사해놓자)</li>
</ol>
<h2 id="6-윈도우-환경변수-설정">6. 윈도우 환경변수 설정</h2>
<ul>
<li><code>cmd</code><pre><code>setx GITHUB_TOKEN &quot;[5번에서_발급받은_토큰_입력]&quot;</code></pre></li>
<li><strong>다시시작</strong> 해야 깃허브 토큰이 제대로 환경 변수로 등록된다.</li>
</ul>
<h2 id="7-배치파일-직접-실행-or-작업-스케쥴러">7. 배치파일 직접 실행 or 작업 스케쥴러</h2>
<ul>
<li><code>runallclone.bat</code>을 더블 클릭하여 실행하면 파이썬 스크립트가 실행되어 모든 깃허브 레포지토리가 동기화 된다.</li>
<li>만약 xx분 마다 깃허브와 로컬의 저장소를 동기화시키고 싶다면 작업 스케쥴러를 사용하자. </li>
<li>리눅스는 crontab 쓰면 되니 더 간단하게 될 것이다. bat 파일을 sh로 바꾸고 실행해보자.</li>
<li><code>검색 - 작업 스케쥴러</code> 실행 후 다음과 같이 설정하자.</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/b4dd2802-5e58-4532-92ec-cb049f6f0fea/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/1282b99f-ebde-4c81-b0e0-6efc61b08fd6/image.png" /></p>
<ul>
<li><p>트리거
<img alt="" src="https://velog.velcdn.com/images/rimgosu/post/9a628f18-e723-4260-aad9-32c712262687/image.png" /></p>
</li>
<li><p>동작 </p>
<ul>
<li><strong>시작위치, 배치파일 위치 나눠서 작성한다.</strong></li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/2882834b-e9bf-4f34-8b1f-d3faca41c256/image.png" /></p>
<ul>
<li>조건</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/b8fded2b-1193-4169-8cd6-a5b27b205be9/image.png" /></p>
<ul>
<li>설정</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/05ef3723-a227-495c-8b8c-ba240b0fd500/image.png" /></p>
<ul>
<li><strong>다시 시작</strong>하거나 만든 스케쥴러를 선택 - <code>실행</code> 버튼을 누르면 자동으로 원격 저장소와 sync를 맞추게 된다.</li>
</ul>
<h2 id="8-동작-확인">8. 동작 확인</h2>
<ul>
<li>다음과 같이 일정 시간마다 내 모든 깃허브 레포지토리와 동기화 하는 것을 볼 수 있다.</li>
<li>나는 <code>c:/gits</code> 폴더를 기본 동기화 장소로 사용하고, 원하는 레포지토리의 바로가기를 만들어 사용할 예정이다. </li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/8b9900a4-181a-4dfd-8603-e17530019e3d/image.png" /></p>