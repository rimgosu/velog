<h1 id="greedot-todo">greedot TODO</h1>
<h2 id="지금까지-한-것">지금까지 한 것</h2>
<ul>
<li>fast api 공부</li>
<li>db 설계<pre><code>from sqlalchemy import create_engine
</code></pre></li>
</ul>
<p>from sqlalchemy import create_engine, Column, Integer, String, Date, Enum, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from enum import unique, Enum as PyEnum</p>
<p>Base = declarative_base()</p>
<p>@unique
class RoleEnum(PyEnum):
    ADMIN = &quot;ADMIN&quot;
    MANAGER = &quot;MANAGER&quot;
    MEMBER = &quot;MEMBER&quot;</p>
<p>@unique
class StatusEnum(PyEnum):
    ACTIVATE = &quot;ACTIVATE&quot;
    DISABLED = &quot;DISABLED&quot;</p>
<p>@unique
class GradeEnum(PyEnum):
    FREE = &quot;FREE&quot;
    BASIC = &quot;BASIC&quot;
    PREMIUM = &quot;PREMIUM&quot;</p>
<p>@unique
class LogTypeEnum(PyEnum):
    SENDTALK = &quot;SENDTALK&quot;
    RECEIVEDTALK = &quot;RECEIVEDTALK&quot;
    CLICKED = &quot;CLICKED&quot;</p>
<p>@unique
class LogTypeEnum(PyEnum):
    SENDTALK = &quot;SENDTALK&quot;
    RECEIVEDTALK = &quot;RECEIVEDTALK&quot;
    CLICKED = &quot;CLICKED&quot;</p>
<p>class Member(Base):
    <strong>tablename</strong> = 'member'</p>
<pre><code>id = Column('member_id', Integer, primary_key=True, autoincrement=True)
email = Column(String(255), nullable=False)
nickname = Column(String(255), nullable=False)
password = Column(String(255), nullable=False)
role = Column(Enum(RoleEnum), nullable=False)
status = Column(Enum(StatusEnum), nullable=False)
grade = Column(Enum(GradeEnum), nullable=False)
register_at = Column(Date, nullable=False)

gree = relationship(&quot;Gree&quot;, back_populates=&quot;member&quot;)
logs = relationship(&quot;Logs&quot;, back_populates=&quot;member&quot;)</code></pre><p>class Gree(Base):
    <strong>tablename</strong> = 'gree'</p>
<pre><code>id = Column('gree_id', Integer, primary_key=True, autoincrement=True)
member_id = Column(Integer, ForeignKey('member.member_id'), nullable=False)
gree_name = Column(String(255), nullable=False)
root_path = Column(String(255), nullable=False)
prompt_character = Column(String(255))  # Should be a relationship if it's an enum
prompt_age = Column(Integer)
prompt_mbti = Column(String(255))  # Should be a relationship if it's an enum
register_at = Column(Date, nullable=False)

member = relationship(&quot;Member&quot;, back_populates=&quot;gree&quot;)
logs = relationship(&quot;Logs&quot;, back_populates=&quot;gree&quot;)</code></pre><p>class Logs(Base):
    <strong>tablename</strong> = 'logs'</p>
<pre><code>id = Column('log_id', Integer, primary_key=True, autoincrement=True)
gree_id = Column(Integer, ForeignKey('gree.gree_id'), nullable=False)
member_id = Column(Integer, ForeignKey('member.member_id'), nullable=False)
log_type = Column(Enum(LogTypeEnum), nullable=False)
talk = Column(String(255))
register_at = Column(Date, nullable=False)

member = relationship(&quot;Member&quot;, back_populates=&quot;logs&quot;)
gree = relationship(&quot;Gree&quot;, back_populates=&quot;logs&quot;)</code></pre><h1 id="데이터베이스-설정">데이터베이스 설정</h1>
<p>SERVER_HOST = &quot;database-1.c3mqckcawht2.ap-southeast-2.rds.amazonaws.com&quot;
USERNAME = &quot;admin&quot;
PASSWORD = &quot;63814110&quot;
DATABASE_NAME = &quot;greedot&quot;</p>
<h1 id="sqlalchemy-엔진-생성">SQLAlchemy 엔진 생성</h1>
<p>engine = create_engine(f&quot;mysql+pymysql://{USERNAME}:{PASSWORD}@{SERVER_HOST}/{DATABASE_NAME}&quot;)</p>
<h1 id="데이터베이스에-테이블-생성">데이터베이스에 테이블 생성</h1>
<p>Base.metadata.create_all(engine)</p>
<p>```</p>
<p><img alt="" src="https://velog.velcdn.com/images/rimgosu/post/760be126-b4d3-44e0-9d8b-e6f3de9a4320/image.png" /></p>
<h2 id="todo">TODO</h2>
<ul>
<li>sqlalchemy 공부</li>
<li>1대N 관계 제대로 매핑할 것</li>
</ul>