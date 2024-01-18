<h2 id="대표-소개">대표 소개</h2>
<ul>
<li>hello ai 대표 : <a href="https://helloai.kr/">https://helloai.kr/</a></li>
<li>김영욱 대표 링크드인 : <a href="https://kr.linkedin.com/in/%EC%98%81%EC%9A%B1-%EA%B9%80-315a4831">https://kr.linkedin.com/in/%EC%98%81%EC%9A%B1-%EA%B9%80-315a4831</a></li>
<li>강의 자료 공유(영욱닷컴) : <a href="https://blog.naver.com/warit">https://blog.naver.com/warit</a></li>
</ul>
<h1 id="azure">azure</h1>
<h2 id="1-기본-설정">1. 기본 설정</h2>
<ul>
<li><a href="http://portal.azure.com">http://portal.azure.com</a></li>
<li>id : <a href="mailto:labuser93@snuailab.onmicrosoft.com">labuser93@snuailab.onmicrosoft.com</a> </li>
<li>pw : !Seoul2025</li>
</ul>
<h2 id="2-데이터-센터">2. 데이터 센터</h2>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/747590fe-0a66-434d-8c45-38eda85ef9d5/image.png" /></p>
<ul>
<li>데이터 센터 위치 : <a href="https://datacenters.microsoft.com/globe/explore">https://datacenters.microsoft.com/globe/explore</a></li>
</ul>
<h2 id="3-azure-settings-✍️">3. azure settings ✍️</h2>
<ol>
<li>리소스 그룹 (작업 방 - 할당 : 93)
<img alt="" src="https://velog.velcdn.com/images/rimgosu/post/d03b38d7-12f3-4fd7-af8b-34d946e4ae7f/image.png" /></li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/b09836e9-a562-42c1-935f-87cacde26888/image.png" /></p>
<ol start="2">
<li><p>ubuntu 서버 만들기
<img alt="" src="https://velog.velcdn.com/images/rimgosu/post/29bdbde2-ce91-4d3c-83e6-ce791fbef69f/image.png" />
<img alt="" src="https://velog.velcdn.com/images/rimgosu/post/0c349c9a-4c9a-4766-97fd-54e680be349c/image.png" /></p>
</li>
<li><p>가상 머신 만들기
<img alt="" src="https://velog.velcdn.com/images/rimgosu/post/93f344f4-99ba-48ae-a433-aafc9e225862/image.png" /></p>
</li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/4bd57233-50f6-4437-b18f-53c364d19265/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/83308472-92fe-454a-bc7e-a73727baa4da/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/65864623-83d3-4873-a3e6-2bb0f8b9a3da/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/c4b0f4b7-7253-4b7a-970d-2ce01f442bbe/image.png" /></p>
<ol start="4">
<li>ssh로 연결
<img alt="" src="https://velog.velcdn.com/images/rimgosu/post/ef9f51f2-2475-47f8-99cf-90cce8e1207f/image.png" /></li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/e3b68a72-14e8-4deb-afb3-1b2fc643557d/image.png" /></p>
<pre><code>ssh -i ~/.ssh/id_rsa.pem winkey@20.200.217.203</code></pre><h2 id="4-linux-settings-👍">4. linux settings 👍</h2>
<ol>
<li>apt-get 업데이트<pre><code>sudo apt-get update
sudo apt-get upgrade</code></pre></li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/7de806f2-7696-44b7-8e2b-e508111712df/image.png" /></p>
<ul>
<li>tab - ok</li>
</ul>
<ol start="2">
<li>docker 설치 (아래 내용 참조)</li>
</ol>
<h1 id="컨테이너">컨테이너</h1>
<h2 id="1-서버-가상화">1. 서버 가상화</h2>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/0bcca659-4c88-4ac8-9736-b3364925f5d3/image.png" /></p>
<ul>
<li>Hosted Hypervisor Virtual Machine<ul>
<li>OS 위에 OS가 올라감으로 서버 부하가 많이 생긴다</li>
</ul>
</li>
<li>Container<ul>
<li>Host OS : 리눅스 OS</li>
<li>그 위에 Container가 올라가있고, Minimal Guest OS가 올라가는 형식이다. </li>
<li>기본 공유 자원 / 각각의 개별 자원으로 나눔. 버전을 기본적으로 각각 설정할 수 있으므로 똑같은 환경으로 배포가 가능하다는 장점이 있다.</li>
</ul>
</li>
</ul>
<h2 id="2-docker-vs-쿠버네티스">2. docker vs 쿠버네티스</h2>
<ul>
<li>도커 : 컨테이너 하나 관리<ul>
<li>소 한마리 애지중지 키우는 개념</li>
</ul>
</li>
<li>쿠버네티스 : 컨테이너 다수 관리<ul>
<li>미국에서 소 떼거지로 관리하는 개념</li>
</ul>
</li>
</ul>
<h2 id="3-docker">3. docker</h2>
<ul>
<li><a href="https://www.docker.com/">https://www.docker.com/</a></li>
<li>getting started : <a href="https://www.docker.com/get-started/">https://www.docker.com/get-started/</a></li>
<li>ubuntu docker 설치 : <a href="https://docs.docker.com/engine/install/ubuntu/">https://docs.docker.com/engine/install/ubuntu/</a></li>
</ul>
<h3 id="docker-repositories-👍">docker repositories 👍</h3>
<ul>
<li>다양한 네트워크의 레포지토리가 있다.</li>
</ul>
<ol>
<li>docker 공식 사이트 (library)</li>
</ol>
<ul>
<li><a href="https://docs.docker.com/registry">https://docs.docker.com/registry</a></li>
</ul>
<ol start="2">
<li>dockerhub</li>
</ol>
<ul>
<li><a href="https://hub.docker.com/">https://hub.docker.com/</a></li>
</ul>
<ol start="3">
<li>각 클라우드마다 docker 레포지토리 존재함. (Azure Container Registry)</li>
</ol>
<h3 id="docker-ubuntu-설치-✍️">docker ubuntu 설치 ✍️</h3>
<ul>
<li><a href="https://docs.docker.com/engine/install/ubuntu/#installation-methods">https://docs.docker.com/engine/install/ubuntu/#installation-methods</a></li>
</ul>
<ol>
<li>docker 설치 전 사전작업<pre><code># Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
</code></pre></li>
</ol>
<h1 id="add-the-repository-to-apt-sources">Add the repository to Apt sources:</h1>
<p>echo <br />  &quot;deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] <a href="https://download.docker.com/linux/ubuntu">https://download.docker.com/linux/ubuntu</a> <br />  $(. /etc/os-release &amp;&amp; echo &quot;$VERSION_CODENAME&quot;) stable&quot; | <br />  sudo tee /etc/apt/sources.list.d/docker.list &gt; /dev/null
sudo apt-get update</p>
<pre><code>
2. docker 설치
</code></pre><p>sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin</p>
<pre><code>
- 설정창 나오면 탭키 - ok


3. docker 테스트</code></pre><p>sudo docker run hello-world</p>
<pre><code>- 로컬에 있으면 실행
- 로컬에 없다면 인터넷에 있는 이미지를 찾아 다운로드하고, 실행시킴
- 기본적으로 도커 레포지토리에서 찾아 가져오고, 다른 레포지토리에서 다운로드도 가능하다.

4. ubuntu 18.04 다운로드</code></pre><p>$ sudo docker pull ubuntu:18.04</p>
<p>18.04: Pulling from library/ubuntu
7c457f213c76: Pull complete
Digest: sha256:152dc042452c496007f07ca9127571cb9c29697f42acbfad72324b2bb2e43c98
Status: Downloaded newer image for ubuntu:18.04
docker.io/library/ubuntu:18.04</p>
<pre><code>- ubuntu 원래 다운로드 받으려면 엄청 오래걸리는데, 현재 22.04 버전 위에서 동작하고 있으므로 스냅샷인 63MB만 받으면 된다. (효율적이군)

### docker 명령어 ✍️
1. **다운로드 받은** docker 이미지 확인</code></pre><p>$ sudo docker images
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
ubuntu        18.04     f9a80a55f492   7 months ago   63.2MB
hello-world   latest    d2c94e258dcb   8 months ago   13.3kB</p>
<pre><code>
2. **실행** 중인 docker 이미지 확인</code></pre><p>$ sudo docker ps</p>
<p>CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES</p>
<pre><code>
3. docker **실행 내역** 확인
</code></pre><p>$ sudo docker ps -a</p>
<p>CONTAINER ID   IMAGE         COMMAND    CREATED          STATUS                      PORTS     NAMES
31c0991209b4   hello-world   &quot;/hello&quot;   19 minutes ago   Exited (0) 19 minutes ago             zealous_cohen</p>
<pre><code>
4. docker 이미지 **실행**, ubuntu:18.04 실행
- -it : interactive 모드
   - 상호작용 가능한 모드로 ubuntu 18.04 환경에 진입할 수 있게 된다
- -name : 메모리에서 docker 이미지를 실행시킬 때 이름을 지정해줌
- /bin/bash : bash shell에서 실행</code></pre><p>$ sudo docker run -it --name demo1 ubuntu:18.04 /bin/bash</p>
<p>root@06d4ae567214:/# ls
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var</p>
<pre><code>
5. 이미지에서 **접속 종료**</code></pre><p>root@06d4ae567214:/etc# exit
exit
winkey@labuser93ubuntu:~$</p>
<pre><code>

6. docker를 **계속 실행**
- -d : daemon</code></pre><p>$ sudo docker run -it -d --name demo2 ubuntu:18.04
2e5aeafde515f253ae5653528951caededd5733d2874104afe49a4e2ecd7514f</p>
<p>$ sudo docker ps
CONTAINER ID   IMAGE          COMMAND       CREATED          STATUS          PORTS     NAMES
2e5aeafde515   ubuntu:18.04   &quot;/bin/bash&quot;   13 seconds ago   Up 12 seconds
demo2</p>
<pre><code>- container id를 할당받고, 백그라운드에서 계속 실행되고 있는 상태가 됨


7. **메모리에 올라와** 있는 docker 실행
- exec 명령어로 실행시킬 수 있다.</code></pre><p>$ sudo docker exec -it demo2 /bin/bash
root@2e5aeafde515:/#</p>
<pre><code>
8. busybox 실행 (docker 테스트 이미지) 및 **로그** 보기</code></pre><p>$ sudo docker run --name demo5 -d busybox sh -c &quot;while true;do
$(echo date);sleep 1; done&quot;</p>
<p>a3083ce2f910269d1e2fdcf718c6cf6e055fb9485c9b22d05240918b1894c799</p>
<pre><code>
- 로그 확인</code></pre><p>$ sudo docker logs demo5</p>
<p>Thu Jan 11 03:27:26 UTC 2024
Thu Jan 11 03:27:28 UTC 2024
Thu Jan 11 03:27:29 UTC 2024
Thu Jan 11 03:27:30 UTC 2024
Thu Jan 11 03:27:31 UTC 2024
Thu Jan 11 03:27:32 UTC 2024</p>
<pre><code>
- 실시간 로그 확인</code></pre><p>$ sudo docker logs demo5 -f</p>
<p>Thu Jan 11 03:27:26 UTC 2024
Thu Jan 11 03:27:28 UTC 2024
Thu Jan 11 03:27:29 UTC 2024
Thu Jan 11 03:27:30 UTC 2024
Thu Jan 11 03:27:31 UTC 2024
Thu Jan 11 03:27:32 UTC 2024
... 계속 반복</p>
<pre><code>
8. 메모리에서 실행중인 도커 이미지 **실행 중단**
- docker stop</code></pre><p>$ sudo docker ps
CONTAINER ID   IMAGE          COMMAND                  CREATED             STATUS             PORTS     NAMES
a3083ce2f910   busybox        &quot;sh -c 'while true;d…&quot;   About an hour ago   Up About an hour             demo5
2e5aeafde515   ubuntu:18.04   &quot;/bin/bash&quot;              About an hour ago   Up About an hour             demo2</p>
<p>$ sudo docker stop demo5
demo5</p>
<p>$ sudo docker ps
CONTAINER ID   IMAGE          COMMAND       CREATED             STATUS             PORTS     NAMES
2e5aeafde515   ubuntu:18.04   &quot;/bin/bash&quot;   About an hour ago   Up About an hour             demo2</p>
<pre><code>
9. 메모리에 적재된 도커 이미지 **삭제**
- docker rm</code></pre><p>$ sudo docker ps -a
CONTAINER ID   IMAGE          COMMAND                  CREATED             STATUS                          PORTS     NAMES
a3083ce2f910   busybox        &quot;sh -c 'while true;d…&quot;   About an hour ago   Exited (137) 2 minutes ago                demo5
71c788454ee6   busybox        &quot;sh -c 'while true;d…&quot;   About an hour ago   Exited (2) About an hour ago              demo3
2e5aeafde515   ubuntu:18.04   &quot;/bin/bash&quot;              About an hour ago   Exited (0) About a minute ago             demo2
06d4ae567214   ubuntu:18.04   &quot;/bin/bash&quot;              2 hours ago         Exited (0) 2 hours ago                    demo1
31c0991209b4   hello-world    &quot;/hello&quot;                 2 hours ago         Exited (0) 2 hours ago                    zealous_cohen</p>
<p>$ sudo docker rm demo1 
demo1</p>
<p>$ sudo docker ps -a
CONTAINER ID   IMAGE          COMMAND                  CREATED             STATUS                         PORTS     NAMES
a3083ce2f910   busybox        &quot;sh -c 'while true;d…&quot;   About an hour ago   Exited (137) 4 minutes ago               demo5
71c788454ee6   busybox        &quot;sh -c 'while true;d…&quot;   About an hour ago   Exited (2) About an hour ago             demo3
2e5aeafde515   ubuntu:18.04   &quot;/bin/bash&quot;              2 hours ago         Exited (0) 3 minutes ago                 demo2
31c0991209b4   hello-world    &quot;/hello&quot;                 2 hours ago         Exited (0) 2 hours ago                   zealous_cohen</p>
<pre><code>

10. 하드디스크에 존재하는 도커 이미지 삭제
- docker rmi
</code></pre><p>$ sudo docker images
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
busybox       latest    9211bbaa0dbd   3 weeks ago    4.26MB
ubuntu        18.04     f9a80a55f492   7 months ago   63.2MB
hello-world   latest    d2c94e258dcb   8 months ago   13.3kB</p>
<p>$ sudo docker rmi busybox
Untagged: busybox:latest
Untagged: busybox@sha256:ba76950ac9eaa407512c9d859cea48114eeff8a6f12ebaa5d32ce79d4a017dd8
Deleted: sha256:9211bbaa0dbd68fed073065eb9f0a6ed00a75090a9235eca2554c62d1e75c58f
Deleted: sha256:82ae998286b2bba64ce571578647adcabef93d53867748d6046cc844ff193a83</p>
<p>$ sudo docker images
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
ubuntu        18.04     f9a80a55f492   7 months ago   63.2MB
hello-world   latest    d2c94e258dcb   8 months ago   13.3kB</p>
<pre><code>
- ubuntu 삭제 : 특정 버전으로 정했으면 이미지의 이름과 버전을 같이 명시해줘야 삭제가 가능하다</code></pre><p>$ sudo docker rmi ubuntu:18.04
Untagged: ubuntu:18.04
Untagged: ubuntu@sha256:152dc042452c496007f07ca9127571cb9c29697f42acbfad72324b2bb2e43c98
Deleted: sha256:f9a80a55f492e823bf5d51f1bd5f87ea3eed1cb31788686aa99a2fb61a27af6a
Deleted: sha256:548a79621a426b4eb077c926eabac5a8620c454fb230640253e1b44dc7dd7562</p>
<pre><code>


### Dockerfile 명령어 ✍️

- Dockerfile 생성</code></pre><p>touch Dockerfile</p>
<pre><code>
#### FROM
- Dockerfile 이 base image로 어떤 이미지를 사용할 것인지를 명시하는 명령어입니다.</code></pre><p>FROM [:] [AS ]</p>
<h1 id="예시">예시</h1>
<p>FROM ubuntu
FROM ubuntu:18.04
FROM ngix:latest AS ngx</p>
<pre><code>

#### COPY
- `&lt;src&gt;`의 파일 혹은 디렉토리를 `&lt;dest&gt;` 경로에 복사하는 명령어입니다.
</code></pre><p>COPY ... </p>
<h1 id="예시-1">예시</h1>
<p>COPY a.txt /some-directory/b.txt
COPY my-directory /some-directory-2</p>
<pre><code>

#### RUN
- 명시한 커맨드를 도커 컨테이너에서 실행하는 것을 명시하는 명령어입니다.</code></pre><p>RUN <command />
RUN [&quot;excutable-command&quot;, 'parameter1', 'parameter2']</p>
<h1 id="예시-2">예시</h1>
<p>RUN pip install torch
RUN pip install -r requirements.txt</p>
<pre><code>
#### CMD
- 명시한 커맨드를 도커 컨테이너가 시작될 때, 실행하는 것을 명시하는 명령어입니다.
   - vs RUN : 도커가 처음 실행될 때(설정) 실행된다
   - 반면 CMD는 docker가 run 될 때 마다 실행됨
   - 하나의 docker 이미지는 하나의 CMD만 실행할 수 있다
</code></pre><p>CMD <command /> 
CMD [&quot;executable-command&quot;, &quot;parameter1&quot;, &quot;parameter2&quot;] 
CMD [&quot;parameter1&quot;, &quot;parameter2&quot;] # ENTRYPOINT 와 함께 사용될 때 </p>
<h1 id="예시-3">예시</h1>
<p>CMD python main.py 
CMD </p>
<pre><code>

#### WORKDIR
- 이후 작성될 명령어를 컨테이너 내의 어떤 디렉토리에서 수행할 것인지를 명시하는 명령어입니다.
- 해당 디렉토리가 없다면 생성합니다.</code></pre><p>WORKDIR /path/to/workdir </p>
<h1 id="예시-4">예시</h1>
<p>WORKDIR /home/demo</p>
<pre><code>

#### ENV
- 컨테이너 내부에서 지속적으로 사용될 environment variable의 값을 설정하는 명령어입니다.
</code></pre><p>ENV   
ENV = </p>
<h1 id="예시-5">예시</h1>
<h1 id="default-언어-설정">default 언어 설정</h1>
<p>RUN locale-gen ko_KR.UTF-8 
ENV LANG ko_KR.UTF-8 
ENV LANGUAGE ko_KR.UTF-8 
ENV LC_ALL ko_KR.UTF-8</p>
<pre><code>

#### EXPOSE
- 컨테이너에서 뚫어줄 포트/프로토콜을 지정할 수 있습니다.
- protocol을 지정하지 않으면 TCP가 디폴트로 설정됩니다.
</code></pre><p>EXPOSE  
EXPOSE / </p>
<h1 id="예시-6">예시</h1>
<p>EXPOSE 8080</p>
<pre><code>


### Dockerfile 실습 ✍️
1. Dockerfile 만들기</code></pre><p>vi Dockerfile</p>
<pre><code></code></pre><p>FROM ubuntu:18.04</p>
<p>RUN apt-get update</p>
<p>CMD [&quot;echo&quot;, &quot;Hello Docker&quot;]</p>
<pre><code>
2. 내가 만든 Dockerfile ** 빌드**</code></pre><p>sudo docker build -t my-image:v1.0.0 .</p>
<pre><code>
3. docker 실행</code></pre><p>sudo docker run my-image:v1.0.0</p>
<pre><code>
#### docker registry로 push
1. **docker registry** 실행
- 도커의 이미지를 관리하기 위한 도커 이미지를 설치하여 실행
- 5000번</code></pre><p>sudo docker run -d -p 5000:5000 --name registry registry</p>
<pre><code>
2. my-image를 방금 생성한 registry를 바라보도록 **tag**
- tag 명령어를 통해 repository를 어디에 연결할 지 결정할 수 있다.
- **링크된 것**, git remote origin add와 비슷하다.</code></pre><p>$ sudo docker tag my-image:v1.0.0 localhost:5000/my-image:v1.0.0</p>
<p>$ sudo docker images
REPOSITORY                TAG       IMAGE ID       CREATED          SIZE
my-image                  v1.0.0    bf450d7aa616   23 minutes ago   109MB
localhost:5000/my-image   v1.0.0    bf450d7aa616   23 minutes ago   109MB
registry                  latest    909c3ff012b7   5 weeks ago      25.4MB</p>
<pre><code>
3. my-image를 registry에 **push**</code></pre><p>$ sudo docker push localhost:5000/my-image:v1.0.0
The push refers to repository [localhost:5000/my-image]
b5858e8710d9: Pushed
548a79621a42: Pushed
v1.0.0: digest: sha256:16982bd2cd1153fe0a9b875396f3881862b6a6c77e6f788b5b5d7575b345dff8 size: 741</p>
<pre><code>

#### dockerhub로 push
- &lt;https://hub.docker.com/&gt;

1. docker login으로 dockerhub에 로그인</code></pre><p>$ sudo docker login
Log in with your Docker ID or email address to push and pull images from Docker Hub. If you don't have a Docker ID, head over to <a href="https://hub.docker.com/">https://hub.docker.com/</a> to create one.
You can log in with your password or a Personal Access Token (PAT). Using a limited-scope PAT grants better security and is required for organizations using SSO. Learn more at <a href="https://docs.docker.com/go/access-tokens/">https://docs.docker.com/go/access-tokens/</a></p>
<p>Username: newnyup319
Password:
WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
Configure a credential helper to remove this warning. See
<a href="https://docs.docker.com/engine/reference/commandline/login/#credentials-store">https://docs.docker.com/engine/reference/commandline/login/#credentials-store</a></p>
<p>Login Succeeded</p>
<pre><code>
2. dockerhub로 **tag**
</code></pre><p>sudo docker tag my-image:v1.0.0 newnyup319/my-image:v1.0.0</p>
<pre><code></code></pre><p>$ sudo docker images
REPOSITORY                TAG       IMAGE ID       CREATED          SIZE
my-image                  v1.0.0    bf450d7aa616   43 minutes ago   109MB
newnyup319/my-image       v1.0.0    bf450d7aa616   43 minutes ago   109MB
localhost:5000/my-image   v1.0.0    bf450d7aa616   43 minutes ago   109MB
registry                  latest    909c3ff012b7   5 weeks ago      25.4MB</p>
<pre><code>
3. dockerhub로 **push**
</code></pre><p>$ sudo docker push newnyup319/my-image:v1.0.0
The push refers to repository [docker.io/newnyup319/my-image]
b5858e8710d9: Pushed
548a79621a42: Mounted from library/ubuntu
v1.0.0: digest: sha256:9e9bddec89c0b29a3fc8ac560f52cc3aa47ffedb7d03ad550c4215a555fec1a7 size: 741</p>
<pre><code>
![](https://velog.velcdn.com/images/rimgosu/post/5e1aac44-8e23-4be1-b65d-1f2468b625d4/image.png)

- 성공적으로 이미지 업로드 된 것을 확인할 수 있다.




# azure cv cat vs dog ✅

![](https://velog.velcdn.com/images/rimgosu/post/d281163f-e8ff-44a3-818b-73cfc7c22682/image.png)


## 1. azure에서 computer vision 생성
- azure portal - 리소스 그룹 - RG93 - 만들기 - computer vision

![](https://velog.velcdn.com/images/rimgosu/post/19a30e7b-499f-47b1-83be-0e360f3e5704/image.png)


![](https://velog.velcdn.com/images/rimgosu/post/9034f910-d7f6-40ff-9d10-bdf241b6f021/image.png)

- 만들고, 키 및 엔드포인트 - 키와 주소 복사하고 colab

![](https://velog.velcdn.com/images/rimgosu/post/cdce0e8d-8d55-4151-841d-31dde4d6997a/image.png)

![](https://velog.velcdn.com/images/rimgosu/post/03b2b0b8-09d2-4511-a5ea-4b146b9093d1/image.png)


## 2. 이미지 분석 - colab
### 이미지 불러오기</code></pre><p>image_url = '<a href="https://cdn.huffingtonpost.kr/news/photo/201602/22260_43420.jpeg'">https://cdn.huffingtonpost.kr/news/photo/201602/22260_43420.jpeg'</a></p>
<p>from PIL import Image
from io import BytesIO
import requests</p>
<p>Image.open(BytesIO(requests.get(image_url).content))</p>
<pre><code>

### key, endpoint 연결</code></pre><p>key = '[key를 입력하세요]'
endpoint = '<a href="https://labuser93computervision.cognitiveservices.azure.com/'">https://labuser93computervision.cognitiveservices.azure.com/'</a>
endpoint = endpoint + 'vision/v2.0/'</p>
<p>analyze_endpoint = endpoint + 'analyze' # 분석
detect_endpoint = endpoint + 'detect' # 객체 탐지
ocr_endpoint = endpoint + 'ocr' # 글자 인식</p>
<p>headers = {'Ocp-Apim-Subscription-Key': key}
params = {'visualFeatures': 'Categories,Description,Color'}
data = {'url': image_url}</p>
<pre><code>
### analyze (태그 달아주기)</code></pre><p>response = requests.post(analyze_endpoint,
                         headers=headers,
                         params=params,
                         json=data)
result = response.json()
result['description'] </p>
<pre><code>
#### analyze 결과</code></pre><p>{'tags': ['sitting',
  'cat',
  'brown',
  'indoor',
  'dog',
  'looking',
  'animal',
  'staring',
  'camera',
  'standing',
  'tan',
  'front',
  'table',
  'laying',
  'close',
  'orange',
  'bed'],
 'captions': [{'text': 'a close up of a dog and a cat looking at the camera',
   'confidence': 0.8600456236335963}]}</p>
<pre><code>- google 포토에서 '브롤스타즈'를 검색하면 나오는 원리로, 태그를 달 항목을 찾아준다. _미쳤음_


### detect (객체 탐지)
</code></pre><h1 id="object-detection">Object Detection</h1>
<p>response = requests.post(detect_endpoint,
                         headers=headers,
                         json=data)</p>
<p>result = response.json()
result</p>
<pre><code>
#### detect 결과
- 개와 고양이 객체 성공적으로 탐지하는 것을 볼 수 있다.</code></pre><p>{'objects': [{'rectangle': {'x': 195, 'y': 53, 'w': 360, 'h': 493},
   'object': 'dog',
   'confidence': 0.92,
   'parent': {'object': 'mammal',
    'confidence': 0.934,
    'parent': {'object': 'animal', 'confidence': 0.935}}},
  {'rectangle': {'x': 0, 'y': 235, 'w': 260, 'h': 317},
   'object': 'cat',
   'confidence': 0.869,
   'parent': {'object': 'mammal',
    'confidence': 0.88,
    'parent': {'object': 'animal', 'confidence': 0.881}}}],
 'requestId': '179b4ac2-6cd9-4b8e-8afb-b74e7092fa6a',
 'metadata': {'height': 552, 'width': 570, 'format': 'Jpeg'}}</p>
<pre><code></code></pre>