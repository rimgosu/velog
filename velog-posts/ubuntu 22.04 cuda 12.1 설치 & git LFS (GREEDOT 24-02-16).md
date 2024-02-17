<h2 id="todo">TODO</h2>
<ol>
<li>azure gpu 달린 가상머신 열 것. 😢</li>
<li>감정분석 =&gt; 감정리포트 백엔드 작업 😢</li>
<li>파일업로드 테스트(목오브젝트 사용) 😢</li>
</ol>
<h2 id="진전-없는-하루">진전 없는 하루..</h2>
<ul>
<li><a href="https://github.com/GreeDot/predict-emotion">https://github.com/GreeDot/predict-emotion</a></li>
<li>azure에서 이미 pytorch와 cuda 이것저것 다 깔린 가상머신 오픈해서 해보려고 했는데, 하루종일 거의 아무것도 못했다.</li>
<li>일단 새로 ubuntu 22.04 서버를 개설해 처음부터 다시 까는 것이 나을 것 같다.</li>
</ul>
<h2 id="✔-ubuntu-2204-cuda-121-설치">✔ ubuntu 22.04 cuda 12.1 설치</h2>
<h3 id="1-ubuntu-업그레이드">1. ubuntu 업그레이드</h3>
<pre><code>sudo apt update
sudo apt upgrade
sudo apt install build-essential dkms
sudo apt install linux-headers-$(uname -r)</code></pre><h3 id="2-cuda-toolkit-121-downloads">2. CUDA Toolkit 12.1 Downloads</h3>
<ul>
<li><a href="https://developer.nvidia.com/cuda-12-1-0-download-archive?target_os=Linux&amp;target_arch=x86_64&amp;Distribution=Ubuntu&amp;target_version=22.04&amp;target_type=deb_network">https://developer.nvidia.com/cuda-12-1-0-download-archive?target_os=Linux&amp;target_arch=x86_64&amp;Distribution=Ubuntu&amp;target_version=22.04&amp;target_type=deb_network</a></li>
<li>아래 반드시 cuda-&lt;버전&gt;으로 설정해주어야한다.<pre><code>wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb
sudo apt-get update
sudo apt-get -y install cuda-12-1</code></pre></li>
</ul>
<h3 id="3-환경-변수-설정">3. 환경 변수 설정</h3>
<pre><code>echo 'export PATH=/usr/local/cuda-12.1/bin:$PATH' &gt;&gt; ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-12.1/lib64:$LD_LIBRARY_PATH' &gt;&gt; ~/.bashrc
source ~/.bashrc
</code></pre><h3 id="4-nvidia-드라이버-설치">4. nvidia 드라이버 설치</h3>
<h4 id="4-1-ubuntu-drivers-common-설치">4-1) ubuntu-drivers-common 설치</h4>
<pre><code>sudo apt install ubuntu-drivers-common
sudo ubuntu-drivers autoinstall
sudo reboot</code></pre><h4 id="4-2-nvidia-smi">4-2) nvidia-smi</h4>
<pre><code>nvidia-smi</code></pre><ul>
<li>다음과 같이 nvidia-utils-버전 이 나오면 성공이다.<pre><code>azure-user@ai-service:~$ nvidia-smi
Command 'nvidia-smi' not found, but can be installed with:
sudo apt install nvidia-utils-390         # version 390.157-0ubuntu0.22.04.2, or
sudo apt install nvidia-utils-418-server  # version 418.226.00-0ubuntu5~0.22.04.1
sudo apt install nvidia-utils-450-server  # version 450.248.02-0ubuntu0.22.04.1
sudo apt install nvidia-utils-470         # version 470.223.02-0ubuntu0.22.04.1
sudo apt install nvidia-utils-470-server  # version 470.223.02-0ubuntu0.22.04.1
sudo apt install nvidia-utils-525         # version 525.147.05-0ubuntu0.22.04.1
sudo apt install nvidia-utils-525-server  # version 525.147.05-0ubuntu0.22.04.1
sudo apt install nvidia-utils-535         # version 535.129.03-0ubuntu0.22.04.1
sudo apt install nvidia-utils-535-server  # version 535.129.03-0ubuntu0.22.04.1
sudo apt install nvidia-utils-510         # version 510.60.02-0ubuntu1
sudo apt install nvidia-utils-510-server  # version 510.47.03-0ubuntu3</code></pre></li>
</ul>
<h4 id="4-3-r535-설치">4-3) R535 설치</h4>
<pre><code>sudo apt install nvidia-utils-535 </code></pre><blockquote>
<p>r535 설치 이유 : <a href="https://learn.microsoft.com/ko-kr/azure/virtual-machines/linux/n-series-driver-setup">https://learn.microsoft.com/ko-kr/azure/virtual-machines/linux/n-series-driver-setup</a></p>
</blockquote>
<h3 id="5-nvidia-드라이버-설치">5. nvidia 드라이버 설치</h3>
<ul>
<li><a href="https://learn.microsoft.com/ko-kr/azure/virtual-machines/linux/n-series-driver-setup">https://learn.microsoft.com/ko-kr/azure/virtual-machines/linux/n-series-driver-setup</a></li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/4d5d25a6-6a82-43d5-892d-ccdcc70b2471/image.png" /></p>
<ul>
<li>다음 사이트에서 NVIDIA vGPU 16.3, driver branch R535(.exe)를 다운로드 받아 ssh로 ubuntu로 옮겨주도록 하자.</li>
</ul>
<pre><code>scp -i ~/.ssh/id_rsa.pem NVIDIA-Linux-x86_64-535.154.05-grid-azure.run azure-user@20.214.136.176:~</code></pre><ul>
<li>실행<pre><code>sudo bash NVIDIA-Linux-x86_64-535.154.05-grid-azure.run</code></pre></li>
</ul>
<h2 id="✔-git-lfs">✔ git LFS</h2>
<ul>
<li>학습된 모델이 너무 커서(300메가) 한 번에 깃허브에 올리지 못하는 문제가 발생하여 LFS를 사용하어 업로드 하였다.</li>
</ul>
<h3 id="git-lfs-설치">git lfs 설치</h3>
<pre><code>sudo apt-get update
sudo apt-get install git-lfs</code></pre><h3 id="git-lfs-pull">git lfs pull</h3>
<ul>
<li>lfs로 파일이 올라간 레포지토리를 clone하고, lfs를 pull받는 과정을 진행하면 된다.<pre><code>git lfs pull</code></pre></li>
</ul>