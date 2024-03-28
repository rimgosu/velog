<h1 id="🚀-docker-clean-script">🚀 docker clean script</h1>
<blockquote>
<p>docker compose를 사용하면 docker container를 일괄적으로 내리고,
이미지도 깨끗하게 정리해 용량을 확보해야 하는 경우가 생긴다.
다음 상황을 예시로 container를 일괄적으로 제거하는 방법에 대해 알아보겠다.</p>
</blockquote>
<pre><code>☁  back [main] sudo docker ps
CONTAINER ID   IMAGE                               COMMAND                  CREATED        STATUS              PORTS
                 NAMES
3aecc22a1fe2   main-api   &quot;docker-entrypoint.s…&quot;   45 hours ago   Up About a minute   0.0.0.0:3000-&gt;3000/tcp, :::3000-&gt;3000/tcp   main-api
12341d2d5c87   dev-api           &quot;docker-entrypoint.s…&quot;   45 hours ago   Up About a minute   0.0.0.0:3001-&gt;3001/tcp, :::3001-&gt;3001/tcp   dev-api
5678a492cbf0   redis:alpine                        &quot;docker-entrypoint.s…&quot;   45 hours ago   Up About a minute   0.0.0.0:6379-&gt;6379/tcp, :::6379-&gt;6379/tcp   dev-redis</code></pre><h1 id="1-일괄-중지제거-🗑️">1. 일괄 중지&amp;제거 🗑️</h1>
<pre><code>sudo docker stop $(sudo docker ps -aq)
sudo docker rm $(sudo docker ps -aq)</code></pre><ul>
<li>다음 두 명령어를 통해 일괄 중지 및 제거가 가능하다.</li>
<li>-a 옵션은 모든 컨테이너를 나타내고, -q 옵션은 컨테이너 이름만 나오도록 하는 것이다.</li>
</ul>
<pre><code>☁  back [main] sudo docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES</code></pre><ul>
<li><em>성공적으로 잘 제거되었다</em></li>
</ul>
<h1 id="2-volume-image-제거-💽">2. volume, image 제거 💽</h1>
<ul>
<li><p>docker volume 설정을 하게되면 다음과 같이 volume이 남게 되고,</p>
</li>
<li><p>이미지 또한 한꺼번에 제거하도록 하자.</p>
</li>
<li><p><em>현재 상황</em></p>
<pre><code>☁  back [main] sudo docker volume ls
DRIVER    VOLUME NAME
local     27f0c766444d47f06554625ffbece0ed74515b347903378aada987936b0319de
local     128b3462ce4062020410a10b75b7a2ebe93eb4ffc1c62acc40c5d2d2cc29cad5
local     5930d8df14c4f7a536ce087b75761c04378285aa70d9350de48d750bbc0a4359
local     d877d438aa37fd1fe0a4ad0bd225c6432d208864dbf17445345141d119ffb2dd
local     d998b074692b3b6d2c12d19c7d4fffd56130d314a618f68963d63ca97a742b37
☁  back [main] sudo docker images
REPOSITORY                          TAG       IMAGE ID       CREATED          SIZE
api                                    latest    f86ad15e4816   47 minutes ago   470MB
dev-api                                latest    42d6f28f3426   46 hours ago     625MB
virtual-dev-api                        latest    f0fd4b8c80f2   46 hours ago     2.06GB
&lt;none&gt;                              &lt;none&gt;    2f94418c2bcf   46 hours ago     625MB
&lt;none&gt;                              &lt;none&gt;    f52eb3729109   46 hours ago     2.06GB
&lt;none&gt;                              &lt;none&gt;    d76c783fce4a   2 days ago       625MB
&lt;none&gt;                              &lt;none&gt;    46f6ad2f4e23   2 days ago       2.06GB
&lt;none&gt;                              &lt;none&gt;    0b5e73f7efe6   6 days ago       625MB
&lt;none&gt;                              &lt;none&gt;    b92d891413ab   6 days ago       2.06GB
&lt;none&gt;                              &lt;none&gt;    592626f28ee0   6 days ago       625MB
&lt;none&gt;                              &lt;none&gt;    2d89c4e76e72   6 days ago       2.06GB
&lt;none&gt;                              &lt;none&gt;    20e5ff84b593   6 days ago       2.06GB
&lt;none&gt;                              &lt;none&gt;    8a3e606fab24   6 days ago       625MB
&lt;none&gt;                              &lt;none&gt;    7a7afd523341   6 days ago       625MB
&lt;none&gt;                              &lt;none&gt;    22e2af703e09   6 days ago       2.06GB
&lt;none&gt;                              &lt;none&gt;    639da70ab065   6 days ago       2.06GB
&lt;none&gt;                              &lt;none&gt;    1e84ef2aebda   6 days ago       625MB
mysql                               8.0       f309f7dabfd1   2 months ago     603MB
redis                               alpine    435993df2c8d   2 months ago     41MB
redis                               7.0       ffc7b7efc8c1   2 months ago     130MB
mongo                               4.2       9b5c4a4fdcb5   10 months ago    388MB
mysql/mysql-server                  latest    1d9c2219ff69   14 months ago    496MB</code></pre></li>
<li><p>docker system prune 명령어를 통해 전부 제거할 수 있다.</p>
<pre><code>sudo docker system prune -a --volumes</code></pre></li>
<li><p>system prune: 사용중이지 않은 이미지를 제거한다.</p>
</li>
<li><p>-a: 모든 이미지를 제거한다.</p>
</li>
<li><p>--volumes: 모든 사용 중이 아닌 볼륨도 함께 제거한다.</p>
</li>
</ul>
<h1 id="3-통합-스크립트">3. 통합 스크립트</h1>
<pre><code>sudo docker stop $(sudo docker ps -aq)
sudo docker rm $(sudo docker ps -aq)
sudo docker system prune -a --volumes</code></pre>