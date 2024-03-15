<h2 id="✏️-git-pull-request-flow">✏️ git pull request flow</h2>
<h3 id="1-git-fetch-origin">1. git fetch origin</h3>
<ul>
<li>원격 저장소에서 <em>커밋 이력</em>만 가져온다.</li>
</ul>
<pre><code class="language-bash">$ git fetch origin
...
[새로운 브랜치] REFACTORING-017 -&gt; origin/REFACTORING-017
[새로운 브랜치] REFACTORING-018 -&gt; origin/REFACTORING-018</code></pre>
<h3 id="2-git-checkout--b-로컬브랜치-원격브랜치">2. git checkout -b [로컬브랜치] [원격브랜치]</h3>
<ul>
<li>로컬에서 REFACTORING-017로 체크아웃하되, 원격의 origin/REFACTORING-017 내용과 동기화</li>
</ul>
<pre><code class="language-bash">(dev) $ git checkout -b REFACTORING-017 origin/REFACTORING-017
(REFACTORING-017) $</code></pre>
<ol>
<li>작업이 완료된 후 github에서 pull request를 승인한다.</li>
<li>로컬에서 dev 브랜치로 체크아웃 한다.</li>
<li>git fetch origin으로 pull request 이력을 가지고온다.</li>
</ol>
<pre><code class="language-bash">$ git fetch origin
...
dev -&gt; origin/dev</code></pre>
<h3 id="3-git-rebase-origindev">3. git rebase origin/dev</h3>
<ol>
<li>현재 브랜치에서 <strong><code>origin/dev</code></strong> 브랜치까지의 모든 변경 사항(커밋)을 임시로 제거한다.</li>
<li><strong><code>origin/dev</code></strong> 브랜치의 최신 변경 사항을 현재 브랜치로 가져온다.</li>
</ol>
<pre><code class="language-bash">$ git rebase origin/dev
Successfully rebase origin/dev</code></pre>
<h3 id="4-git-log---graph---oneline---all">4. git log --graph --oneline --all</h3>
<ul>
<li>다음 명령어를 통해 원격 브랜치와 병합 여부를 한번에 파악할 수 있다.</li>
</ul>
<h3 id="5-git-branch--r-merged-dev">5. git branch -r —merged dev</h3>
<ul>
<li>현재 브랜치(dev)와 원격의 브랜치가 병합이 되었는지 확인할 수 있는 명령어</li>
</ul>
<pre><code class="language-bash">(dev) $ git branch -r --merged dev
...
REFACTORING-017</code></pre>
<ul>
<li>반대로 병합 안 된 브랜치도 확인 가능하다.</li>
</ul>
<pre><code class="language-bash">(dev) $ git branch -r --no-merged dev
origin/main</code></pre>