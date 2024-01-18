# 먼저 벨로그의 RSS 피드를 파싱하고 깃허브 레포지토리에 커밋하는 파이썬 스크립트를 작성합니다.

# 필요한 라이브러리들을 설명합니다.
# - feedparser: RSS 피드 파싱을 위한 라이브러리
# - git: 깃허브 레포지토리에 액세스하고 커밋하는 데 사용
# - os: 파일 시스템과 상호 작용


import feedparser
import git
import os

# 벨로그 RSS 피드 URL
rss_url = 'https://velog.io/@rimgosu/posts'

# 깃허브 레포지토리 경로
repo_path = 'https://api.velog.io/rss/@rimgosu'

# 레포지토리 로드
repo = git.Repo(repo_path)

# RSS 피드 파싱
feed = feedparser.parse(rss_url)

# 각 글을 파일로 저장하고 커밋
for entry in feed.entries:
    # 파일 이름 생성 (예: 글 제목을 사용)
    file_name = f"{entry.title}.md"
    file_path = os.path.join(repo_path, file_name)

    # 파일이 이미 존재하지 않으면 생성
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(entry.description)  # 글 내용을 파일에 작성

        # 깃허브 커밋
        repo.git.add(file_path)
        repo.git.commit('-m', f'Add post: {entry.title}')

# 변경 사항을 깃허브에 푸시
repo.git.push()