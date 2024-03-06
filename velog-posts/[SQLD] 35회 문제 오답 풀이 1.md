<h2 id="문제-5-다음-보기-중-분산-데이터베이스에-대한-특징으로-부적절한-것은">문제 5. 다음 보기 중 분산 데이터베이스에 대한 특징으로 부적절한 것은?</h2>
<p>1) 지역 자치성, 점증적 시스템 용량이 확장된다.
2) 빠른 응답속도와 통신비용을 절감할 수 있다.
3) 데이터 처리 비용이 증대한다.
4) 데이터 무결성을 보장하고 데이터 보안성이 높아진다.</p>
<h3 id="문제-5-해설">문제 5 해설</h3>
<p>정답: 4
분산 데이터베이스는 여러 위치에 분산되어 있는 데이터베이스 시스템을 말합니다. 이 시스템은 여러 장점을 제공하지만, 각 옵션이 그 특성을 정확히 반영하는지를 평가하는 것이 중요합니다. 각 보기를 분석해 보겠습니다.</p>
<p>1) 지역 자치성, 점증적 시스템 용량이 확장된다.</p>
<ul>
<li>분산 데이터베이스는 각 지역에서 자체적으로 데이터를 관리할 수 있으며, 필요에 따라 시스템의 용량을 점진적으로 확장할 수 있습니다. 따라서 이는 분산 데이터베이스의 특징으로 적절합니다.</li>
</ul>
<p>2) 빠른 응답속도와 통신비용을 절감할 수 있다.</p>
<ul>
<li>사용자가 가까운 위치에서 데이터에 접근할 수 있기 때문에, 응답 속도가 빨라지고 통신 비용이 절감될 수 있습니다. 이 역시 분산 데이터베이스의 장점 중 하나입니다.</li>
</ul>
<p>3) 데이터 처리 비용이 증대한다.</p>
<ul>
<li>분산 데이터베이스는 데이터를 여러 위치에 분산하여 저장하기 때문에, 일관성을 유지하고 통합 관리하는 데 추가적인 비용이 발생할 수 있습니다. 그러나 이는 필연적으로 증대된다기보다는 관리 및 설계에 따라 달라질 수 있습니다. 분산 처리 시스템의 설계와 최적화에 따라 오히려 전체적인 데이터 처리 비용을 줄일 수도 있습니다. 그러므로 이 옵션은 부분적으로만 적절할 수 있습니다.</li>
</ul>
<p>4) 데이터 무결성을 보장하고 데이터 보안성이 높아진다.</p>
<ul>
<li>분산 데이터베이스는 데이터 무결성과 보안성을 강화할 수 있는 기능을 제공하지만, 이는 자동으로 보장되는 것은 아닙니다. 오히려 여러 위치에 데이터를 분산 저장함으로써, 무결성 유지와 보안성 확보를 위한 추가적인 노력이 필요할 수 있습니다. 따라서, 이는 분산 데이터베이스의 잠재적인 이점으로 볼 수 있지만, 자동으로 보장되는 특성은 아닙니다.</li>
</ul>
<p>이 분석을 통해 볼 때, 각 보기가 분산 데이터베이스의 특징을 대체로 잘 반영하고 있으나, &quot;3) 데이터 처리 비용이 증대한다&quot;는 상황에 따라 다를 수 있으므로, 이 보기가 상대적으로 부적절할 수 있습니다. 그러나 분산 데이터베이스 시스템의 설계와 운영 방법에 따라 데이터 처리 비용이 증가할 수도 있고, 효율성이 높아질 수도 있어서, 정답을 판단하는 데 있어 맥락을 고려해야 합니다. 보편적으로 분산 데이터베이스에 대한 이해를 바탕으로 한다면, 이 질문은 다소 모호할 수 있으며, 전문가의 해석에 따라 답변이 달라질 수 있습니다.</p>
<h2 id="문제-11-아래의-ansi-join-sql에서-가장-올바르지-않은-것은">문제 11. 아래의 ANSI JOIN SQL에서 가장 올바르지 않은 것은?</h2>
<p>1) SELECT EMP.DEPTNO, EMPNO, ENAME, DNAME FROM EMP INNER JOIN DEPT ON EMP.DEPTNO = DEPT.DEPTNO;
2) SELECT EMP.DEPTNO, EMPNO, ENAME, DNAME FROM EMP NATURAL JOIN DEPT;
3) SELECT*FROM DEPT JOIN DEPT_TEMP USING(DEPTNO);
4) SELECT E.EMPNO, E.ENAME, D.DEPTNO, D.DNAME FROM EMP E INNER JOIN DEPT D ON (E.DEPTNO = D.DEPTNO);</p>
<h3 id="문제-11-해설">문제 11 해설</h3>
<ol start="11">
<li>정답 :  2
해설 : NATURAL JOIN에서 EMP.DEPTNO와 같이 OWNER 명을 사용하면 에러 발생</li>
</ol>
<h2 id="문제-13-union에-대한-설명-중-바른-것은">문제 13. UNION에 대한 설명 중 바른 것은?</h2>
<p>1) 데이터의 중복 행을 제거한다.
2) 데이터의 중복 행을 포함한다.
3) 정렬 작업을 수행하지 않는다.
4) 두 테이블에 모두 포함된 행을 검색한다.</p>
<h3 id="문제-13-해설">문제 13 해설</h3>
<ul>
<li>정답 :  1 </li>
<li>해설 : UNION은 중복된 행을 제거하고 정렬한다. UNION ALL은 합집합</li>
</ul>
<h3 id="문제-13-해설-2">문제 13 해설 2</h3>
<p>UNION에 대한 설명 중 바른 것을 찾기 위해서는, UNION의 기본적인 특성을 이해해야 합니다.</p>
<ul>
<li><p><strong>1) 데이터의 중복 행을 제거한다.</strong></p>
<ul>
<li><strong>바른 설명</strong>: SQL에서 <code>UNION</code> 연산자는 두 개 이상의 <code>SELECT</code> 문의 결과 집합을 합칠 때 사용됩니다. 이 과정에서 중복되는 행은 자동으로 제거되어, 결과 집합에는 각각의 고유한 행만 포함됩니다. 따라서, 이 설명은 <code>UNION</code>에 대해 바르게 설명하고 있습니다.</li>
</ul>
</li>
<li><p><strong>2) 데이터의 중복 행을 포함한다.</strong></p>
<ul>
<li><strong>잘못된 설명</strong>: 이 설명은 <code>UNION ALL</code> 연산자의 특성에 해당됩니다. <code>UNION ALL</code>은 <code>UNION</code>과 달리 중복된 행을 제거하지 않고 모든 행을 포함하여 결과 집합을 반환합니다.</li>
</ul>
</li>
<li><p><strong>3) 정렬 작업을 수행하지 않는다.</strong></p>
<ul>
<li><strong>잘못된 설명</strong>: <code>UNION</code> 연산을 수행할 때, SQL 서버는 결과 집합의 중복을 제거하기 위해 내부적으로 정렬 작업을 수행할 수 있습니다. 따라서, 이 설명은 정확하지 않습니다. 사용자가 <code>ORDER BY</code>를 명시적으로 사용하지 않더라도, 중복 제거 과정에서 내부적인 정렬이 일어날 수 있습니다.</li>
</ul>
</li>
<li><p><strong>4) 두 테이블에 모두 포함된 행을 검색한다.</strong></p>
<ul>
<li><strong>잘못된 설명</strong>: 이 설명은 <code>INNER JOIN</code> 또는 <code>INTERSECT</code> 연산의 특성에 더 가깝습니다. <code>UNION</code>은 두 개 이상의 쿼리 결과를 합치는데, 각 쿼리 결과에 있는 모든 고유 행을 포함합니다. 반면, 두 테이블에 모두 포함된 행만을 검색하는 것은 <code>INNER JOIN</code>이나 <code>INTERSECT</code> 연산의 기능입니다.</li>
</ul>
</li>
</ul>
<p>따라서, 이 중에서 <code>UNION</code>에 대한 설명으로 가장 바른 것은 <strong>1) 데이터의 중복 행을 제거한다</strong>입니다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/23ca8146-25ac-4521-b6ae-3c66f0cf52ac/image.png" /></p>
<h2 id="문제-26-다음-중-데이터-무결성을-보장하기-위한-방법으로-가장-부적절한-것은">문제 26. 다음 중 데이터 무결성을 보장하기 위한 방법으로 가장 부적절한 것은?</h2>
<p>1) 애플리케이션
2) Trigger
3) Lock
4) 제약조건</p>
<h3 id="문제-26-정답">문제 26 정답</h3>
<p>정답 :  3</p>
<ul>
<li>해설 : Lock/Unlock은 병행성 제어(동시성) 기법이다.</li>
<li>무결성 : 데이터 임의 갱신으로부터 보호해야 하는 것.</li>
<li>제약조건을 넣어서 무결성을 보장하거나, Triger 로직 안에 검사 기능을 넣을 수도 있고, 개발자의 코딩에서 로직을 넣을 수도 있다.</li>
</ul>
<h2 id="📋-connect-by">📋 CONNECT BY</h2>
<ul>
<li>이 절을 이용하여 계층 질의에서 상위계층(부모행)과 하위계층(자식행)의 관계를 규정할 수 있다.</li>
<li>PRIOR연산자와 함께 사용하여 계층구조로 표현할 수 있다.</li>
<li>CONNECT BY PRIOR 자식컬럼 = 부모컬럼 : 부모에서 자식으로 트리 구성 (Top Down)</li>
<li>CONNECT BY PRIOR 부모컬럼 = 자식컬럼 : 자식에서 부모로 트리 구성 (Bottom Up)</li>
<li>CONNECT BY NOCYCLE PRIOR: NOCYCLE 파라미터를 이용하여 무한 루프 방지</li>
<li>서브 쿼리를 사용할 수 없다.</li>
</ul>
<blockquote>
<p>항상 ⬅️
자식 = 부모 : 부모에서 자식으로(순방향)
부모 = 자식 : 자식에서 부모로(역방향)</p>
</blockquote>
<h2 id="문제-30-다음-중-문자열이-입력될-때-빈-공간으로-채우는-형태의-데이터-타입은">문제 30. 다음 중 문자열이 입력될 때 빈 공간으로 채우는 형태의 데이터 타입은?</h2>
<p>1) VARCHAR2
2) CHAR
3) DATE
4) NUMBER</p>
<h3 id="문제-30-정답">문제 30 정답</h3>
<p>정답 :  2
해설 : CHAR(10)으로 칼럼을 생성하고 8개의 문자를 입력하면 나머지 2개는 공백으로 입력된다. VARCHAR2는 가변길이 문자열 타입으로 입력한 크기만큼 할당된다.</p>
<h2 id="문제-49-아래의-sql에-대한-column-header를-적으시오dbms--oracle">문제 49. 아래의 SQL에 대한 Column Header를 적으시오(DBMS : Oracle)</h2>
<pre><code>&lt;SQL&gt;
SELECT employee_id, DEPARTMENT_ID, SALARY AS &quot; salary&quot;
FROM SQLD_49
WHERE EMPLOYEE_ID &lt; 110;</code></pre><h3 id="문제-49-정답">문제 49 정답</h3>
<p>정답 :  EMPLOYEE_ID, DEPARTMENT_ID, salary</p>
<h2 id="문제-50-아래-데이터를-가진-테이블에-대한-sql결과를-적으시오">문제 50. 아래 데이터를 가진 테이블에 대한 SQL결과를 적으시오.</h2>
<pre><code>[SQLD_50]
COL1     COL2
--------------
1
2
3        1
4        1
5        2
6        2
7        3
8        4
9        5
10       6

- - - - - - -

SELECT COUNt(*)
FROM SQLD_50
WHERE COL1 &lt;&gt; 4
START WITH COL1 = 1
CONNECT BY PRIOR COL1 = COL2;
</code></pre><h3 id="문제-50-쿼리-✔️">문제 50 쿼리 ✔️</h3>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/8da45c75-5aad-43df-b2c4-35c77b37bf28/image.png" /></p>
<ul>
<li>정답: 4</li>
</ul>
<h3 id="문제-50-해설">문제 50 해설</h3>
<p>이 SQL 쿼리는 오라클 데이터베이스의 계층형 쿼리 기능을 사용하여 특정 조건을 만족하는 행의 수를 계산합니다. 계층형 쿼리는 <code>START WITH ... CONNECT BY</code> 구문을 사용하여 데이터 간의 부모-자식 관계를 탐색합니다. 이 쿼리를 분석하고 어떤 결과를 반환하는지, 그리고 그 로직에 대해 설명하겠습니다.</p>
<h3 id="쿼리-분석">쿼리 분석</h3>
<pre><code class="language-sql">SELECT COUNT(*)
FROM my_second_table
WHERE COL1 &lt;&gt; 4
START WITH COL1 = 1
CONNECT BY PRIOR COL1 = COL2;</code></pre>
<ul>
<li><code>START WITH COL1 = 1</code>: 쿼리는 <code>COL1</code> 값이 1인 행에서 시작합니다. 이는 쿼리의 '루트' 또는 시작점을 정의합니다.</li>
<li><code>CONNECT BY PRIOR COL1 = COL2</code>: 이 구문은 테이블 내의 행들 사이의 관계를 정의합니다. 여기서는 <code>COL1</code>의 값이 이전 행(<code>PRIOR</code>)의 <code>COL2</code> 값과 같은 행을 찾아 계층을 형성합니다. 즉, <code>COL2</code>가 부모 <code>COL1</code>을 가리키는 자식-부모 관계를 형성합니다.</li>
<li><code>WHERE COL1 &lt;&gt; 4</code>: 이 조건은 <code>COL1</code>의 값이 4가 아닌 행만을 대상으로 합니다. 계층 구조가 형성된 후에 이 필터가 적용되어 최종 결과에서 제외됩니다.</li>
</ul>
<h3 id="로직-설명">로직 설명</h3>
<ol>
<li><code>COL1</code>이 1인 행을 시작점으로 선택합니다.</li>
<li><code>COL1</code>의 값이 다른 행의 <code>COL2</code> 값과 일치하는 방식으로 연결하여 계층을 형성합니다.</li>
<li>이 과정에서 <code>COL1</code> 값이 4인 행은 제외합니다.</li>
<li>최종적으로 선택된 행들의 수를 카운트합니다.</li>
</ol>
<h3 id="결과-예측">결과 예측</h3>
<p>이 쿼리를 실행하면 <code>COL1</code>이 1인 행에서 시작하여 계층형 구조를 따라가면서 <code>COL1</code> 값이 4가 아닌 행들을 카운트합니다. 이 테이블 구조와 데이터를 고려했을 때, <code>COL1</code>이 1인 행은 <code>COL2</code>를 통해 <code>COL1</code>이 3인 행으로 연결됩니다. 그러나 <code>COL1</code>이 4인 행은 <code>WHERE</code> 조건에 의해 제외됩니다. 따라서, 계층형 쿼리는 <code>COL1</code>이 1인 행에서 시작하여 <code>COL1</code>이 3인 행으로만 이동할 수 있으며, 이후 연결 가능한 <code>COL1</code> 값이 4인 행은 제외됩니다.</p>
<p>그러나, <code>START WITH</code>에서 <code>COL1</code>이 1인 행을 시작점으로 설정했고, <code>COL1</code> 값이 4인 행을 제외하라는 조건을 더했음에도 불구하고, 실제로 <code>COL1</code>이 4인 행으로 직접 연결되는 행은 없습니다. <code>CONNECT BY</code> 조건에 따라 <code>COL1</code>이 1인 행은 자식이 없으므로, 이 쿼리는 단순히 <code>COL1</code>이 1인 행만을 카운트하는 것으로 보입니다. 따라서, 결과는 1이 될 것으로 예상합니다.</p>
<p>그러나, 제가 설명한 내용은 쿼리의 기본 로직과 예상 결과에 대한 것이며, 실제 결과는 데이터베이스에서 쿼리를 실행해보지 않는 이상 확실하지 않습니다. 오라클의 계층</p>
<p>형 쿼리는 상당히 복잡할 수 있으며, <code>CONNECT BY</code> 조건이나 <code>WHERE</code> 절의 정확한 해석은 실행 컨텍스트에 따라 달라질 수 있습니다.</p>