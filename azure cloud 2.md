<h1 id="azure">azure</h1>
<h2 id="🗂️-스토리지">🗂️ 스토리지</h2>
<h3 id="🐧-파일공유-with-linux-os">🐧 파일공유 with Linux OS</h3>
<ol>
<li>리소스 그룹 만들기</li>
<li>스토리지 만들기</li>
<li>스토리지 내 파일 공유 만들기</li>
<li>가상머신 만들기 (ubuntu 22.04 LTS)<ul>
<li>VM 삭제 시 공유 IP 및 NIC 삭제 ✅</li>
<li>ssh 키 쌍으로 연결 ✅</li>
<li>.pem 파일 다운로드</li>
</ul>
</li>
<li>파일 공유 - 연결 - 리눅스 스크립트 복사</li>
<li>/mnt/jhfileshare 폴더에서 파일 공유 가능하다.</li>
</ol>
<ul>
<li><p>리눅스에서 🐧 
<img alt="" src="https://velog.velcdn.com/images/rimgosu/post/b7319661-f85c-4494-8aeb-8b1e1a5d587f/image.png" /></p>
</li>
<li><p>Azure 파일 공유에서 🔄️
<img alt="" src="https://velog.velcdn.com/images/rimgosu/post/e9140461-e762-4368-a129-645dd747eeec/image.png" /></p>
</li>
</ul>
<h2 id="🔑-네트워크-보안-그룹">🔑 네트워크 보안 그룹</h2>
<h3 id="가상-네트워크">가상 네트워크</h3>
<ul>
<li>가상 네트워크 - 서브넷 추가</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/26e53e46-723e-4cc5-a034-3f4a11039a44/image.png" /></p>
<h3 id="가상-머신">가상 머신</h3>
<ul>
<li>Windows Server 2019 Datacenter - x64 Gen2</li>
<li>위에서 만든 가상 네트워크를 추가</li>
<li>부트진단 사용 안함</li>
<li>고급 - 확장설치 - Microsoft Antimulware 추가</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/9a950a42-ad5f-4c82-8bdc-61f7dffd62d4/image.png" /></p>
<h3 id="네트워크-보안-그룹">네트워크 보안 그룹</h3>
<ul>
<li>가상머신과 가상 네트워크를 만든 리소스 그룹에서 네트워크 보안그룹을 클릭해보자. 인바운드 규칙과 아웃바운드 규칙이 있다.</li>
<li><strong>우선순위</strong> : 숫자가 낮을수록 우선순위가 높다<ul>
<li>ex) 300번 인바운드 보안 규칙이 65500 보안규칙보다 우선순위가 높아 3389 TCP 포트는 허용한다.</li>
</ul>
</li>
</ul>