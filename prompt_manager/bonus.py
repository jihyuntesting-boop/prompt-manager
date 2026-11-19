"""보너스 기능: 저장/내보내기 메뉴, 수정/삭제, 조회수 Top 목록."""

from prompt_manager.storage import (
    DEFAULT_EXPORT_DIR,
    DEFAULT_JSON_PATH,
    export_markdown,
    load_prompts,
    save_prompts,
)


def save_to_json(prompts):
    """현재 프롬프트를 JSON 파일로 저장한다."""
    path = save_prompts(prompts)
    print(f"{len(prompts)}개의 프롬프트를 저장했습니다: {path}")


def load_from_json(prompts):
    """JSON 파일에서 프롬프트를 불러와 현재 목록을 교체한다."""
    try:
        loaded = load_prompts()
    except ValueError as error:
        print(error)
        return
    if loaded is None:
        print(f"저장된 파일이 없습니다: {DEFAULT_JSON_PATH}")
        return
    prompts[:] = loaded
    print(f"{len(prompts)}개의 프롬프트를 불러왔습니다.")


def export_to_markdown(prompts):
    """카테고리별 Markdown 파일로 내보낸다."""
    if not prompts:
        print("내보낼 프롬프트가 없습니다.")
        return
    paths = export_markdown(prompts)
    print(f"{len(paths)}개의 Markdown 파일을 만들었습니다: {DEFAULT_EXPORT_DIR}")
    for path in paths:
        print(f"- {path.name}")


def manage_storage(prompts):
    """저장 / 불러오기 / 내보내기 하위 메뉴."""
    print("\n=== 저장 / 불러오기 / 내보내기 ===")
    print("1. JSON으로 저장")
    print("2. JSON에서 불러오기")
    print("3. 카테고리별 Markdown 내보내기")
    print("0. 돌아가기")
    actions = {"1": save_to_json, "2": load_from_json, "3": export_to_markdown}
    choice = input("선택: ").strip()
    if choice == "0":
        return
    action = actions.get(choice)
    if action is None:
        print("잘못된 번호입니다.")
        return
    action(prompts)


def top_prompts(prompts, limit=5):
    """조회수가 많은 순(같으면 번호 순)으로 (전체 번호, 프롬프트) 목록을 반환한다."""
    numbered = list(enumerate(prompts, start=1))
    numbered.sort(key=lambda item: (-item[1].get("views", 0), item[0]))
    return numbered[:limit]


def show_top(prompts):
    """조회수 Top 목록을 출력한다."""
    print("\n=== 조회수 Top 5 ===")
    viewed = [(n, p) for n, p in top_prompts(prompts) if p.get("views", 0) > 0]
    if not viewed:
        print("아직 조회된 프롬프트가 없습니다. 상세 보기(5번)를 먼저 이용해보세요.")
        return
    for rank, (number, prompt) in enumerate(viewed, start=1):
        print(f"{rank}위. (번호 {number}) {prompt['title']} - 조회수 {prompt['views']}")
