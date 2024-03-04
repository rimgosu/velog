<h2 id="문제-14-주어진-두-개의-테이블에-대해서-아래의-sql문을-수행한-이후에-test1-테이블의-건수는">문제 14. 주어진 두 개의 테이블에 대해서 아래의 SQL문을 수행한 이후에 TEST1 테이블의 건수는?</h2>
<pre><code>[TEST1]
COL1  COL2  COL3
------------------
A      X      1
B      Y      2
C      Z      3

[TEST2]
COL1  COL2  COL3
------------------
A      X      1
B      Y      2
C      Z      3
D      가      4
E      나      5

[SQL]
MERGE INTO TEST1
USING TEST2
 ON (TEST1.COL1 = TEST2.COL1)
WHEN MATCHED THEN
 UPDATE SET TEST1.COL3 = 4
      WHERE TEST1.COL3 = 2
 DELETE WHERE TEST1.COL3 &lt;= 2
WHEN NOT MATCHED THEN
 INSERT(TEST1.COL1, TEST1.COL2, TEST1.COL3)
 VALUES(TEST2.COL1, TEST2.COL2, TEST2.COL3);</code></pre><p>1) 4
2) 3
3) 5
4) 8</p>
<h3 id="문제-14-해설-❓">문제 14 해설 ❓</h3>
<ul>
<li>일단 합쳐지는것 3개, delete</li>
<li>아니 근데 delete 하나 되어서 4개여야하는 거 아님?</li>
</ul>
<h2 id="문제-16-아래의-test10-테이블에-대해서-아래의-sql문을-수행하였을-때의-결과-건수는">문제 16. 아래의 TEST10 테이블에 대해서 아래의 SQL문을 수행하였을 때의 결과 건수는?</h2>
<pre><code>[TEST10]
EMPNO  NAME  MANAGER
--------------------
1      LIM     NULL
2      PARK    1
3      KIM     2

[SQL]
SELECT LPAD('**', (LEVEL-1) * 2, ' ')
       || EMPNO AS EMP, NAME
FROM TEST10
WHERE EMPNO &lt;&gt; 3
START WITH EMPNO = 3
CONNECT BY EMPNO = PRIOR MANAGER;</code></pre><p>1) 0
2) 1
3) 2
4) 3</p>
<h3 id="문제-16-해설">문제 16 해설</h3>
<p>이 SQL 문은 Oracle의 계층적 쿼리를 사용하여 <code>TEST10</code> 테이블에서 계층적 데이터를 조회하는 예입니다. 계층적 쿼리를 사용하면, 부모-자식 관계에 있는 행들을 계층적으로 검색할 수 있습니다. 여기서 사용된 키워드의 의미는 다음과 같습니다:</p>
<ul>
<li><code>START WITH EMPNO = 3</code>: EMPNO가 3인 행부터 검색을 시작합니다.</li>
<li><code>CONNECT BY EMPNO = PRIOR MANAGER</code>: 현재 행의 EMPNO가 이전 행의 MANAGER와 동일할 때, 이러한 관계를 사용하여 연결합니다.</li>
<li><code>WHERE EMPNO &lt;&gt; 3</code>: EMPNO가 3이 아닌 행만 결과에 포함합니다.</li>
</ul>
<p>그러나, <code>WHERE</code> 절이 <code>START WITH</code> 절보다 먼저 적용되지 않습니다. <code>START WITH</code>에서 검색을 시작하여 <code>CONNECT BY</code>를 통해 계층적으로 연결된 후, 최종 결과에 대해 <code>WHERE</code> 절이 적용됩니다. 따라서, <code>WHERE</code> 절은 <code>START WITH</code>에 의해 이미 선택된 행들에 대해서만 필터링하는 역할을 합니다.</p>
<p>이 쿼리의 경우, <code>EMPNO = 3</code>인 행에서 시작하여 그의 관리자로 거슬러 올라가려고 합니다. 그러나 <code>EMPNO &lt;&gt; 3</code>이라는 조건 때문에 실제로는 EMPNO가 3인 행이 결과에 포함되지 않습니다. 하지만, 이 조건은 <code>START WITH</code> 절이 적용된 후의 결과에 대해 필터링을 적용하기 때문에, EMPNO가 3인 행을 시작점으로 사용할 수 있습니다.</p>
<p>계층 구조는 다음과 같습니다:</p>
<ol>
<li>KIM (EMPNO = 3) - 시작점, 하지만 결과에는 포함되지 않음 (WHERE 조건 때문에)</li>
<li>PARK (EMPNO = 2, MANAGER = 1) - KIM의 관리자</li>
<li>LIM (EMPNO = 1, MANAGER = NULL) - PARK의 관리자</li>
</ol>
<p>따라서, <code>WHERE</code> 조건 (<code>EMPNO &lt;&gt; 3</code>)에 의해 EMPNO가 3인 KIM은 결과에서 제외되고, PARK와 LIM만 결과에 포함됩니다. 결과적으로 결과 건수는 2가 됩니다.</p>
<p>정답은 3) 2입니다.</p>
<h2 id="문제-35-주어진-erd에서-오류가-나지-않는-sql문을-고르시오">문제 35. 주어진 ERD에서 오류가 나지 않는 SQL문을 고르시오.</h2>
<pre><code>1)
SELECT * FROM 계좌마스터
WHERE 회원번호 = (SELECT DISTINCT 회원번호 FROM 고객);

2)
SELECT * FROM 계좌마스터 
WHERE 회원번호 IN (SELECT DISTINCT 회원번호 FROM 고객);

3)
SELECT 회원번호, 종목코드 FROM 일자별주문내역
WHERE 주문일자 EXISTS (SELECT DISTINCT 주문일자 FROM 계좌마스터);

4)
SELECT 회원번호, 종목코드 FROM 일자별주문내역
WHERE 주문일자 ALL (SELECT DISTINCT 주문일자 FROM 계좌마스터);</code></pre><h3 id="문제-35-어떻게-하면-오류-없이-굴러가는가">문제 35 어떻게 하면 오류 없이 굴러가는가</h3>
<h4 id="3번의-경우">3번의 경우</h4>
<pre><code>SELECT 회원번호, 종목코드 
FROM 일자별주문내역 
WHERE EXISTS (
    SELECT 1 FROM 계좌마스터 
    WHERE 계좌마스터.주문일자 = 일자별주문내역.주문일자
);</code></pre><ul>
<li>WHERE EXISTS 순으로 서브쿼리 자체를 받아야함</li>
</ul>
<h4 id="4번의-경우">4번의 경우</h4>
<pre><code>SELECT 회원번호, 종목코드 
FROM 일자별주문내역 
WHERE 주문일자 &gt;= ALL (
    SELECT DISTINCT 주문일자 FROM 계좌마스터
);
</code></pre><ul>
<li>ALL 키워드는 비교 연산자와 같이 사용해야함</li>
</ul>
<h2 id="문제-41-다음-보기-중-트랜잭션의-특징에-대한-설명중-올바른-것은">문제 41. 다음 보기 중 트랜잭션의 특징에 대한 설명중 올바른 것은?</h2>
<p>1) 원자성(Atomicity) : 트랜잭션 내의 모든 문장이 모두(ALL) 반영되거나, 혹은 일부가 반영 되어야 한다.
2) 영속성 : 트랜잭션의 수행으로 데이터베이스의 무결성은 보장 될 수 없다.
3) 일관성 : 여러 개의 트랜잭션들이 동시에 수행될 때, 한 개의 트랜잭션의 복사본을 유지한다.
4) 지속성 : Commit이 완료되면 영구적으로 저장을 보장해야 한다.</p>
<h3 id="문제-41-해설">문제 41 해설</h3>
<ol>
<li>원자성: 모두 반영 또는 모두 취소</li>
<li>일관성: 트랜잭션은 항상 일관적이어야 한다</li>
<li>고립성: 둘 이상의 트랜잭션이 실행되고 있을 때, 어떤 트랜잭션도 다른 트랜잭션 연산에 끼어들 수 없다</li>
<li>지속성: 트랜잭션이 성공적으로 작업을 마치면, 결과는 영구적으로 저장되어야 한다.</li>
</ol>
<h2 id="문제-45-oracle-환경에서-주어진-테이블을-아래의-결과와-같이-정렬하고자-할-때-sql문의-빈칸에-들어갈-값을-작성하시오">문제 45. Oracle 환경에서 주어진 테이블을 아래의 결과와 같이 정렬하고자 할 때, SQL문의 빈칸에 들어갈 값을 작성하시오.</h2>
<pre><code>[TEST45]
C1    C2
----------
10    100
10    200
10    NULL
20    100
20    NULL
20    200

[RESULT]
C1    C2
----------
10    200
10    100
10    NULL
20    200
20    100
20    NULL

[SQL]
SELECT C1, C2
FROM SQLD_02
ORDER BY C1, C2 DESC (      );</code></pre><h3 id="문제-45-정답">문제 45 정답</h3>
<ul>
<li>NULLS LAST</li>
</ul>