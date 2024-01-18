<h2 id="강사-소개">강사 소개</h2>
<ul>
<li>원철연 강사님</li>
<li>예제로 배우는 Vue.js</li>
<li>C# XML &amp; LINQ 완벽가이드</li>
<li>초보자를 위한 C# and Database 완벽가이드</li>
<li><a href="https://fromyou.tistory.com/">https://fromyou.tistory.com/</a></li>
</ul>
<h2 id="자격증-추천">자격증 추천</h2>
<ul>
<li>az104</li>
<li>az204</li>
</ul>
<h1 id="azure">azure</h1>
<ul>
<li>기본적인 흐름</li>
</ul>
<ol>
<li>권한 확인</li>
<li>리소스 그룹 만들기</li>
<li>디스크 만들기</li>
</ol>
<h2 id="microsoft-entra-id">Microsoft Entra ID</h2>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/025f9fdb-1d0b-423a-b995-5f651c5b3d46/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/f239d6c9-e273-4d2d-b26e-56820fb5fcd3/image.png" /></p>
<ul>
<li>Microsoft Entra ID는 사용자 아이덴티티와 액세스를 관리하는 클라우드 서비스입니다. 이전에는 Azure Active Directory로 불렸습니다. 이 서비스를 통해 사용자 인증, 애플리케이션 접근 관리, 보안 강화 등이 가능합니다.</li>
</ul>
<h2 id="구독---리소스-공급자">구독 - 리소스 공급자</h2>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/a8c07c9d-d65e-4e0a-93dd-3bb2c5e2c551/image.png" /></p>
<ul>
<li>각 사용 권한에 대한 명세가 있다.</li>
<li>권한이 없을 때마다 풀어줘야한다.</li>
</ul>
<h2 id="리소스-그룹">리소스 그룹</h2>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/d1c3a90d-6ed8-4f1d-9145-1f99d5812673/image.png" /></p>
<ul>
<li>만들기</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/004a06ef-9ca5-4beb-ad29-ea6a61ec0024/image.png" /></p>
<h2 id="디스크">디스크</h2>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/0232ce2d-78e0-4ab4-b981-40ed3941952c/image.png" /></p>
<ul>
<li>만들기</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/75bb138f-74a6-4725-98b5-ce720fafd44b/image.png" /></p>
<ul>
<li>디스크를 만들면, 리소스 그룹 내에 리소스가 생성된 것을 확인할 수 있다.</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/e28ee0c0-741e-436d-9986-998830d0d8d4/image.png" /></p>
<h2 id="azure-clipower-shell">azure cli(power shell)</h2>
<ul>
<li><a href="https://shell.azure.com">https://shell.azure.com</a></li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/28da11f9-4d73-41c0-a30a-591e1627488b/image.png" /></p>
<h3 id="리소스-그룹-생성">리소스 그룹 생성</h3>
<pre><code class="language-bash">$location='eastasia'
$rgName='edu-destinationcy93-rg'
New-AzResourceGroup -Name $rgName -Location $location</code></pre>
<pre><code>PS /home/labuser93&gt; $location='eastasia'            
PS /home/labuser93&gt; $rgName='edu-destinationcy93-rg'
PS /home/labuser93&gt; New-AzResourceGroup -Name $rgName -Location $location

ResourceGroupName : edu-destinationcy93-rg
Location          : eastasia
ProvisioningState : Succeeded
Tags              : 
ResourceId        : /subscriptions/f5bc93f2-df0a-4b1a-ab9e-2b0203fc7d26/resourceGroups/edu-destinationcy93-rg</code></pre><h3 id="디스크-생성">디스크 생성</h3>
<pre><code class="language-bash">$location='eastasia'
$rgName='edu-destinationcy93-rg'
$diskConfig = New-AzDiskConfig `
-Location $location `
-CreateOption Empty `
-DiskSizeGB 32 `
-Sku Standard_LRS
$diskName = 'edu-ps-disk-93'
New-AzDisk `
-ResourceGroupName $rgName `
-DiskName $diskName `
-Disk $diskConfig</code></pre>
<pre><code>PS /home/labuser93&gt; $location='eastasia'            
PS /home/labuser93&gt; $rgName='edu-destinationcy93-rg'
PS /home/labuser93&gt; $diskConfig = New-AzDiskConfig `
&gt;&gt; -Location $location `
&gt;&gt; -CreateOption Empty `
&gt;&gt; -DiskSizeGB 32 `
&gt;&gt; -Sku Standard_LRS
PS /home/labuser93&gt; $diskName = 'edu-ps-disk-93'
PS /home/labuser93&gt; New-AzDisk `
&gt;&gt; -ResourceGroupName $rgName `
&gt;&gt; -DiskName $diskName `
&gt;&gt; -Disk $diskConfig

ResourceGroupName            : edu-destinationcy93-rg
ManagedBy                    : 
ManagedByExtended            : {}
Sku                          : Microsoft.Azure.Management.Compute.Models.DiskSku</code></pre><h2 id="azure-clibash">azure cli(bash)</h2>
<ul>
<li>bash로 변경</li>
</ul>
<h3 id="az-account-list--o-table">az account list -o table</h3>
<ul>
<li>계정 리스트 보기<pre><code class="language-bash">$ az account list -o table
Name                     CloudName    SubscriptionId                        TenantId                              State    IsDefault</code></pre>
</li>
</ul>
<hr />
<p>서울대학교 ChatGPT 과정  AzureCloud   f5bc93f2-df0a-4b1a-ab9e-2b0203fc7d26  c3b5a8fe-e46d-4078-9bd0-5eb0bb801edb  Enabled  True</p>
<pre><code>
### az resource list -o table
- 계정 리소스 그룹 확인
```bash
$ az resource list -o table
Name                                                  ResourceGroup                      Location          Type                                                Status
----------------------------------------------------  ---------------------------------  ----------------  --------------------------------------------------  --------
cs110032003416f2f58                                   cloud-shell-storage-southeastasia  southeastasia     Microsoft.Storage/storageAccounts
cs110032003416f2f66                                   cloud-shell-storage-southeastasia  southeastasia     Microsoft.Storage/storageAccounts
cs110032003416f2f6a                                   cloud-shell-storage-southeastasia  southeastasia     Microsoft.Storage/storageAccounts</code></pre><h3 id="az-group-delete---name-edu-destinationcy93-rg---no-wait---yes-✏️">az group delete --name edu-destinationcy93-rg --no-wait --yes ✏️</h3>
<ul>
<li>azgroup 삭제</li>
<li>비동기로 삭제해주는 명령어이다 </li>
<li>원래 삭제하는거 하나하나 해야하는데, 한 방에 삭제해서 편하다</li>
</ul>
<h2 id="arm-template-✅">ARM Template ✅</h2>
<ul>
<li>ARM(Azure Resource Manager) 템플릿은 Azure의 리소스를 정의하고 배포하기 위한 JSON 파일로, 클라우드 <strong>리소스의 구성 및 관리를 자동화</strong>하는 데 사용됩니다.</li>
<li>인프라를 정의하는 개념인 IaC의 한 형태</li>
<li>Azure Portal에서 VM, Storage를 생성하기 위해 클릭할 필요 없이 key-value 쌍으로 이어진 json 형태의 ARM template 이용 리소스를 정의하고 Azure Resource Manager가 리소스를 생성하도록 함</li>
</ul>
<h3 id="arm-template를-이용-디스크-리소스-그룹-생성-리소스-그룹-복제하기">ARM Template를 이용 디스크, 리소스 그룹 생성 (리소스 그룹 복제하기)</h3>
<ol>
<li>Azure Portal을 이용하여 리소스 그룹과 리소스 생성</li>
<li>생성한 리소스로부터 Template 다운로드(parameters.json, template.json)</li>
<li>Azure Portal에서 사용자 지정 탬플릿 배포(Deploy a custom template) 실행</li>
<li>parameters.json, template.json 업로드, 수정 후 배포</li>
</ol>
<h4 id="1-json-받기">1. json 받기</h4>
<ul>
<li>리소스 그룹 - 배포 - Deployment name - 템플릿 - 다운로드 - 압축 풀기</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/2c099939-c828-48bf-816a-9b1c5e79a9c6/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/14fb12ba-0ce8-4d81-8bd4-cb9824cf949a/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/f64a5c79-38df-42cb-9691-6d1808ae7ef2/image.png" /></p>
<h4 id="2-사용자-지정-템플릿-배포">2. 사용자 지정 템플릿 배포</h4>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/767e323e-300d-42f3-b88b-60f5a9f2863d/image.png" /></p>
<ul>
<li>'편집기에서 사용자 고유의 템플릿을 빌드합니다.' - 파일 로드 - template.json</li>
<li>sourceResourceId 삭제, hyperVGeneration 삭제<pre><code>&quot;sourceResourceId&quot;: {
          &quot;type&quot;: &quot;String&quot;
      },
&quot;hyperVGeneration&quot;: {
          &quot;defaultValue&quot;: &quot;V1&quot;,
          &quot;type&quot;: &quot;String&quot;
      },</code></pre></li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/c566ce46-56e0-4fa5-b419-312a59fd7438/image.png" /></p>
<ul>
<li>매개변수 편집- 파일 로드 - parameter.json</li>
<li>diskName value 수정</li>
</ul>
<pre><code>&quot;diskName&quot;: {
            &quot;value&quot;: &quot;eduarmdiskjh02&quot;
        },</code></pre><ul>
<li>다음과 같이 똑같이 디스크 복제되어 생성된 것을 확인할 수 있다.</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/cae89500-3822-4400-9aed-a623aa45be7f/image.png" /></p>
<h2 id="스토리지-계정">스토리지 계정</h2>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/5c1e2237-f845-45e5-8147-3e47636e8066/image.png" /></p>
<ul>
<li>만들기 - LRS(로컬 중복 스토리지) - 다음: 고급</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/1aa6ea4f-2e0f-442b-8282-97b3c0e6f350/image.png" /></p>
<ul>
<li>보안 - 개별 컨테이너에 대한 익명 액세스 허용 ✅ (클릭해줘야 생성 후 수정 가능하다) - 검토 - 만들기</li>
<li>마찬가지로 템플릿 다운로드 ㄱㄱ</li>
</ul>
<h3 id="azure-powershell">azure powershell</h3>
<h4 id="1-json-업로드">1. json 업로드</h4>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/fcee1e1b-ac61-41cf-8943-1fb056770cb3/image.png" /></p>
<ul>
<li>bash쉘로 변경 후 parameter.json, template.json 둘 다 업로드 하자.</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/e04b4a12-66e4-4a17-af9e-4be036968f9a/image.png" /></p>
<ul>
<li><code>template.json</code><ul>
<li>&quot;parameters&quot; 내용 삭제</li>
<li>&quot;storageAccounts_name&quot; 추가</li>
<li>아래와 같이 빈 값이 되게끔 나오면 된다.</li>
</ul>
</li>
</ul>
<pre><code class="language-javascript">{
    &quot;$schema&quot;: &quot;http://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#&quot;,
    &quot;contentVersion&quot;: &quot;1.0.0.0&quot;,
    &quot;parameters&quot;: {
        &quot;storageAccounts_name&quot;:{
            &quot;type&quot;:&quot;String&quot;,
            &quot;metadata&quot;:{
                &quot;description&quot;:&quot;My first storage account&quot;
            }
        },
        &quot;location&quot;: {
            &quot;type&quot;: &quot;String&quot;,
            &quot;metadata&quot;: {
                &quot;description&quot;: &quot;Location for all resources.&quot;
            }
        }
    },
    &quot;variables&quot;: {},
    &quot;resources&quot;: [
        {
            &quot;type&quot;: &quot;Microsoft.Storage/storageAccounts&quot;,
            &quot;apiVersion&quot;: &quot;2022-05-01&quot;,
            &quot;name&quot;: &quot;[parameters('storageAccounts_name')]&quot;,
            &quot;location&quot;: &quot;[parameters('location')]&quot;,
            &quot;dependsOn&quot;: [],
            &quot;tags&quot;: {},
            &quot;sku&quot;: {
                &quot;name&quot;: &quot;Standard_LRS&quot;,
                &quot;tier&quot;: &quot;Standard&quot;

            },
            &quot;kind&quot;: &quot;StorageV2&quot;,

        }
    ],
    &quot;outputs&quot;: {}
}</code></pre>
<ul>
<li><code>parameters.json</code><pre><code class="language-javascript">{
  &quot;$schema&quot;: &quot;https://schema.management.azure.com/schemas/2015-01-01/deploymentParameters.json#&quot;,
  &quot;contentVersion&quot;: &quot;1.0.0.0&quot;,
  &quot;parameters&quot;: {
      &quot;storageAccounts_name&quot;: {
          &quot;value&quot;: &quot;uniquestorage123xyz&quot;
      },
      &quot;location&quot;: {
          &quot;value&quot;: &quot;eastus&quot;
      }
  }
}</code></pre>
</li>
</ul>
<h4 id="2-리소스-그룹-생성">2. 리소스 그룹 생성</h4>
<pre><code class="language-bash">az group create -l koreacentral -n usingjh01-rg</code></pre>
<pre><code class="language-bash">$ az group create -l koreacentral -n usingjh01-rg
{
  &quot;id&quot;: &quot;/subscriptions/f5bc93f2-df0a-4b1a-ab9e-2b0203fc7d26/resourceGroups/usingjh01-rg&quot;,
  &quot;location&quot;: &quot;koreacentral&quot;,
  &quot;managedBy&quot;: null,
  &quot;name&quot;: &quot;usingjh01-rg&quot;,
  &quot;properties&quot;: {
    &quot;provisioningState&quot;: &quot;Succeeded&quot;
  },
  &quot;tags&quot;: null,
  &quot;type&quot;: &quot;Microsoft.Resources/resourceGroups&quot;
}</code></pre>
<h4 id="3-az-그룹-배포">3. az 그룹 배포</h4>
<ul>
<li><p>실행 명령어</p>
<pre><code class="language-bash">az deployment group create --name armdeployjh01 --resource-group usingjh01-rg --template-file template.json --parameters parameters.json</code></pre>
</li>
<li><p>기댓값</p>
<pre><code class="language-bash">PS /home/labuser93&gt; az deployment group create --name armdeployjh01 --resource-group usingjh01-rg --template-file template.json --parameters parameters.json
{
&quot;id&quot;: &quot;/subscriptions/f5bc93f2-df0a-4b1a-ab9e-2b0203fc7d26/resourceGroups/usingjh01-rg/providers/Microsoft.Resources/deployments/armdeployjh01&quot;,
&quot;location&quot;: null,
&quot;name&quot;: &quot;armdeployjh01&quot;,
&quot;properties&quot;: {
  &quot;correlationId&quot;: &quot;23b25601-9c0e-40b2-b9b0-7f7dbbc17667&quot;,
  ...
</code></pre>
</li>
</ul>
<p>}</p>
<pre><code>

## azure 스토리지 👍
- 테이블 데이터 뿐만 아니라 다양한 데이터를 대용량으로 저장 가능
   - 정형 데이터
   - 반정형 데이터
   - 비정형 데이터
- 이 셋 다 저장 가능한 장소이다.

&gt; 다음에서 배울 수 있는 것
&gt;&gt; 1. 파일(이미지) 공유 후 주소로 공유
&gt;&gt; 2. 윈도우 가상머신에서 스토리지 공유 (윈도우 뿐만 아니라 맥, 리눅스에서도 가능)



### 컨테이너 ✅

![](https://velog.velcdn.com/images/rimgosu/post/fa6cc87e-756d-4535-858a-dc17cd95a0c9/image.png)

- 컨테이너 추가 - imgfolder

![](https://velog.velcdn.com/images/rimgosu/post/4ab020eb-ea70-47ee-b0e6-5b4ca2b08768/image.png)

![](https://velog.velcdn.com/images/rimgosu/post/b6830beb-cdc2-48fe-8ad7-c30ac1d4f4bd/image.png)
</code></pre>
<code>ResourceNotFound</code>
The specified resource does not exist. RequestId:9c07a97d-101e-0110-8083-47a1e4000000 Time:2024-01-15T07:23:43.3226425Z

```
- 권한이 없어서 이미지에 엑세스할 수 없다. 그러므로 엑세스 수준을 컨테이너로 바꿔보자.

<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/b4c88dd8-60f1-4281-b784-807c70951ccd/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/212fe0ce-1635-43b5-8e00-5efc621cf5b3/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/1197bdb2-3d6f-46ca-939e-9b78c1f8322b/image.png" /></p>
<ul>
<li>다음과 같이 이미지 잘 나오는 것을 볼 수 있다.</li>
<li><em>이럼 이미지 업로드할 때 S3같은거 안써도 되는 거 아닌가?</em></li>
</ul>
<h3 id="파일-공유-✅">파일 공유 ✅</h3>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/3184edad-3760-44b7-a2b9-08850e869073/image.png" /></p>
<ul>
<li>만들기 - 백업 사용 체크 해제 (이거 때문에 파일 삭제도 안되고 리소스 그룹 삭제도 안될 염려가 있다.)</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/addd1fd0-fadb-45f6-8009-ada6d4533268/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/8def9a87-dd2f-4f9f-943d-e0854d1071bf/image.png" /></p>
<ul>
<li>다음과 같이 잘 만들어졌다.</li>
</ul>
<h3 id="가상-머신-✅">가상 머신 ✅</h3>
<ul>
<li>윈도우 10으로 가상머신 만들어보자</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/3220956d-465c-40d8-a439-2a8e47cde2dc/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/db150f3e-d690-4483-98ed-78b08fc7998e/image.png" /></p>
<ul>
<li>VM 삭제 시 공용 IP 및 NIC 삭제 체크</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/a333be69-f689-4126-a54e-4bbb251c1dd3/image.png" /></p>
<ul>
<li>진단 : 사용 안함</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/dc360510-474b-4a2d-b810-6322d1d1ba12/image.png" /></p>
<ul>
<li>jhvm01.rdp 파일을 더블클릭하여 접속 가능하다. (완전히 동일한 윈도우 환경임)</li>
</ul>
<h3 id="가상머신-스토리지-연결-✅">가상머신 스토리지 연결 ✅</h3>
<ul>
<li>스토리지 - 연결 - 스크립트</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/adb27b29-fc40-4f0b-8c83-0c3a49f79b81/image.png" /></p>
<ul>
<li>가상머신의 power shell ise에 스크립트를 붙여넣기 하자</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/3cec82d6-e2ce-4cf5-8711-5bc81b21202d/image.png" /></p>
<ul>
<li>다음과 같이 스토리지 공유할 수 있는 디스크가 추가된 것을 볼 수 있다.</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/61ff1227-2eec-44a5-87ce-5ea07036db78/image.png" /></p>
<ul>
<li>스토리지에 <code>first share.txt</code> 파일을 만들어 저장해보았다.</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/d9860745-3851-49da-a54a-de9d59d8cd53/image.png" /></p>
<ul>
<li>스토리지 - 찾아보기(탐색기)에서 파일이 추가된 것을 볼 수 있다.</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/da86d4da-ebe8-4e66-bf2f-f6826dd4251e/image.png" /></p>