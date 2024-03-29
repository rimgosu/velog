<h1 id="🚀-docker-images-to-tar">🚀 docker images to tar</h1>
<blockquote>
<p>인터넷 환경이 잘 구축되어 있기 때문에
docker image를 실제 파일로 만들 일은 잘 없다.
그저 잘 빌드해서 이미지로 만들고, dockerhub에 업로드 하면 되기 때문이다.</p>
<p>그러나 인터넷이 없는 환경이라면?
docker image를 실제 파일로 만들어 운용하는 방법에 대해 알아보자.</p>
</blockquote>
<h1 id="1-docker-image-➡️-tar-🚬">1. docker image ➡️ tar 🚬</h1>
<ul>
<li>다음과 같이 docker build나 docker compose up으로 이미지가 저장되어 있다고 생각해보자.<pre><code class="language-bash">☁  ~  docker images
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
test-api     latest    969809c19fe0   15 hours ago    470MB
mysql        8.0       c3ef21d6632d   2 days ago      603MB
nginx        latest    92b11f67642b   6 weeks ago     187MB
redis        7.0       ffc7b7efc8c1   2 months ago    130MB
mongo        4.2       9b5c4a4fdcb5   10 months ago   388MB</code></pre>
</li>
<li>이 이미지를 실제 존재하는 파일로 백업하고 싶다면?</li>
<li>docker save 명령어를 이용하도록 하자.</li>
</ul>
<pre><code class="language-bash">☁  backup  sudo docker save -o $(pwd)/test-api.tar test-api:latest
☁  backup  sudo docker save -o $(pwd)/mongo.tar mongo:4.2
☁  backup  sudo docker save -o $(pwd)/redis.tar redis:7.0
☁  backup  sudo docker save -o $(pwd)/mysql.tar mysql:8.0
☁  backup  ls
test-api.tar  mongo.tar  mysql.tar  redis.tar                                      </code></pre>
<ul>
<li>로컬에 존재하는 이미지를 전부 삭제하고 tar의 내용물을 확인해보자.<pre><code class="language-bash">☁  backup  sudo docker system prune -a --volumes
☁  backup  sudo docker images
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE</code></pre>
</li>
</ul>
<h1 id="2-tar-➡️-docker-image-💽">2. tar ➡️ docker image 💽</h1>
<ul>
<li>docker load 명령어를 통해 다시 이미지로 복원할 수 있다.<pre><code>☁  backup  sudo docker load -i test-api.tar &amp;&amp; sudo docker load -i mongo.tar &amp;&amp; sudo docker load -i mysql.tar &amp;&amp; sudo docker load -i redis.tar
548a79621a42: Loading layer [==================================================&gt;]  65.53MB/65.53MB
009afd448c57: Loading layer [==================================================&gt;]    405kB/405kB
  :
  :
  :
cc67fe8ba93c: Loading layer [==================================================&gt;]  4.096kB/4.096kB
Loaded image ID: sha256:ffc7b7efc8c16eeff6b2e6c99127b76035473c40d550d5b501557fe87db37b42
☁  backup  sudo docker images
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
test-api     latest    f0872a588a9f   5 minutes ago   470MB
mysql        8.0       c3ef21d6632d   2 days ago      603MB
redis        7.0       ffc7b7efc8c1   2 months ago    130MB
mongo        4.2       9b5c4a4fdcb5   10 months ago   388MB
☁  backup</code></pre></li>
</ul>