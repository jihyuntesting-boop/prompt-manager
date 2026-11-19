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
