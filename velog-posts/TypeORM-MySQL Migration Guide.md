<h1 id="typeorm-migration-guide-🚥">TypeORM Migration Guide 🚥</h1>
<blockquote>
<p>ORM을 활용하여 데이터베이스 테이블을 자동으로 생성하면 물론 편하지만,
기존 데이터베이스에서 테이블을 생성 하고 엔티티를 역으로 마이그레이션 해야 하는 상황이 있다.
즉, 테이블 생성 ➡️ TypeORM Generator ➡️ 엔티티 수정</p>
</blockquote>
<h1 id="1-테이블-생성-📜">1. 테이블 생성 📜</h1>
<h2 id="a-reverse-engineer">a. Reverse Engineer</h2>
<ul>
<li>MySQL Workbench 8.0</li>
<li>Database - Reverse Engineer</li>
<li>다른 테이블을 참고하여 데이터베이스를 만들고 연관 관계를 추가한다.</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/2739ba69-abd2-4cda-85c2-1e06783c9743/image.png" /></p>
<h2 id="b-forward-engineer">b. Forward Engineer</h2>
<ul>
<li>작업을 다 마쳤다면 Database -Forward Engineer</li>
<li>테이블 생성 SQL 문을 확인할 수 있다.<pre><code class="language-sql"></code></pre>
</li>
</ul>
<hr />
<p>-- Table <code>test</code>.<code>test_reverse_copy</code></p>
<hr />
<p>CREATE TABLE IF NOT EXISTS <code>test</code>.<code>test_reverse_copy</code> (
  <code>test_reverse_copy_id</code> BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  <code>type</code> VARCHAR(20) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NOT NULL,
  <code>created_at</code> DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  <code>updated_at</code> DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  <code>deleted_at</code> DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (<code>test_reverse_copy_id</code>))
ENGINE = InnoDB
AUTO_INCREMENT = 166
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;</p>
<pre><code>
- Forward Engineer를 다 마쳤다면 다음과 같이 성공적으로 테이블이 생긴 것을 볼 수 있다.

![](https://velog.velcdn.com/images/rimgosu/post/37fbfd88-7efb-4d32-8a3f-a3d92ccee296/image.png)


# 2. TypeORM Migration 🧊
## a. typeorm-model-generator
- 연결된 데이터베이스의 상태를 토대로 엔티티를 만들어준다.
- 엔티티는 /output/entities 폴더에 만들어진다.</code></pre><p>npx typeorm-model-generator -h [호스트 주소] -p 3306 -d [데이터베이스 이름] -u [유저 이름] -x [접속패스워드] -e mysql</p>
<pre><code>- 응답 결과</code></pre><p>Need to install the following packages:
<a href="mailto:typeorm-model-generator@0.4.6">typeorm-model-generator@0.4.6</a>
Ok to proceed? (y) y
npm WARN deprecated <a href="mailto:adal-node@0.2.4">adal-node@0.2.4</a>: This package is no longer supported. Please migrate to @azure/msal-node.
npm WARN deprecated <a href="mailto:uuid@3.4.0">uuid@3.4.0</a>: Please upgrade  to version 7 or higher.  Older versions may use Math.random() in certain circumstances, which is known to be problematic.  See <a href="https://v8.dev/blog/math-random">https://v8.dev/blog/math-random</a> for details.
npm WARN deprecated @npmcli/move-file@1.1.2: This functionality has been moved to @npmcli/fs
<a href="mailto:typeorm-model-generator@0.4.6">typeorm-model-generator@0.4.6</a>
[3:28:27 PM] Starting creation of model classes.
[3:28:27 PM] Typeorm model classes created.
npm notice
npm notice New minor version of npm available! 10.2.3 -&gt; 10.5.0
npm notice Changelog: <a href="https://github.com/npm/cli/releases/tag/v10.5.0">https://github.com/npm/cli/releases/tag/v10.5.0</a>
npm notice Run npm install -g <a href="mailto:npm@10.5.0">npm@10.5.0</a> to update!
npm notice</p>
<pre><code>
## b. 엔티티 확인
- `/output/entities/TestReverseCopy.ts`
- 실제 TypeORM에서 사용하고 있는 엔티티 폴더로 옮겨 사용하도록 하자.
</code></pre><p>import { Column, Entity, PrimaryGeneratedColumn } from &quot;typeorm&quot;;</p>
<p>@Entity(&quot;test_reverse_copy&quot;, { schema: &quot;rever_school&quot; })
export class TestReverseCopy {
  @PrimaryGeneratedColumn({
    type: &quot;bigint&quot;,
    name: &quot;test_reverse_copy_id&quot;,
    unsigned: true,
  })
  testReverseCopyId: string;</p>
<p>  @Column(&quot;varchar&quot;, {
    name: &quot;type&quot;,
    length: 20,
  })
  type: string;</p>
<p>  @Column(&quot;datetime&quot;, {
    name: &quot;created_at&quot;,
    default: () =&gt; &quot;CURRENT_TIMESTAMP&quot;,
  })
  createdAt: Date;</p>
<p>  @Column(&quot;datetime&quot;, {
    name: &quot;updated_at&quot;,
    default: () =&gt; &quot;CURRENT_TIMESTAMP&quot;,
  })
  updatedAt: Date;</p>
<p>  @Column(&quot;datetime&quot;, { name: &quot;deleted_at&quot;, nullable: true })
  deletedAt: Date | null;
}</p>
<p>```</p>
<h2 id="c-엔티티에-필요-제약조건-설정">c. 엔티티에 필요 제약조건 설정</h2>
<ul>
<li>@IsNumber()</li>
<li>@ApiProperty()</li>
<li>IsString()</li>
</ul>
<p>다음과 같이, 필요한 제약 조건을 설정하고, 정상적으로 마이그레이션 되었다면 TypeORM과 연동 된다.</p>