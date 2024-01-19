<h1 id="java-백엔드-면접-질문">java 백엔드 면접 질문</h1>
<ul>
<li>어제 면접 볼 때 몰랐었던 것들 위주로 피드백 해본다.</li>
</ul>
<h2 id="1-sort">1. sort</h2>
<ul>
<li>배열을 받을 때 오름차순으로 정렬하는 코드를 짜시오.</li>
<li>java에서 보통 ArrayList를 사용하므로 제대로 답변하지 못했다.</li>
<li>직접 쳐보면서 버블정렬 구현하는거 해봐야할듯하다.</li>
</ul>
<pre><code>public class BubbleSort {
    public static void main(String[] args) {
        int[] array = {64, 34, 25, 12, 22, 11, 90};
        bubbleSort(array);
        System.out.println(&quot;정렬된 배열: &quot;);
        for (int i = 0; i &lt; array.length; i++) {
            System.out.print(array[i] + &quot; &quot;);
        }
    }

    static void bubbleSort(int[] array) {
        int n = array.length;
        for (int i = 0; i &lt; n - 1; i++) {
            for (int j = 0; j &lt; n - i - 1; j++) {
                if (array[j] &gt; array[j + 1]) {
                    // 원소들의 위치를 교환
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
    }
}
</code></pre><h2 id="2-정규화">2. 정규화</h2>
<ul>
<li>원부이결다조 이것만 알고 있었는데 정확히 뜻은 몰라서 다시 한 번 리마인드 해야할 듯 하다.</li>
<li><a href="https://code-lab1.tistory.com/48">https://code-lab1.tistory.com/48</a></li>
<li>1정규화, 2정규화, 3정규화, BCNF까지는 꼭 공부해놓도록 하자.</li>
</ul>
<h2 id="3-db-인덱스-구현">3. DB 인덱스 구현</h2>
<ul>
<li>CREATE INDEX - ON -();<pre><code class="language-sql">CREATE INDEX idx_username ON users(username);</code></pre>
</li>
</ul>
<h2 id="4-db-페이징-구현">4. DB 페이징 구현</h2>
<ul>
<li>MySQL에서 구현</li>
<li>LIMIT, OFFSET으로 구현하면된다.<pre><code class="language-sql">SELECT * FROM 테이블명
LIMIT 10 OFFSET 0;</code></pre>
</li>
</ul>