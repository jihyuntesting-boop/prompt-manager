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
