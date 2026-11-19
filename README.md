# 나만의 프롬프트 관리 프로그램

GenAI 미션에서 만든 프롬프트를 카테고리별로 분류하고, 키워드로 검색하고, 즐겨찾기로 관리하는 **Python 콘솔 프로그램**입니다.
파이썬 기초 문법과 Git 워크플로(init, add, commit, push, pull, checkout, clone, merge)를 연습하기 위해 만들었습니다.

외부 라이브러리 없이 표준 라이브러리만 사용합니다.

## 실행 방법

요구 사항: Python 3.10 이상, Git

```bash
git clone <이 저장소 URL>
cd prompt-manager
python main.py        # macOS/Linux에서 python이 없으면 python3 main.py
```

테스트 실행:

```bash
python -m unittest discover -v
```

## 기능 목록

| 메뉴 | 기능 | 설명 |
|---|---|---|
| 1 | 프롬프트 추가 | 제목, 내용, 카테고리를 입력해 등록합니다. 빈 값은 다시 입력받습니다. |
| 2 | 프롬프트 목록 | 모든 프롬프트를 번호, 카테고리, 즐겨찾기(⭐)와 함께 출력합니다. |
| 3 | 카테고리별 조회 | 카테고리를 고르면 해당 카테고리의 프롬프트만 출력합니다. |
| 4 | 프롬프트 검색 | 제목 또는 내용에 키워드가 포함된 프롬프트를 찾습니다. (대소문자 무시) |
| 5 | 프롬프트 상세 보기 | 번호를 입력하면 제목, 카테고리, 즐겨찾기 여부, 전체 내용을 보여줍니다. |
| 6 | 즐겨찾기 관리 | 번호를 입력해 즐겨찾기를 추가/해제합니다. |
| 7 | 즐겨찾기 목록 | 즐겨찾기한 프롬프트만 모아서 출력합니다. |
| 8 | 저장 / 불러오기 / 내보내기 (보너스) | JSON 파일로 저장·불러오기, 카테고리별 Markdown 파일 내보내기 |
| 9 | 수정 / 삭제 (보너스) | 제목·내용·카테고리 수정, 확인 후 삭제 |
| 10 | 조회수 Top 목록 (보너스) | 상세 보기 횟수가 많은 순으로 최대 5개 출력 |
| 0 | 종료 | 프로그램을 종료합니다. |

- 잘못된 번호를 입력하면 안내 메시지를 출력하고 메뉴로 돌아갑니다.
- 목록, 카테고리별 조회, 검색, 즐겨찾기 목록의 번호는 전체 목록 기준이라, 그 번호를 그대로 상세 보기와 즐겨찾기 관리에 사용할 수 있습니다.
- 데이터는 실행 중에만 유지되며, 종료하면 기본 데이터로 초기화됩니다. 8번 메뉴에서 직접 저장했을 때만 `data/prompts.json`에 남습니다.
- 상세 보기(5번)를 열 때마다 해당 프롬프트의 조회수가 1 올라갑니다.

## 프롬프트 카테고리

| 카테고리 | 용도 |
|---|---|
| 텍스트 생성 | 블로그, 이메일 등 글쓰기용 지시문 |
| 이미지 생성 | 이미지 생성용 키워드와 구도 설명 |
| 영상 생성 | 영상 스크립트, 장면 구성 |
| 페르소나 | AI에게 역할을 부여하는 설계안 |
| 자동화 | 요약, 분류 등 반복 업무용 프롬프트 |
| 기타 | 위에 속하지 않는 프롬프트 |

프롬프트를 추가할 때 위 목록에서 번호로 고르거나 새 카테고리 이름을 직접 입력할 수 있습니다.

## 폴더 구조

```text
prompt-manager/
├── main.py                  # 진입점
├── prompt_manager/
│   ├── __init__.py
│   ├── app.py               # 메인 메뉴 루프
│   ├── data.py              # 카테고리, 프롬프트 구조, 기본 데이터
│   ├── features.py          # 필수 기능 함수 (추가/목록/조회/검색/상세/즐겨찾기)
│   ├── bonus.py             # 보너스 기능 (저장 메뉴, 수정/삭제, Top 목록)
│   ├── storage.py           # JSON 저장/불러오기, Markdown 내보내기
│   └── ui.py                # 메뉴 출력, 입력 보조 함수
├── tests/                   # unittest 기반 테스트 (12개)
├── docs/
│   ├── concepts.md          # Python/Git 개념 정리
│   └── screenshots/         # 제출용 스크린샷
├── scripts/
│   └── setup-mac.sh         # macOS 개발 환경 설정 (Git 설정, VSCode 확장)
├── CHECKLIST.md             # 과제 요구사항 체크리스트
├── .gitignore
└── README.md
```

기본으로 등록되는 프롬프트 6개는 이전 미션(회의록 요약 프로젝트, 저장소 `B1-1.ChatGPT-`)에서 작성한 것입니다.

## 프롬프트 데이터 구조

프롬프트는 딕셔너리, 전체 목록은 리스트로 저장합니다.

```python
{
    "title": "블로그 글 작성 도우미",
    "content": "당신은 10년 경력의 전문 블로거입니다...",
    "category": "텍스트 생성",
    "favorite": True,
    "views": 0,  # 보너스: 상세 보기 횟수
}
```

## Git 작업 흐름

- 기능 하나를 완성할 때마다 커밋했습니다. (feat, fix, docs, test, chore 접두어 사용)
- `feature/prompt-list` 브랜치에서 목록 기능을 개발한 뒤 `main`으로 병합했습니다.
- 보너스는 `feature/bonus-storage`, `feature/bonus-crud` 브랜치에서 개발해 `main`으로 병합했습니다.

과제 요구사항별 충족 여부는 [CHECKLIST.md](CHECKLIST.md)에 정리했습니다.

## 제출 자료 (스크린샷)

01~08번 이미지는 클라우드 Linux 환경의 터미널 출력이고, 09~15번은 맥의 VSCode에서 직접 캡처한 화면입니다. 01~08번은 VSCode 화면이 아니며, `git log` 이미지는 촬영 시점까지의 커밋 기록입니다.

| 항목 | 파일 |
|---|---|
| Python/Git 버전, Git 설정 | [01-environment.png](docs/screenshots/01-environment.png) |
| 메뉴, 프롬프트 추가, 목록 | [02-run-add-list.png](docs/screenshots/02-run-add-list.png) |
| 카테고리별 조회, 검색, 상세 보기, 즐겨찾기 | [03-run-category-search-detail-favorites.png](docs/screenshots/03-run-category-search-detail-favorites.png) |
| `git log --oneline --graph` | [04-git-log-graph.png](docs/screenshots/04-git-log-graph.png) |
| 원격 저장소와 브랜치 | [05-remote-branches.png](docs/screenshots/05-remote-branches.png) |
| 공개 샘플 저장소 clone | [06-clone-sample-repo.png](docs/screenshots/06-clone-sample-repo.png) |
| 보너스 기능 실행 | [07-run-bonus.png](docs/screenshots/07-run-bonus.png) |
| 단위 테스트 | [08-unit-tests.png](docs/screenshots/08-unit-tests.png) |
| 맥 VSCode: git log 그래프 | [09-vscode-git-log-graph.jpg](docs/screenshots/09-vscode-git-log-graph.jpg) |
| 맥 VSCode: 확장 설치 | [10-vscode-extensions.jpg](docs/screenshots/10-vscode-extensions.jpg) |
| 맥 VSCode: 버전과 Git 설정 | [11-vscode-versions-git-config.png](docs/screenshots/11-vscode-versions-git-config.png) |
| 맥 VSCode: GitHub 로그인 | [12-vscode-github-login.png](docs/screenshots/12-vscode-github-login.png) |
| 맥 터미널: 프로그램 실행 (입력 시행착오 포함) | [13-macos-program-run.jpg](docs/screenshots/13-macos-program-run.jpg) |
| 맥 터미널: 메뉴, 목록, 프롬프트 추가 | [14-macos-run-menu-add-list.jpg](docs/screenshots/14-macos-run-menu-add-list.jpg) |
| 맥 터미널: 추가 결과(7개), 검색, 종료 | [15-macos-run-add-list-search-exit.jpg](docs/screenshots/15-macos-run-add-list-search-exit.jpg) |
