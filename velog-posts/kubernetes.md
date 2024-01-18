<h1 id="kubernetes-✍️">kubernetes ✍️</h1>
<ul>
<li>조타; 키잡이(helmsman)나 파일럿을 뜻하는 그리스어에서 유래</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/a4c3f57d-1dae-4aae-9dbb-c9d98cc69adc/image.jpeg" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/b803fb7a-0ba7-42de-8622-b34e1b47a8d6/image.jpeg" /></p>
<ul>
<li>aks : azure kubernetes service</li>
<li>eks : aws kubernetes service</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/7fe227a2-08cd-4c0e-b097-48c856c40546/image.jpeg" /></p>
<ul>
<li>실습 환경 : minikube</li>
<li>kubernetes 설정하는거 하루종일 걸리는데 좀 간편하게 실습 가능하다</li>
<li>한 대 컴퓨터안에 마스터, 노드 구조로 되어있는 심플한 구조</li>
<li>원래는 서브넷 쪼개고 컴퓨터를 네트워크로 묶고 어쩌구.. 해야함</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/26608d1c-466a-4f54-99cf-188a50e0fea8/image.jpeg" /></p>
<ul>
<li>master / node 구조</li>
<li>사람은 kubectl란 cli 환경을 통해 master과만 통신함. 그럼 master가 알아서 node 관리해주는 구조로 되어있다.</li>
</ul>
<h2 id="minikube-설치">minikube 설치</h2>
<ol>
<li><p>curl로 minikube 다운로드 및 설치</p>
<pre><code>curl -LO https://storage.googleapis.com/minikube/releases/v1.22.0/minikube-linux-amd64 
sudo install minikube-linux-amd64 /usr/local/bin/minikube</code></pre></li>
<li><p>설치 확인</p>
<pre><code>minikube --help</code></pre></li>
<li><p>kubectl 설치</p>
<pre><code>curl -LO https://dl.k8s.io/release/v1.22.1/bin/linux/amd64/kubectl 
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl</code></pre></li>
<li><p>kubectl 설치 확인</p>
<pre><code>kubectl --help</code></pre></li>
</ol>
<h2 id="minikube-시작하기">minikube 시작하기</h2>
<ol>
<li>미니쿠베 시작하기<pre><code>$ minikube start --driver=docker
😄  minikube v1.22.0 on Ubuntu 20.04
✨  Using the docker driver based on user configuration
</code></pre></li>
</ol>
<p>💣  Exiting due to PROVIDER_DOCKER_NEWGRP: &quot;docker version --format -&quot; exit status 1: permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get &quot;http://%2Fvar%2Frun%2Fdocker.sock/v1.24/version&quot;: dial unix /var/run/docker.sock: connect: permission denied
💡  Suggestion: Add your user to the 'docker' group: 'sudo usermod -aG docker $USER &amp;&amp; newgrp docker'
📘  Documentation: <a href="https://docs.docker.com/engine/install/linux-postinstall/">https://docs.docker.com/engine/install/linux-postinstall/</a></p>
<pre><code>
1-2. 트러블 슈팅1
- docker 권한 줘야한다.</code></pre><p>sudo usermod -aG docker $USER
newgrp docker
minikube start --driver=docker</p>
<pre><code>- 다음 명령어로 docker에 대한 권한을 받으면 정상적으로 실행 가능하다.</code></pre><p>$ sudo usermod -aG docker $USER
rp docker
$ newgrp docker
$ minikube start --driver=docker
😄  minikube v1.22.0 on Ubuntu 20.04
✨  Using the docker driver based on user configuration
🎉  minikube 1.32.0 is available! Download it: <a href="https://github.com/kubernetes/minikube/releases/tag/v1.32.0">https://github.com/kubernetes/minikube/releases/tag/v1.32.0</a>
💡  To disable this notice, run: 'minikube config set WantUpdateNotification false'</p>
<p>👍  Starting control plane node minikube in cluster minikube
🚜  Pulling base image ...
💾  Downloading Kubernetes v1.21.2 preload ...
    &gt; preloaded-images-k8s-v11-v1...: 502.14 MiB / 502.14 MiB  100.00% 29.21 Mi
    &gt; gcr.io/k8s-minikube/kicbase...: 361.08 MiB / 361.09 MiB  100.00% 15.39 Mi
🔥  Creating docker container (CPUs=2, Memory=2200MB) ...
🐳  Preparing Kubernetes v1.21.2 on Docker 20.10.7 ...
    ▪ Generating certificates and keys ...
    ▪ Booting up control plane ...
    ▪ Configuring RBAC rules ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: storage-provisioner, default-storageclass
🏄  Done! kubectl is now configured to use &quot;minikube&quot; cluster and &quot;default&quot; namespace by default</p>
<pre><code>
1-3. 트러블슈팅2. 컴퓨터 사양을 늘려보자 
- 램 8기가 -&gt; 램 16기가
- 중지 -&gt; 크기 -&gt; d4s3 (램16기가) -&gt; 크기 조정

![](https://velog.velcdn.com/images/rimgosu/post/263c528c-9226-4505-a923-5123a7929385/image.png)

![](https://velog.velcdn.com/images/rimgosu/post/b80a3e84-1c05-4af8-8c8e-7ab5f64466ff/image.png)



2. minikube 시스템 상태 확인</code></pre><p>$ minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured</p>
<pre><code>
2-1. kubectl 시스템의 구성 확인
- 쿠버네티스 자체도 다 도커 컨테이너 환경으로 되어있다.
</code></pre><p>$ kubectl get pod -n kube-system
NAME                               READY   STATUS    RESTARTS   AGE
coredns-558bd4d5db-d4ff9           1/1     Running   1          41m
etcd-minikube                      1/1     Running   1          41m
kube-apiserver-minikube            1/1     Running   1          41m
kube-controller-manager-minikube   1/1     Running   1          41m
kube-proxy-d4vk9                   1/1     Running   1          41m
kube-scheduler-minikube            1/1     Running   1          41m
storage-provisioner                1/1     Running   2          41m</p>
<pre><code>

3. minikube 삭제</code></pre><p>minikube delete </p>
<pre><code>

## pod
- 쿠버네티스에서 생성하고 관리할 수 있는 배포 가능한 가장 작은 컴퓨팅 단위를 말함
- &lt;https://kubernetes.io/ko/docs/concepts/workloads/pods/&gt;
- pod 단위로 스케줄링, 로드밸런싱, 스케일링 등의 관리 작업을 수행합니다.
- pod는 container를 감싼 개념이라고 생각하면 된다.


### pod 생성
1. pod.yaml 생성
- vi pod.yaml

```yaml
apiVersion: v1 # kubernetes resource 의 API Version 
kind: Pod # kubernetes resource name 
metadata: # 메타데이터 : name, namespace, labels, annotations 등을 포함 
  name: counter 
spec: # 메인 파트 : resource 의 desired state 를 명시 
  containers: 
  - name: count # container 의 이름 
    image: busybox # container 의 image 
    args: [/bin/sh, -c, 'i=0; while true; do echo &quot;$i: $(date)&quot;; i=$((i+1)); sleep 1; done'] # 해당 image 의 entrypoint 의 args 로 입력하고 싶은 부분 </code></pre><ol start="2">
<li>pod.yaml의 명세를 통해 *<em>pod 생성 *</em></li>
</ol>
<ul>
<li>kubectl apply<pre><code>$ kubectl apply -f pod.yaml
pod/counter created </code></pre></li>
</ul>
<h3 id="pod-조회">pod 조회</h3>
<ol>
<li>pod get <strong>pod 확인</strong></li>
</ol>
<pre><code>$ kubectl get pod
NAME      READY   STATUS    RESTARTS   AGE
counter   1/1     Running   0          6m56s</code></pre><ul>
<li>-A 옵션으로 kube-system이 실행시키고 있는 pod의 목록 확인도 가능하다</li>
</ul>
<pre><code>$ kubectl get pod -A
NAMESPACE     NAME                               READY   STATUS    RESTARTS   AGE
default       counter                            1/1     Running   0          10m
kube-system   coredns-558bd4d5db-d4ff9           1/1     Running   1          85m
kube-system   etcd-minikube                      1/1     Running   1          86m
kube-system   kube-apiserver-minikube            1/1     Running   1          86m
kube-system   kube-controller-manager-minikube   1/1     Running   1          86m
kube-system   kube-proxy-d4vk9                   1/1     Running   1          85m
kube-system   kube-scheduler-minikube            1/1     Running   1          86m
kube-system   storage-provisioner                1/1     Running   2          86m</code></pre><ul>
<li>kubectl get pod [pod 이름]<ul>
<li>특정 pod 이름의 pod를 조회할 수 있다</li>
</ul>
</li>
</ul>
<pre><code>$ kubectl get pod counter
NAME      READY   STATUS    RESTARTS   AGE
counter   1/1     Running   0          11m</code></pre><ul>
<li><p>kubectl get pod -o wide</p>
<ul>
<li>더 자세하게 확인 가능하다. ip 정보 확인 가능<pre><code>$ kubectl get pod -o wide
NAME      READY   STATUS    RESTARTS   AGE   IP           NODE       NOMINATED NODE   READINESS GATES
counter   1/1     Running   0          13m   172.17.0.3   minikube   &lt;none&gt;           &lt;none&gt;</code></pre></li>
</ul>
</li>
<li><p>kubectl get pod -o yaml --&gt; a.yaml</p>
<ul>
<li>pod의 정보를 yaml로 출력하기
```yaml
$ cat a.yaml
apiVersion: v1
items:</li>
</ul>
</li>
<li><p>apiVersion: v1
kind: Pod
metadata:
  annotations:</p>
<pre><code>kubectl.kubernetes.io/last-applied-configuration: |
  {&quot;apiVersion&quot;:&quot;v1&quot;,&quot;kind&quot;:&quot;Pod&quot;,&quot;metadata&quot;:{&quot;annotations&quot;:{},&quot;name&quot;:&quot;counter&quot;,&quot;namespace&quot;:&quot;default&quot;},&quot;spec&quot;:{&quot;containers&quot;:[{&quot;args&quot;:[&quot;/bin/sh&quot;,&quot;-c&quot;,&quot;i=0; while true; do echo \&quot;$i: $(date)\&quot;; i=$((i+1)); sleep 1; done&quot;],&quot;image&quot;:&quot;busybox&quot;,&quot;name&quot;:&quot;count&quot;}]}}</code></pre><pre><code></code></pre></li>
<li><p>kubectl get pod -w</p>
<ul>
<li>실시간 모니터링 가능</li>
</ul>
</li>
</ul>
<pre><code>$ kubectl get pod -w
NAME      READY   STATUS    RESTARTS   AGE
counter   1/1     Running   0          135m</code></pre><ul>
<li>kubectl logs [pod 이름]</li>
<li>kubectl logs [pod 이름] -f # 실시간 로그 확인<pre><code>$ kubectl logs counter
0: Fri Jan 12 02:34:36 UTC 2024
1: Fri Jan 12 02:34:37 UTC 2024
2: Fri Jan 12 02:34:38 UTC 2024
3: Fri Jan 12 02:34:39 UTC 2024
4: Fri Jan 12 02:34:40 UTC 2024
5: Fri Jan 12 02:34:41 UTC 2024
6: Fri Jan 12 02:34:42 UTC 2024</code></pre></li>
</ul>
<h3 id="pod-안으로-들어가기">pod 안으로 들어가기</h3>
<ul>
<li>만약 counter pod에 bash 쉘이 있다면 /bin/bash로 접속 가능<pre><code>kubectl exec -it counter /bin/bash</code></pre></li>
</ul>
<h3 id="pod-삭제">pod 삭제</h3>
<ul>
<li>kubectl delete pod [pod-name]</li>
<li>kubectl delete -f [yaml-파일-경로]</li>
</ul>
<pre><code>$ kubectl delete pod counter
pod &quot;counter&quot; deleted</code></pre><h2 id="deployment">deployment</h2>
<ul>
<li>Deployment는 Pod와 Replicaset에 대한 <strong>관리</strong>를 제공하는 단위입니다.</li>
<li><a href="https://kubernetes.io/ko/docs/concepts/workloads/controllers/deployment/">https://kubernetes.io/ko/docs/concepts/workloads/controllers/deployment/</a></li>
<li><strong>관리</strong>라는 의미는 Self-healing, Scaling, Rollout(무중단 업데이트)와 같은 기능을 포함합니다.</li>
<li>Deployment는 pod를 감싼 개념이라고 생각할 수 있습니다.<ul>
<li>pod를 Deployment로 배포함으로써 여러 개로 복제된 Pod, 여러 버전의 Pod를 안전하게 관리할 수 있습니다.</li>
</ul>
</li>
</ul>
<h3 id="deployment-생성">deployment 생성</h3>
<ul>
<li>vi deployment.yaml<pre><code class="language-yaml">apiVersion: apps/v1 # kubernetes resource 의 API Version 
kind: Deployment # kubernetes resource name 
metadata: # 메타데이터 : name, namespace, labels, annotations 등을 포함 
name: nginx-deployment 
labels: 
  app: nginx 
spec: # 메인 파트 : resource 의 desired state 를 명시 
replicas: 3 # 동일한 template 의 pod 을 3 개 복제본으로 생성합니다. 
selector: 
  matchLabels: 
    app: nginx 
template: # Pod 의 template 을 의미합니다. 
  metadata: 
    labels: 
      app: nginx 
  spec: 
    containers: 
    - name: nginx # container 의 이름 
      image: nginx:1.14.2 # container 의 image 
      ports: 
      - containerPort: 80 # container 의 내부 Port 
</code></pre>
</li>
</ul>
<pre><code>   - `replicas : 3` : pod의 갯수를 3으로 지정하겠다. 복제본 3개가 생성되어서 가용성이 증가함. 

- kubectl apply -f deployment.yaml</code></pre><p>$ kubectl apply -f deployment.yaml
deployment.apps/nginx-deployment created</p>
<pre><code>
### deployment 조회
- kubectl get deployment
</code></pre><p>$ kubectl get deployment
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
nginx-deployment   3/3     3            3           2m39s</p>
<pre><code>
- kubectl get pods
   - pod 3개가 복제되어 생긴 것을 확인할 수 있다</code></pre><p>$ kubectl get pod
NAME                                READY   STATUS    RESTARTS   AGE
nginx-deployment-66b6c48dd5-45xkd   1/1     Running   0          5m19s
nginx-deployment-66b6c48dd5-5zvll   1/1     Running   0          5m19s
nginx-deployment-66b6c48dd5-s8mtq   1/1     Running   0          5m19s</p>
<pre><code>
### auto-healing
- pod를 하나 삭제시켜보자
   - auto-healing 기능으로 pod가 삭제되면 새로운 pod를 만들어준다.</code></pre><p>$ kubectl delete pod nginx-deployment-66b6c48dd5-s8mtq
pod &quot;nginx-deployment-66b6c48dd5-s8mtq&quot; deleted</p>
<p>$ kubectl get pods
NAME                                READY   STATUS    RESTARTS   AGE
nginx-deployment-66b6c48dd5-45xkd   1/1     Running   0          8m16s
nginx-deployment-66b6c48dd5-5zvll   1/1     Running   0          8m16s
nginx-deployment-66b6c48dd5-btwqc   1/1     Running   0          22s</p>
<pre><code>

### pod scaling (갯수 늘리기)
- kubectl scale [deployment 이름] --replicas=[늘릴 갯수]</code></pre><p>$ kubectl scale deployment/nginx-deployment --replicas=5
deployment.apps/nginx-deployment scaled
$ kubectl get pods
NAME                                READY   STATUS    RESTARTS   AGE
nginx-deployment-66b6c48dd5-45xkd   1/1     Running   0          11m
nginx-deployment-66b6c48dd5-5zvll   1/1     Running   0          11m
nginx-deployment-66b6c48dd5-btwqc   1/1     Running   0          3m57s
nginx-deployment-66b6c48dd5-m76j8   1/1     Running   0          3s
nginx-deployment-66b6c48dd5-n5ffh   1/1     Running   0          3s</p>
<pre><code>
### deployment 삭제
- kubectl delete deployment [deployment-name]
</code></pre><p>$ kubectl delete -f deployment.yaml
deployment.apps &quot;nginx-deployment&quot; deleted</p>
<pre><code>

## Service
- Service는 쿠버네티스에 배포한 어플리케이션(Pod)을 외부에서 접근하기 쉽게 추상화한 리소스입니다.
- &lt;https://kubernetes.io/ko/docs/concepts/services-networking/service/&gt;
- Pod는 ip를 할당받고 생성되지만, 언제든지 죽었다가 다시 살아날 수 있으며, 그 과정에서 ip는 항상 재할당받기에 고정된 ip로 원하는 pod에 접근할 수는 없습니다.
- 따라서 클러스터 외부 혹은 내부에서 Pod에 접근할 때는, Pod의 ip가 아닌 Service를 통해서 접근하는 방식을 거칩니다.
- Service는 고정된 ip를 가지며, Service는 하나 혹은 여러 개의 Pod과 매칭됩니다.
- 따라서 클라이언트가 Service의 주소로 접근하면, 실제로는 Service에 매칭된 Pod에 접근할 수 있게 됩니다.

### Service 생성 전 사전 지식
- vi deployment2.yaml
- kubectl apply -f deployment2.yaml
```yaml
apiVersion: apps/v1 
kind: Deployment 
metadata: 
  name: nginx-deployment 
  labels: 
    app: nginx 
spec: 
  replicas: 3 
  selector: 
    matchLabels: 
      app: nginx 
  template: 
    metadata: 
      labels: 
        app: nginx 
    spec: 
      containers: 
      - name: nginx 
        image: nginx:1.14.2 
        ports: 
        - containerPort: 80</code></pre><h4 id="pod의-ip로-접속해보기">pod의 ip로 접속해보기</h4>
<ul>
<li><p>kubectl get pod -o wide</p>
<ul>
<li>172.17.0.4 ip 주소로 접속해보자<pre><code>$ kubectl get pod -o wide
NAME                                READY   STATUS    RESTARTS   AGE   IP           NODE       NOMINATED NODE   READINESS GATES
nginx-deployment-66b6c48dd5-8frt4   1/1     Running   0          67s   172.17.0.4   minikube   &lt;none&gt;           &lt;none&gt;
nginx-deployment-66b6c48dd5-mwrcc   1/1     Running   0          67s   172.17.0.5   minikube   &lt;none&gt;           &lt;none&gt;
nginx-deployment-66b6c48dd5-xkmwd   1/1     Running   0          67s   172.17.0.3   minikube   &lt;none&gt;           &lt;none&gt;</code></pre></li>
</ul>
</li>
<li><p>curl -X GET [ip주소] -vvv</p>
<ul>
<li>통신 안되는 것을 확인할 수 있다.
```
$ curl -X GET 172.17.0.4 -vvv
Note: Unnecessary use of -X or --request, GET is already inferred.</li>
</ul>
</li>
<li><p>Trying 172.17.0.4:80...</p>
</li>
<li><p>TCP_NODELAY set</p>
</li>
<li><p>connect to 172.17.0.4 port 80 failed: No route to host</p>
</li>
<li><p>Failed to connect to 172.17.0.4 port 80: No route to host</p>
</li>
<li><p>Closing connection 0
curl: (7) Failed to connect to 172.17.0.4 port 80: No route to host</p>
<pre><code></code></pre></li>
</ul>
<h4 id="minikube-ssh">minikube ssh</h4>
<ul>
<li><p>minikube의 라우터로 적속하는 명령어이다</p>
<pre><code>$ minikube ssh
docker@minikube:~$</code></pre></li>
<li><p>여기서 172.17.0.4로 접속해보자</p>
<ul>
<li>minikube의 라우터 안으로 들어간 후 사설망의 172.17.0.4로 접속하니, 다음과 같이 응답을 받는 것을 볼 수 있다.
```
docker@minikube:~$ curl -X GET 172.17.0.4 -vvv
Note: Unnecessary use of -X or --request, GET is already inferred.</li>
</ul>
</li>
<li><p>Trying 172.17.0.4:80...</p>
</li>
<li><p>TCP_NODELAY set</p>
</li>
<li><p>Connected to 172.17.0.4 (172.17.0.4) port 80 (#0)</p>
<blockquote>
<p>GET / HTTP/1.1
Host: 172.17.0.4
User-Agent: curl/7.68.0
Accept: <em>/</em></p>
</blockquote>
</li>
<li><p>Mark bundle as not supporting multiuse
&lt; HTTP/1.1 200 OK</p>
<pre><code>
</code></pre></li>
</ul>
<h3 id="service-생성">Service 생성</h3>
<ul>
<li><p>vi service.yaml</p>
<pre><code class="language-yaml">apiVersion: v1 
kind: Service 
metadata: 
name: my-nginx 
labels: 
  run: my-nginx 
spec: 
type: NodePort # Service 의 Type 을 명시하는 부분입니다. 자세한 설명은 추후 말씀드리겠습니다. 
ports: 
- port: 80 
  protocol: TCP 
selector: # 아래 label 을 가진 Pod 을 매핑하는 부분입니다. 
  app: nginx  </code></pre>
</li>
<li><p>kubectl apply -f service.yaml</p>
</li>
</ul>
<pre><code>$ kubectl apply -f service.yaml
service/my-nginx created</code></pre><h3 id="service-조회">service 조회</h3>
<ul>
<li>kubectl get service<pre><code>$ kubectl get service
NAME         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
kubernetes   ClusterIP   10.96.0.1        &lt;none&gt;        443/TCP        4h40m
my-nginx     NodePort    10.104.175.251   &lt;none&gt;        80:32528/TCP   2m7s</code></pre></li>
<li>다음과 같이 30842 포트가 외부와 연결되었다.</li>
<li>그러나 클라우드 환경에서 진행하므로, 보안상 방화벽으로 막혀있어서 안됨.. (실습종료)</li>
</ul>
<h1 id="ip-network-지식-👍">ip network 지식 👍</h1>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/2d48580d-ac16-49e4-b960-ef5051852836/image.png" /></p>
<h2 id="private-network사설망">private network(사설망)</h2>
<ul>
<li>private network : 일반적으로 192.~으로 시작하는 주소들을 묶는 것을 private network라고 한다.</li>
<li>사설망은 192.168.0.2, 192.168.0.3 ... 과 같이 192.~ 로 되어있다</li>
<li>공유기 = Gateway(NAT) = 라우터 : 192.168.0.1을 주소로 가진다</li>
<li>공유기는 192.~로 되어있는 주소들 각각을 연결해 181.227.3.33과 같은 주소를 변환해 인터넷에 접속한다.</li>
</ul>
<h2 id="이와-같은-사설망-개념은-쿠버네티스에서도-적용된다">이와 같은 사설망 개념은 쿠버네티스에서도 적용된다</h2>
<ul>
<li>도커 : 각각의 컴퓨터 192.168.0.2, 192.168.0.3, ...</li>
<li>쿠버네티스 : 각각의 컴퓨터를 묶어 라우팅 해주는 역할을 한다. 192.168.0.1</li>
</ul>
<h2 id="16-bit-vs-20-bit">16 bit vs 20 bit</h2>
<ul>
<li>16 bit : 192.168.0.0 ~ 192.~ </li>
<li>20 bit : 172.16.0.0 ~ 172.~ (쿠버네티스가 채택함 ✅)</li>
</ul>
<h2 id="쿠버네티스는-사설망에-있다">쿠버네티스는 사설망에 있다</h2>
<ul>
<li>그래서 나중에 인터넷에 연결하려면 사설망과 공용망 주소를 연결해주는 세팅이 필요하다.</li>
</ul>