"""화면 출력과 사용자 입력을 담당하는 보조 함수."""

from prompt_manager.data import CATEGORIES


def show_menu():
    """메인 메뉴를 출력한다."""
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("8. 저장 / 불러오기 / 내보내기 (보너스)")
    print("0. 종료")


def format_prompt_line(number, prompt):
    """목록에 표시할 한 줄 문자열을 만든다."""
    star = " ⭐" if prompt["favorite"] else ""
    return f"{number}. [{prompt['category']}] {prompt['title']}{star}"


def read_nonempty(label):
    """비어 있지 않은 값을 입력받을 때까지 반복해서 묻는다."""
    while True:
        value = input(label).strip()
        if value:
            return value
        print("값을 입력해주세요.")


def choose_category():
    """카테고리 목록에서 번호로 고르거나 직접 입력받아 카테고리 이름을 반환한다."""
    print("\n카테고리 선택:")
    for number, name in enumerate(CATEGORIES, start=1):
        print(f"{number}) {name}")
    while True:
        value = input("선택 (번호 또는 직접 입력): ").strip()
        if value.isdigit() and 1 <= int(value) <= len(CATEGORIES):
            return CATEGORIES[int(value) - 1]
        if value and not value.isdigit():
            return value
        print("올바른 번호 또는 카테고리 이름을 입력해주세요.")
