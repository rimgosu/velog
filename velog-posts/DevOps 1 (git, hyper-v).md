<h1 id="설정">설정</h1>
<ul>
<li>검색 -&gt; Windows 기능 켜기/끄기 -&gt; Hyper-V 켜기 (windows pro 버전이어야함)
<img alt="" src="https://velog.velcdn.com/images/rimgosu/post/01c44d08-7d24-4040-bf09-913bf02b550b/image.png" /><ul>
<li>이럼 virtual box 설치 안해도 윈도우 자체제공 하이퍼바이저로 리눅스 환경 접속할 수 있다.</li>
</ul>
</li>
</ul>
<h2 id="devops란">DevOps란</h2>
<ul>
<li>DevOps는 애플리케이션과 서비스를 빠른 속도로 제공할 수 있도록 조직의 역량을 향상시키는 문화 철학, 방식 및 도구의 조합</li>
<li>단순히 말해, 개발과 운영의 조합</li>
</ul>
<h2 id="azure-아키텍쳐-아이콘-다운로드">Azure 아키텍쳐 아이콘 다운로드</h2>
<ul>
<li><a href="https://learn.microsoft.com/ko-kr/azure/architecture/icons/">https://learn.microsoft.com/ko-kr/azure/architecture/icons/</a></li>
</ul>
<h2 id="git">git</h2>
<ul>
<li><p>협업 시 윈도우와 맥에서 엔터 방식 차이로 인한 오류를 방지한다.</p>
<pre><code>git config --global core.autocrlf true</code></pre></li>
<li><p>맥이나 리눅스는 input으로 설정.</p>
<pre><code>git config --global core.autocrlf input</code></pre></li>
</ul>
<h3 id="sourcetree">Sourcetree</h3>
<ul>
<li><a href="https://blog.sourcetreeapp.com/2018/04/24/sourcetree-for-windows-enterprise-now-available/">https://blog.sourcetreeapp.com/2018/04/24/sourcetree-for-windows-enterprise-now-available/</a></li>
<li><a href="https://www.sourcetreeapp.com/">https://www.sourcetreeapp.com/</a></li>
<li>비트버킷 x , mercurial x -&gt; 설치, ssh 키 x<ul>
<li>git을 gui로 쉽게 볼 수 있는 툴이다.</li>
</ul>
</li>
</ul>
<h2 id="vs-code">vs code</h2>
<ul>
<li>Extension : Material Icon Theme </li>
</ul>
<h2 id="wsl">wsl</h2>
<ul>
<li>hyper-V가 아니라, 리눅스 커널이 윈도우에 탑재되어있는 것을 wsl이라 한다.</li>
</ul>
<ol>
<li>microsoft store - ubuntu 22.04 - 다운로드 및 설치</li>
<li>vs code - extension - wsl 설치 후 터미널에서 사용</li>
</ol>
<h1 id="git-1">git</h1>
<ul>
<li><a href="https://github.com/git/git">https://github.com/git/git</a><h2 id="초기설정">초기설정</h2>
</li>
<li>이름, 이메일 지정<pre><code>git config --global user.name &quot;rimgosu&quot;
git config --global user.email &quot;newnyup@gmail.com&quot;</code></pre></li>
<li>에디터 vs 코드로 바꾸기<pre><code>git config --global core.editor &quot;code --wait&quot;</code></pre></li>
<li>메인 브랜치로 변경(기존 master)<pre><code>git config --global init.defaultBranch main</code></pre></li>
</ul>
<h2 id="설정-확인">설정 확인</h2>
<pre><code>git config --global --list</code></pre><h2 id="gitignore">.gitignore</h2>
<ul>
<li><a href="https://git-scm.com/docs/gitignore">https://git-scm.com/docs/gitignore</a></li>
</ul>
<h2 id="초기화">초기화</h2>
<ul>
<li><p>git reset</p>
<ul>
<li>git log로 원하는 지점의 hash 값 받은 후 초기화<pre><code>git reset --hard 461772c99d930499eb6c8b6d9b0d60206a0d5c28</code></pre></li>
</ul>
</li>
<li><p>sourcetree reset</p>
<ul>
<li>이 커밋까지 현재 브랜치를 초기화 버튼</li>
</ul>
</li>
</ul>
<ul>
<li>git revert<ul>
<li>작업내역 남기면서 초기화 가능<pre><code>git revert 8abc2b8d2ddcf162a9b51d1892d171432c234feb</code></pre></li>
</ul>
</li>
</ul>
<h2 id="병합">병합</h2>
<ul>
<li>git merge<ul>
<li>합치고 기록이 남음 (추천)</li>
</ul>
</li>
<li>git rebase<ul>
<li>합치고 기록 안남음</li>
</ul>
</li>
</ul>
<h1 id="ubuntu">ubuntu</h1>
<ul>
<li>hyper-v -&gt; 빨리만들기 -&gt; ubuntu 22.04 lts 설치 <strong>👍추천</strong><ul>
<li>disk 12GB로 작게 설정되어있으므로 추후 변경해야한다.</li>
</ul>
</li>
<li>hyper-v -&gt; 새로만들기 -&gt; ram : 4GB, disk : 60GB, 네트워크 : default switch<ul>
<li>trouble shooting : <a href="https://blog.naver.com/angelkim88/221630381266">https://blog.naver.com/angelkim88/221630381266</a></li>
<li>비밀번호 설정 안 될 때 보면 된다.</li>
</ul>
</li>
</ul>
<h2 id="하드디스크-용량-늘리기빨리-만들기-선택-시">하드디스크 용량 늘리기(빨리 만들기 선택 시)</h2>
<ul>
<li>자동 검사점(스냅샷) 제거 - 우클릭 - 검사점 삭제</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/4cf79ab6-510d-42e1-9cbc-0440be7be5ee/image.png" /></p>
<ul>
<li>하드디스크 편집 - 확장 - 60GB<ul>
<li>검사 : 최대 디스크 크기 : 60GB</li>
</ul>
</li>
</ul>
<h2 id="terminal-설정">terminal 설정</h2>
<ol>
<li>루트 비밀번호 설정</li>
</ol>
<ul>
<li>1234로 설정.<pre><code>sudo passwd</code></pre></li>
</ul>
<ol start="2">
<li><p>패키지매니저 업데이트</p>
<pre><code>sudo apt-get update</code></pre></li>
<li><p>vim 설치</p>
<pre><code>sudo apt-get install vim</code></pre></li>
<li><p>gparted 설치</p>
</li>
</ol>
<ul>
<li>트러블 슈팅 : <a href="https://wooriel.tistory.com/3">https://wooriel.tistory.com/3</a><pre><code>sudo apt-get upgrade
sudo apt-get update &amp;&amp; sudo apt-get install gparted </code></pre></li>
<li>ext4 저장소를 60GB로 설정</li>
<li>apply - fix</li>
</ul>
<ol start="5">
<li>git 설치<pre><code>$ sudo apt install git
$ git --version
git version 2.25.1</code></pre></li>
</ol>
<ul>
<li>버전 낮아서 업데이트 해줘야함.<pre><code>$ sudo add-apt-repository ppa:git-core/ppa -y
$ sudo apt-get update
$ sudo apt-get install git -y
git version 2.43.0</code></pre></li>
</ul>
<h2 id="✌️-복사붙여넣기-단축키-✌️">✌️ 복사붙여넣기 단축키 ✌️</h2>
<ul>
<li>ctrl + shift + c , ctrl + shift + v</li>
</ul>