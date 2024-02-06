<p>SSH 키 파일(<code>amazon-linux-key.pem</code>)의 권한 문제로 인해 발생하는 이 오류는 윈도우에서 파일의 권한을 조정하여 해결할 수 있습니다. SSH 키는 매우 민감한 정보를 포함하고 있기 때문에, 보안을 위해 해당 파일을 오직 파일 소유자만 읽을 수 있도록 설정해야 합니다. 다음은 윈도우에서 이 문제를 해결하는 방법을 단계별로 설명합니다:</p>
<ol>
<li><p><strong>파워셸을 관리자 권한으로 실행합니다.</strong> 시작 메뉴에서 'PowerShell'을 검색하고, 마우스 오른쪽 버튼으로 클릭한 후 '관리자로 실행'을 선택합니다.</p>
</li>
<li><p><strong>SSH 키 파일이 있는 디렉토리로 이동합니다.</strong> <code>cd</code> 명령어를 사용하여 키 파일이 위치한 디렉토리로 이동합니다. 예를 들어, 키 파일이 <code>C:\gits\private\ec2</code>에 있다면 다음과 같이 입력합니다:</p>
<pre><code class="language-powershell">cd C:\gits\private\ec2</code></pre>
</li>
<li><p><strong>키 파일의 권한을 변경합니다.</strong> 파일의 권한을 변경하여 오직 파일 소유자만이 읽기 권한을 가지도록 설정합니다. 이를 위해 <code>icacls</code> 명령어를 사용합니다. 다음 명령어를 실행합니다:</p>
<pre><code class="language-powershell">icacls amazon-linux-key.pem /reset
icacls amazon-linux-key.pem /grant:r &quot;$($env:USERNAME):(R)&quot;
icacls amazon-linux-key.pem /inheritance:r</code></pre>
<p>이 명령어들은 첫째로 파일의 권한을 초기화하고, 둘째로 현재 사용자에게 읽기 권한만 부여하며, 셋째로 상속받은 권한을 제거합니다.</p>
</li>
</ol>