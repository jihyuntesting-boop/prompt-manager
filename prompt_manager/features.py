"""메뉴별 기능 함수 모음."""

from prompt_manager.data import create_prompt
from prompt_manager.ui import choose_category, read_nonempty


def add_prompt(prompts):
    """새 프롬프트를 입력받아 리스트에 추가한다. (실행 중에만 유지)"""
    print("\n=== 프롬프트 추가 ===")
    title = read_nonempty("제목: ")
    content = read_nonempty("내용: ")
    category = choose_category()
    prompts.append(create_prompt(title, content, category))
    print("\n프롬프트가 추가되었습니다!")
