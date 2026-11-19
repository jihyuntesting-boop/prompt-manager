# 과제 체크리스트: Python & Git 기초

범례: ✅ 완료하고 검증함 · ⚠️ 일부만 충족하거나 사용자 확인이 필요함 · ❌ 이 환경에서는 할 수 없어 사용자 PC에서 해야 함

저장소: https://github.com/jihyuntesting-boop/prompt-manager

## 1. 최종 결과물

| 상태 | 항목 | 근거 |
|---|---|---|
| ✅ | 메뉴 번호로 기능을 선택하는 콘솔 프로그램 | `python main.py`, 스크린샷 02 |
| ✅ | 추가, 목록, 카테고리별 조회, 검색, 상세 보기, 즐겨찾기 동작 | 스크린샷 02, 03 |
| ✅ | 실행 중 추가한 프롬프트와 즐겨찾기 유지, 종료 시 초기화 | 메모리 리스트만 사용. 8번 메뉴로 직접 저장할 때만 파일 생성 |
| ✅ | 이전 미션 프롬프트 3개 이상을 기본 데이터로 등록 | 이전 미션 저장소 `B1-1.ChatGPT-`(회의록 요약 프로젝트)의 프롬프트 6개를 등록 (`prompt_manager/data.py`) |
| ✅ | 프로젝트 코드가 GitHub에 업로드됨 | 위 저장소 URL |
| ✅ | 기능 단위 커밋 10개 이상 | `git rev-list --count main` (수십 개), 스크린샷 04 |
| ✅ | 브랜치 생성 및 병합 기록 | `feature/prompt-list`, `feature/bonus-storage`, `feature/bonus-crud`를 `checkout -b`로 만들고 `merge --no-ff`로 병합 |
| ✅ | README에 설명과 실행 방법 | `README.md` |
| ✅ | 함수로 기능별 코드 분리 | `prompt_manager/` 패키지 (app, data, features, bonus, storage, ui) |

## 2. 제출물

| 상태 | 항목 | 근거 |
|---|---|---|
| ✅ | GitHub 저장소 URL | https://github.com/jihyuntesting-boop/prompt-manager |
| ❌ | 개발 환경 설정 스크린샷 (**VSCode**, Python 버전, Git 설정) | Python/Git 버전과 설정은 `docs/screenshots/01-environment.png`(클라우드 터미널)로 대체. **VSCode 화면은 사용자 PC에서 직접 캡처 필요** |
| ⚠️ | 프로그램 실행 결과 스크린샷 | 클라우드 터미널 출력 이미지 02, 03, 07. 사용자 PC에서 실행한 화면이 필요하면 다시 캡처 |
| ⚠️ | `git log --oneline --graph` 스크린샷 | `docs/screenshots/04-git-log-graph.png` (촬영 시점까지). 사용자 PC에서 clone 후 캡처하면 더 좋음 |

## 3. 과제 목표 (스스로 설명할 수 있어야 함)

| 상태 | 항목 | 근거 |
|---|---|---|
| ❌ | VSCode에서 Python 파일을 만들고 실행 | 사용자 PC에서 직접 수행 |
| ✅ | 터미널에서 Python/Git 버전 확인과 설정 점검 | 스크린샷 01 |
| ✅ | 파이썬 기초 문법 설명 자료 | `docs/concepts.md` |
| ✅ | Git이 무엇이고 왜 필요한지 설명 자료 | `docs/concepts.md` |
| ✅ | init, add, commit, push, pull, checkout, clone, merge 설명 자료 | `docs/concepts.md` |
| ✅ | 브랜치 생성과 병합 | 스크린샷 04 |
| ✅ | GitHub에 코드 업로드와 관리 | 저장소, 스크린샷 05 |

설명 자료는 제공했지만 "스스로 설명할 수 있는지"는 학습자가 직접 읽고 익혀야 합니다.

## 4. 기능 요구 사항

### 4-1. 개발 환경

| 상태 | 항목 | 근거 |
|---|---|---|
| ❌ | VSCode에 Python 확장 설치 | 사용자 PC에서 수행 |
| ❌ | VSCode Korean Language Pack 설치 (선택) | 사용자 PC에서 수행 |
| ✅ | Python 3.10 이상 확인 | 스크린샷 01 (Python 3.13) |
| ✅ | `print("Hello")` 실행 | 스크린샷 01 |
| ✅ | Git 버전 확인 | 스크린샷 01 |
| ⚠️ | Git 사용자 정보(이름, 이메일) 설정 | 이 저장소에 로컬로 설정함. **사용자 PC의 Git에는 별도 설정 필요** |
| ⚠️ | 기본 브랜치 이름 main | 이 저장소는 `main` 사용, `init.defaultBranch=main` 설정함. 사용자 PC는 `git config --global init.defaultBranch main` |
| ❌ | VSCode에서 GitHub 로그인과 연동 확인 | 사용자 PC에서 수행 |

### 4-2. Git 저장소 설정 및 초기화

| 상태 | 항목 | 근거 |
|---|---|---|
| ✅ | GitHub에 새 저장소 생성 | `prompt-manager` (사용자가 생성) |
| ✅ | 로컬에서 `init`으로 저장소 시작 | `git init -b main`, 첫 커밋 `chore: init repository with .gitignore` |
| ✅ | 원격 연결, 첫 커밋과 푸시 | `git remote add origin`, `git push -u origin main`, 스크린샷 05 |
| ✅ | `.gitignore` 작성 | `.gitignore` |
| ✅ | README.md에 프로젝트 제목 | 두 번째 커밋 `docs: add README with project title` |
| ✅ | 공개 샘플 저장소를 `clone`해 구조와 로그 확인 | `octocat/Hello-World`, 스크린샷 06 (확인 후 삭제함) |

### 4-3. 프로그램 실행 및 메뉴

| 상태 | 항목 | 근거 |
|---|---|---|
| ✅ | 실행 시 메뉴 출력 | 스크린샷 02 |
| ✅ | 번호 입력으로 기능 선택 | `app.py`의 `handlers` 딕셔너리 |
| ✅ | 잘못된 번호는 안내 후 메뉴 재출력 | 스크린샷 03 마지막 부분 |
| ✅ | "종료" 선택 시 종료 | 메뉴 0 |
| ✅ | 각 기능 후 메뉴로 복귀 | 메인 `while` 루프 |

### 4-4. 기본 프롬프트 데이터

| 상태 | 항목 | 근거 |
|---|---|---|
| ✅ | 이전 미션 프롬프트 3개 이상 미리 등록 | 6개 등록 (회의록 정리 v1, 입력 템플릿, 미노 페르소나 v2, few-shot 예시, 임원 보고용 변환, 모델 비교용 입력) |
| ✅ | 리스트와 딕셔너리로 저장 | `data.py`의 `create_prompt`, `get_default_prompts` |
| ✅ | 제목, 내용, 카테고리, 즐겨찾기 여부 포함 | `tests/test_features.py` (보너스로 `views` 추가) |
| ✅ | 카테고리 예시 6종 | `CATEGORIES` |

### 4-5. 프롬프트 추가

| 상태 | 항목 | 근거 |
|---|---|---|
| ✅ | 새 프롬프트 등록 | 메뉴 1 |
| ✅ | 제목, 내용, 카테고리 입력 | `add_prompt` |
| ✅ | 빈 입력이면 재요청 | `read_nonempty` |
| ✅ | 카테고리를 목록에서 선택하거나 직접 입력 | `choose_category` |
| ✅ | 리스트에 저장 (실행 중에만 유지) | `prompts.append` |
| ✅ | 즐겨찾기 기본값 False | 테스트 `test_create_prompt_defaults_favorite_false` |

### 4-6. 프롬프트 목록 (브랜치 활용)

| 상태 | 항목 | 근거 |
|---|---|---|
| ✅ | main 이외의 브랜치에서 작업 | `feature/prompt-list` |
| ✅ | 모든 프롬프트를 번호와 함께 출력 | `show_list`, 스크린샷 02 |
| ✅ | 제목, 카테고리, 즐겨찾기(⭐) 표시 | `format_prompt_line` |
| ✅ | 비어 있으면 안내 메시지 | `show_list`의 빈 목록 처리 |
| ✅ | 커밋 후 main에 병합 (checkout, merge) | 스크린샷 04의 병합 그래프 |

### 4-7 ~ 4-10. 조회, 검색, 상세, 즐겨찾기

| 상태 | 항목 | 근거 |
|---|---|---|
| ✅ | 카테고리 목록 선택 후 해당 카테고리만 출력 | 스크린샷 03, 테스트 |
| ✅ | 카테고리에 프롬프트가 없으면 안내 | `show_by_category` |
| ✅ | 키워드로 제목 또는 내용 검색 (대소문자 무시) | 스크린샷 03, 테스트 |
| ✅ | 검색 결과 목록 출력, 없으면 안내 | `search_prompt` |
| ✅ | 번호 입력으로 전체 내용 출력 (제목, 카테고리, 즐겨찾기, 내용) | `show_detail`, 스크린샷 03 |
| ✅ | 잘못된 번호는 안내 | `read_prompt_number` |
| ✅ | 즐겨찾기 추가/해제 | `toggle_favorite` |
| ✅ | 즐겨찾기만 모아 보기 | `show_favorites` |

### 4-11 ~ 4-12. 코드 구조와 README

| 상태 | 항목 | 근거 |
|---|---|---|
| ✅ | 한 함수에 몰아 넣지 않음, 기능별 함수 분리 | `show_menu`, `add_prompt`, `show_list`, `search_prompt`, `show_favorites` 등 |
| ✅ | README: 이름과 설명 | `README.md` |
| ✅ | README: 실행 방법 | `README.md` |
| ✅ | README: 기능 목록 | `README.md` |
| ✅ | README: 카테고리 설명 | `README.md` |

## 5. 보너스 과제 (선택)

| 상태 | 항목 | 근거 |
|---|---|---|
| ✅ | JSON 파일로 저장/불러오기 | 메뉴 8, `storage.py`, 스크린샷 07, 테스트 |
| ✅ | 카테고리별 Markdown 파일로 내보내기 | 메뉴 8, `exports/`, 테스트 |
| ✅ | 프롬프트 수정/삭제 | 메뉴 9, 스크린샷 07 |
| ✅ | 상세 보기 시 조회수 기록 | `show_detail`, 스크린샷 07 |
| ✅ | 조회수 기준 Top 목록 | 메뉴 10, 테스트 |

## 6. 제약 사항

| 상태 | 항목 | 근거 |
|---|---|---|
| ✅ | Python 3.10 이상 | 실행 환경 3.13. 코드는 3.10 문법만 사용 |
| ✅ | 필수 요구사항은 외부 라이브러리 없이 기본 문법만 사용 | 표준 라이브러리(`json`, `pathlib`, `unittest`)만 사용, 설치할 패키지 없음 |
| ✅ | 10개 이상의 의미 있는 커밋 | `feat`, `fix`, `docs`, `test`, `chore` 접두어로 변경 의도를 설명 |
| ✅ | init, add, commit, push, pull, checkout, clone, merge 각 1회 이상 | init(저장소 생성), add/commit(전체 이력), push(원격 반영), pull(`Already up to date` 확인), checkout(브랜치 생성/이동), clone(샘플 저장소), merge(`--no-ff` 병합 3회) |
| ✅ | 브랜치 생성 및 병합을 로컬 checkout, merge로 수행 | 스크린샷 04 |
| ✅ | 이전 미션 프롬프트 3개 이상을 기본 데이터로 등록 | 위와 동일 (6개) |

## 남은 할 일 (사용자 PC에서)

VSCode와 PC의 Git 설정은 이 클라우드 환경에서 만질 수 없어 PC에서 해야 합니다. 설치와 설정은 스크립트 한 번으로 끝나도록 준비했습니다. (Windows PowerShell, 이 환경에는 PowerShell이 없어 **스크립트는 실행해 보지 못했습니다**)

```powershell
git clone https://github.com/jihyuntesting-boop/prompt-manager
cd prompt-manager
.\scripts\setup-windows.ps1 -Name "GitHub사용자명" -Email "GitHub에 등록한 이메일"
```

1. 위 스크립트로 Python 확장, Korean Language Pack 설치와 Git 사용자 정보, 기본 브랜치 설정을 한 번에 처리
2. VSCode 왼쪽 아래 계정 아이콘에서 GitHub 로그인(브라우저 승인 필요), 로그인된 화면 캡처
3. `python main.py` 실행 화면과 `git log --oneline --graph` 화면 캡처 (클라우드 터미널 이미지 대신 PC 화면을 내려면)
