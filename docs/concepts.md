# Python / Git 개념 정리

## Git이란, 왜 필요한가
Git은 파일의 변경 이력을 저장하는 **분산 버전 관리 시스템**입니다. 변경을 커밋 단위로 기록하므로 이전 상태로 되돌리거나, 브랜치로 기능을 분리해 개발하거나, 여러 사람이 같은 프로젝트를 함께 작업할 수 있습니다. GitHub는 Git 저장소를 인터넷에 올려 공유하는 호스팅 서비스입니다.

## 이번 과제에서 쓴 Git 명령

| 명령 | 하는 일 | 이 프로젝트에서의 사용 |
|---|---|---|
| `git init` | 현재 폴더를 새 Git 저장소로 만든다 | `git init -b main`으로 시작 |
| `git add` | 변경 파일을 커밋 대기 영역(스테이징)에 올린다 | 기능 단위로 `git add` |
| `git commit` | 스테이징된 변경을 이력으로 저장한다 | 기능마다 커밋 |
| `git push` | 로컬 커밋을 원격 저장소(GitHub)로 보낸다 | `git push -u origin main` |
| `git pull` | 원격의 새 커밋을 가져와 로컬에 합친다 | 푸시 후 `git pull`로 동기화 확인 |
| `git checkout` | 브랜치를 바꾸거나(`-b`로 새로 만들며) 이동한다 | `git checkout -b feature/prompt-list` |
| `git clone` | 원격 저장소를 통째로 내려받는다 | 공개 샘플 `octocat/Hello-World` 확인 |
| `git merge` | 다른 브랜치의 변경을 현재 브랜치에 합친다 | `git merge --no-ff feature/prompt-list` |

## 브랜치와 병합
브랜치는 독립된 작업 줄기입니다. `main`을 건드리지 않고 `feature/...` 브랜치에서 기능을 만든 뒤, 완성되면 `main`으로 병합합니다. `--no-ff`를 쓰면 병합 커밋이 남아 `git log --graph`에서 분기와 합류가 보입니다.

## 이 프로젝트에 쓰인 Python 기초 문법

| 문법 | 사용 위치 |
|---|---|
| 변수, 문자열, f-string | 모든 출력 (`f"{number}. [{category}] {title}"`) |
| 리스트 | `prompts` (프롬프트 전체), `CATEGORIES` |
| 딕셔너리 | 프롬프트 1개 (`title`, `content`, `category`, `favorite`) |
| 조건문 `if` / `elif` / `else` | 입력 검증, 즐겨찾기 표시 |
| 반복문 `for`, `while` | 목록 출력, 메뉴 루프, 빈 입력 재요청 |
| 함수 `def`, 반환값 | 기능별 분리 (`add_prompt`, `show_list` 등) |
| 리스트 컴프리헨션 | 카테고리 필터, 검색 |
| `enumerate` | 번호 매기기 |
| 모듈과 `import` | `prompt_manager` 패키지 분리 |
| `try` / `except` | JSON 불러오기 오류 처리, Ctrl+C 종료 |
| `if __name__ == "__main__"` | 진입점 `main.py` |
