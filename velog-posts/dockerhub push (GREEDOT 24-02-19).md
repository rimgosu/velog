<h2 id="✔️-todo">✔️ TODO</h2>
<ol>
<li>감정 분석 백엔드 작업(DB와 연동) ✅</li>
</ol>
<h2 id="✔️-dockerhub-push">✔️ dockerhub push</h2>
<h3 id="1-dockerhub-login">1. dockerhub login</h3>
<pre><code>sudo docker login</code></pre><h3 id="2-docker-tag">2. docker tag</h3>
<pre><code>docker tag local-image:tag username/repository:tag</code></pre><ul>
<li>example<pre><code>docker tag my-image newnyup319/greedot-ai:latest</code></pre></li>
</ul>
<h3 id="3-docker-push">3. docker push</h3>
<pre><code>docker push username/repository:tag</code></pre><ul>
<li>example<pre><code>docker push newnyup319/greedot-ai:latest</code></pre></li>
</ul>