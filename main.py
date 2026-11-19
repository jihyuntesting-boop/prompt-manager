"""프로그램 진입점. 실행: python main.py"""

from prompt_manager.app import run

if __name__ == "__main__":
    try:
        run()
    except (KeyboardInterrupt, EOFError):
        print("\n프로그램을 종료합니다.")
