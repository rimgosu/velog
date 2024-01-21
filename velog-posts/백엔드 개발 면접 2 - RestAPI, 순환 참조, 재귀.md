<h2 id="백엔드-면접-회고-2">백엔드 면접 회고 2</h2>
<ul>
<li>이번 주 총 세 번의 면접을 보았고, 백엔드 면접은 두 번째였다.</li>
<li>이번 면접은 자체 서비스가 있는 기업이었고, 내가 주로 사용하는 Spring이 아닌 장고로 개발을 진행하는 기업이었다. 기술 CTO님이 나와 면접을 진행했다.</li>
<li>그 중 답변 못했던 질문들에 대해 알아보는 시간을 가져보자.</li>
</ul>
<h2 id="1-restapi">1. RestAPI</h2>
<ul>
<li>RestAPI에 대해 알고 있냐는 질문에 GET, POST, PATCH, PUT, DELETE 함수를 말했다.</li>
<li>그러나 그 외 함수에 대해 알고 있으며, Options에 대해 알고 있냐는 질문을 받았다. </li>
<li>처음 들어보는 질문이었고, 제대로 답변하지 못했다.</li>
</ul>
<h3 id="restrepresentational-state-transfer란">REST(REpresentational State Transfer)란?</h3>
<ul>
<li>REST는 &quot;Representational State Transfer&quot;의 약자로, 자원의 상태를 주고받는 모든 것을 의미하며, 웹의 기존 기술과 HTTP 프로토콜을 활용하는 아키텍처 스타일입니다. </li>
</ul>
<h3 id="rest-api란">REST API란?</h3>
<ul>
<li>REST API는 REST의 특징을 기반으로 서비스 API를 구현한 것으로, 각 요청이 어떤 동작이나 정보를 위한 것인지 요청 자체로 추론 가능합니다. RESTful API는 REST 설계 규칙을 잘 따르는 API를 말하며, 이해하기 쉽고 사용하기 쉬운 API를 목표로 합니다. URI, HTTP 메소드, 표현 방식 등을 사용하여 자원에 대한 행위를 명확하게 표현합니다. </li>
</ul>
<h3 id="rest-api와-restful-api의-차이">REST API와 RESTful API의 차이?</h3>
<ul>
<li>RESTful은 REST의 설계 규칙을 잘 지켜서 설계된 API를 RESTful한 API라고 합니다.</li>
<li>즉, 주소만 봐도 어떤 응답을 받아올 지에 대해 쉽게 추측할 수 있게 주소를 설계하는 것을 RESTful API라고 한다.</li>
</ul>
<h3 id="5가지-주요-함수-외-다른-함수">5가지 주요 함수 외 다른 함수</h3>
<ol>
<li><p><strong>HEAD</strong>: GET 요청과 유사하지만, HEAD 요청은 실제 데이터 대신에 데이터의 메타데이터(예: 헤더 정보)만을 반환합니다. 이 메서드는 리소스의 존재 여부나 서버의 응답 헤더를 확인할 때 유용합니다.</p>
</li>
<li><p><strong>OPTIONS</strong>: 이 메서드는 웹 서버가 지원하는 HTTP 메서드를 확인하는 데 사용됩니다. CORS(Cross-Origin Resource Sharing)와 관련된 사전 요청(pre-flight request)에서도 사용됩니다.</p>
</li>
<li><p><strong>TRACE</strong>: 서버에 도달하는 요청의 변경 여부를 진단하기 위해 사용됩니다. 이는 클라이언트와 서버 사이의 요청/응답 체인을 테스트하는 데 사용될 수 있습니다.</p>
</li>
<li><p><strong>CONNECT</strong>: 클라이언트가 프록시 서버를 통해 다른 네트워크 서비스에 터널 연결을 요청하는 데 사용됩니다.</p>
</li>
</ol>
<p>이러한 메서드들은 특정한 상황에서 유용할 수 있지만, 일반적인 REST API 개발에서는 드물게 사용됩니다. 대부분의 RESTful 서비스는 주로 GET, POST, PUT, DELETE, PATCH 메서드에 집중합니다.</p>
<h2 id="2-순환-참조">2. 순환 참조</h2>
<ul>
<li>순환 참조에 대해 처음 들었다.</li>
<li>순환 참조시 메모리가 제대로 해제되지 않아 메모리 누수가 발생할 수 있다는 이야기를 들었다.</li>
</ul>
<h3 id="순환참조-예시1">순환참조 예시1</h3>
<pre><code>class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __del__(self):
        print(&quot;delete&quot;)

# 두 노드 생성
node1 = Node(1)
node2 = Node(2)

# 순환 참조 생성
node1.next = node2
node2.next = node1</code></pre><ul>
<li>다음과 같이 node1이 node2를 참조하고, node2가 node1을 참조하면 파이썬의 가비지 컬렉터가 동작하지 않아 메모리 누수 현상이 발생할 수 있다.</li>
<li>때문에 다음 함수는 종료가 되더라도 자동으로 가지비 컬렉터가 동작하지 않아 &quot;delete&quot;가 호출되지 않는다.</li>
</ul>
<h3 id="순환참조-예시2">순환참조 예시2</h3>
<pre><code>@Component
public class BeanA {
    private BeanB beanB;

    public void BeanA(BeanB beanB){
        this.beanB = beanB;
    }
}

@Component
public class BeanB {
    private BeanA beanA;

    public void BeanB(BeanA beanA){
        this.beanA = beanA;
    }
}</code></pre><ul>
<li>마찬가지로 자바에서도 가비지 컬렉터가 동작하는데, 이와같이 객체 내에서 객체를 불러올 때 순환 참조 이슈가 발생하여 메모리 릭 현상이 발생할 수 있다.</li>
<li>설계할 때 이를 고려해서 메모리 누수를 방지해야 한다는 뜻.</li>
</ul>
<h2 id="3-재귀함수">3. 재귀함수</h2>
<ul>
<li>최근 프로그래머스에서 문제를 풀면, dfs, bfs, dp 등 아무리 봐도 이해가 안되는 개념이 나왔다.</li>
<li>문제 하나를 풀어야 했는데 딱 문제를 이해하자 마자 '내가 못 푸는 문제인데..' 라고 생각하며 바로 못푼다고 말씀 드릴까 하다가 끝까지 풀다 결국 못풀었다.</li>
<li><a href="https://leetcode.com/problems/min-cost-climbing-stairs/description/">https://leetcode.com/problems/min-cost-climbing-stairs/description/</a></li>
</ul>
<h3 id="solution">Solution</h3>
<pre><code class="language-python">def minCostClimbingStairs(cost):
    n = len(cost)
    if n == 0 or n == 1:
        return 0

    min_cost = [0] * n
    min_cost[0], min_cost[1] = cost[0], cost[1]

    for i in range(2, n):
        min_cost[i] = min(min_cost[i - 1], min_cost[i - 2]) + cost[i]

    return min(min_cost[-1], min_cost[-2])

# 예시 사용법
cost = [10, 15, 20]
print(minCostClimbingStairs(cost))  # 출력 예: 15
</code></pre>
<ul>
<li>답 보고 푸는 개념을 좀 심도있게 생각해봐야겠다.</li>
<li>db, bfs, dfs 3월 전까지는 능숙하게 풀수 있으면 좋겠다.</li>
</ul>