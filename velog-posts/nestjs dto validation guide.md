<h1 id="🚀-nestjs-dto-validation-guide">🚀 nestjs dto validation guide</h1>
<blockquote>
<p>DTO: Data Transfer Object
클라이언트 측에서 Request를 받을 때 '타입 지정'만으로 validation 할 수 없다,
따라서 기본 validation 사용 방법과 custom validation을 사용하여 검증하는 것에 대해 정리하겠다.</p>
</blockquote>
<h2 id="1-picktype-🪵">1. PickType 🪵</h2>
<p>entity에서 정의된 제약 조건을 PickType 활용해 dto에서도 활용이 가능하다.</p>
<ul>
<li>다음과 같이 Mail 엔티티에서 정의된 'title'과 'html' 필드를 가져와 동일한 제약조건을 설정할 수 있다.</li>
</ul>
<pre><code>export class CreateMailDto extends PickType(Mail, [
  'title',
  'html',
]) {
  @IsArray()
  @Validate(CheckEmailList)
  userList: string[];
}</code></pre><p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/655db495-eb3d-4369-b059-10157d105de4/image.png" /></p>
<h2 id="2-class-validator-decorator-🗝️">2. class-validator decorator 🗝️</h2>
<p>nestjs 공식 문서에서 확인해보면 class-validator 라이브러리를 활용하여 validation을 하는 것을 권장하고 있다</p>
<ul>
<li><a href="https://docs.nestjs.com/techniques/validation">https://docs.nestjs.com/techniques/validation</a></li>
<li>예시에서 <code>@IsEmail()</code>, <code>@IsNotEmpty()</code> 등의 라이브러리를 활용하여 원하는 validation을 진행한다.</li>
</ul>
<pre><code>import { IsEmail, IsNotEmpty } from 'class-validator';

export class CreateUserDto {
  @IsEmail()
  email: string;

  @IsNotEmpty()
  password: string;
}</code></pre><h3 id="가장-자주-사용되는-validator-decorator">가장 자주 사용되는 validator decorator</h3>
<table>
<thead>
<tr>
<th>데코레이터</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>@IsString()</code></td>
<td>해당 필드의 값이 문자열인지 검증</td>
</tr>
<tr>
<td><code>@IsNotEmpty()</code></td>
<td>필드가 비어있지 않은지 검증. 문자열, 배열 등에서 사용할 수 있으며, 공백 문자열이나 빈 배열도 유효하지 않은 값으로 간주</td>
</tr>
<tr>
<td><code>@IsEmail()</code></td>
<td>해당 필드의 값이 유효한 이메일 형식인지 검증</td>
</tr>
<tr>
<td><code>@IsOptional()</code></td>
<td>필드 값이 제공되지 않거나 <code>undefined</code>일 경우에 검증을 건너뜀</td>
</tr>
<tr>
<td><code>@MinLength()</code> / <code>@MaxLength()</code></td>
<td>문자열의 최소 길이와 최대 길이를 검증</td>
</tr>
<tr>
<td><code>@IsInt()</code> / <code>@IsNumber()</code></td>
<td>해당 필드의 값이 정수 또는 숫자인지 검증</td>
</tr>
<tr>
<td><code>@IsBoolean()</code></td>
<td>필드 값이 불리언 타입인지 검증</td>
</tr>
<tr>
<td><code>@IsArray()</code></td>
<td>해당 필드의 값이 배열인지 검증</td>
</tr>
<tr>
<td><code>@ArrayNotEmpty()</code></td>
<td>배열이 비어있지 않은지 검증</td>
</tr>
<tr>
<td><code>@ValidateNested()</code></td>
<td>객체 배열에서 각 객체를 검증할 때 사용합니다. <code>@Type()</code> 데코레이터와 함께 사용되어, 배열 내 객체의 클래스 타입을 명시하고 그 객체들이 유효한지 검증합니다.</td>
</tr>
</tbody></table>
<h3 id="node_modulesclass-validatortypesdecorator">/node_modules/class-validator/types/decorator</h3>
<ul>
<li>다음 폴더에서 이미 자체적으로 제공되는 validation decorator를 확인해볼 수 있다.</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/a366ac8b-b609-481e-9c34-58c222cb3473/image.png" /></p>
<h2 id="3-custom-validation-decorator-✨">3. custom-validation decorator ✨</h2>
<p>위의 기본 제공 class-validator decorator만으로는 모든 검증을 다 하기 어려운 부분이 있다.
service 단에서 dto의 값을 검증하는 방법이 있겠지만, dto 자체의 문제이므로 나는 dto 단에서 검증을 마치는 것을 선호한다.</p>
<ul>
<li>@ValidatorConstraint 데코레이터를 사용하여 custom validator class를 등록할 수 있다.</li>
<li>@ValidatorConstraint 데코레이터를 사용하면 반드시 ValidatorConstraintInterface를 받아 구현을 진행해야하고, return으로 불리언 타입을 받아 검증을 진행할 수 있다.</li>
</ul>
<pre><code>@ValidatorConstraint({ name: 'IsEvenNumber' })
export class IsEvenNumber implements ValidatorConstraintInterface {
  validate(value: number): boolean {
    if (value {
      return value % 2 === 0
    }
    return false
  }
}

export class SpecificNumber {
  // 짝수인지 체크
  @Validate(IsEvenNumber, { message: 'No Even Number' })
  specificNumber: number
}</code></pre>