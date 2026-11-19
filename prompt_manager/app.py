"""메인 메뉴 루프."""

from prompt_manager.data import get_default_prompts
from prompt_manager.features import add_prompt, search_prompt, show_by_category, show_list
from prompt_manager.ui import show_menu


def run():
    """프로그램을 실행한다. 0을 선택하면 종료한다."""
    prompts = get_default_prompts()
    handlers = {
        "1": add_prompt,
        "2": show_list,
        "3": show_by_category,
        "4": search_prompt,
    }

    while True:
        show_menu()
        choice = input("선택: ").strip()
        if choice == "0":
            print("프로그램을 종료합니다.")
            break
        handler = handlers.get(choice)
        if handler is None:
            print("잘못된 번호입니다. 메뉴에 있는 번호를 입력해주세요.")
            continue
        handler(prompts)
