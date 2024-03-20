<h1 id="🚀-welcome">🚀 Welcome!</h1>
<blockquote>
<p>개발을 하다 보면 우분투의 초기 세팅을 하는 일이 잦다.
따라서 내가 우분투를 설치하고 나서 가장 먼저 세팅하는 것들을 위주로 소개하고자 한다.
꾸준히 업데이트 예정.</p>
</blockquote>
<h1 id="1-git-ssh-설정-🗝️">1. git ssh 설정 🗝️</h1>
<pre><code>ssh-keygen -t ed25519 -C &quot;newnyup@gmail.com&quot; # 본인 이메일 입력
eval &quot;$(ssh-agent -s)&quot;
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub</code></pre><ul>
<li>결과: ssh-ed25519 <em>[ssh-key]</em> newnyup@gmail.com</li>
<li>git에서 clone 시 ssh로 clone 하면 더 이상 password를 요구하지 않습니다.</li>
</ul>
<h1 id="2-docker-설치-🐋">2. docker 설치 🐋</h1>
<ul>
<li><a href="https://docs.docker.com/engine/install/ubuntu/">https://docs.docker.com/engine/install/ubuntu/</a><pre><code>sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo \
&quot;deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release &amp;&amp; echo &quot;$VERSION_CODENAME&quot;) stable&quot; | \
sudo tee /etc/apt/sources.list.d/docker.list &gt; /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin</code></pre></li>
</ul>
<h1 id="3-zsh-설치-💭">3. zsh 설치 💭</h1>
<pre><code>sudo apt-get update
sudo apt-get install zsh
chsh -s $(which zsh)</code></pre><h2 id="1-oh-my-zsh-설치">1) oh-my-zsh 설치</h2>
<pre><code>sh -c &quot;$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)&quot;</code></pre><h2 id="2-plugin-설치">2) plugin 설치</h2>
<pre><code>git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting</code></pre><ul>
<li>vi ~/.zshrc<pre><code>plugins=(
  git
  zsh-autosuggestions
  zsh-syntax-highlighting
)</code></pre></li>
<li>source ~/.zshrc</li>
</ul>
<h1 id="4-nvm-설치-💼">4. nvm 설치 💼</h1>
<pre><code>curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash</code></pre><h2 id="zshrc-설정-파일-변경">.zshrc 설정 파일 변경</h2>
<ul>
<li><p>vi ~/.zshrc</p>
<pre><code>autoload -U add-zsh-hook
load-nvmrc() {
local nvmrc_path=&quot;.nvmrc&quot;

# '.nvmrc' 파일이 현재 디렉토리에 있는지 확인
if [[ -f &quot;$nvmrc_path&quot; ]]; then
  nvm use
elif [[ $commands[nvm] ]]; then
  # '.nvmrc' 파일이 없다면 기본 버전을 사용
  nvm use default
fi
}
</code></pre></li>
</ul>
<h1 id="디렉토리가-변경될-때마다-load-nvmrc-함수를-실행">디렉토리가 변경될 때마다 'load-nvmrc' 함수를 실행</h1>
<p>add-zsh-hook chpwd load-nvmrc
load-nvmrc</p>
<pre><code>
- source ~/.zshrc
</code></pre>