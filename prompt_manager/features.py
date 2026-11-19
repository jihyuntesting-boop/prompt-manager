"""메뉴별 기능 함수 모음."""

from prompt_manager.data import create_prompt
from prompt_manager.ui import choose_category, format_prompt_line, read_nonempty


def add_prompt(prompts):
    """새 프롬프트를 입력받아 리스트에 추가한다. (실행 중에만 유지)"""
    print("\n=== 프롬프트 추가 ===")
    title = read_nonempty("제목: ")
    content = read_nonempty("내용: ")
    category = choose_category()
    prompts.append(create_prompt(title, content, category))
    print("\n프롬프트가 추가되었습니다!")


def show_list(prompts):
    """저장된 모든 프롬프트를 번호와 함께 출력한다."""
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    for number, prompt in enumerate(prompts, start=1):
        print(format_prompt_line(number, prompt))
    print(f"\n총 {len(prompts)}개의 프롬프트")


def filter_by_category(prompts, category):
    """해당 카테고리의 (전체 번호, 프롬프트) 목록을 반환한다."""
    return [
        (number, prompt)
        for number, prompt in enumerate(prompts, start=1)
        if prompt["category"] == category
    ]


def show_by_category(prompts):
    """카테고리를 고르면 해당 카테고리의 프롬프트만 출력한다."""
    print("\n=== 카테고리별 조회 ===")
    category = choose_category()
    results = filter_by_category(prompts, category)
    if not results:
        print(f"\n[{category}] 카테고리에 등록된 프롬프트가 없습니다.")
        return
    print(f"\n[{category}] 카테고리 프롬프트:")
    for number, prompt in results:
        print(format_prompt_line(number, prompt))
    print(f"\n총 {len(results)}개의 프롬프트")


def find_prompts(prompts, keyword):
    """제목 또는 내용에 키워드가 포함된 (전체 번호, 프롬프트) 목록을 반환한다."""
    keyword = keyword.lower()
    return [
        (number, prompt)
        for number, prompt in enumerate(prompts, start=1)
        if keyword in prompt["title"].lower() or keyword in prompt["content"].lower()
    ]


def search_prompt(prompts):
    """키워드를 입력받아 검색 결과를 출력한다."""
    print("\n=== 프롬프트 검색 ===")
    keyword = read_nonempty("검색어: ")
    results = find_prompts(prompts, keyword)
    if not results:
        print("\n검색 결과가 없습니다.")
        return
    print("\n검색 결과:")
    for number, prompt in results:
        print(format_prompt_line(number, prompt))
    print(f"\n{len(results)}개의 프롬프트를 찾았습니다.")


def read_prompt_number(prompts):
    """번호를 입력받아 prompts의 인덱스를 반환한다. 잘못된 입력이면 None."""
    value = input("번호 입력: ").strip()
    if value.isdigit() and 1 <= int(value) <= len(prompts):
        return int(value) - 1
    print("잘못된 번호입니다.")
    return None


def show_detail(prompts):
    """번호로 선택한 프롬프트의 전체 내용을 출력한다."""
    print("\n=== 프롬프트 상세 보기 ===")
    index = read_prompt_number(prompts)
    if index is None:
        return
    prompt = prompts[index]
    prompt["views"] = prompt.get("views", 0) + 1
    line = "─" * 28
    print(f"\n{line}")
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {'⭐' if prompt['favorite'] else '-'}")
    print(f"조회수: {prompt['views']}")
    print(line)
    print("내용:")
    print(prompt["content"])
    print(line)


def toggle_favorite(prompts):
    """번호로 선택한 프롬프트의 즐겨찾기를 추가/해제한다."""
    print("\n=== 즐겨찾기 관리 ===")
    index = read_prompt_number(prompts)
    if index is None:
        return
    prompt = prompts[index]
    prompt["favorite"] = not prompt["favorite"]
    if prompt["favorite"]:
        print(f"'{prompt['title']}' 프롬프트를 즐겨찾기에 추가했습니다!")
    else:
        print(f"'{prompt['title']}' 프롬프트를 즐겨찾기에서 해제했습니다!")


def show_favorites(prompts):
    """즐겨찾기된 프롬프트만 모아서 출력한다."""
    print("\n=== 즐겨찾기 목록 ===")
    favorites = [
        (number, prompt)
        for number, prompt in enumerate(prompts, start=1)
        if prompt["favorite"]
    ]
    if not favorites:
        print("즐겨찾기한 프롬프트가 없습니다.")
        return
    for number, prompt in favorites:
        print(format_prompt_line(number, prompt))
    print(f"\n총 {len(favorites)}개의 즐겨찾기")
