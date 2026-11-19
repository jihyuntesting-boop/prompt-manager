"""보너스 1: JSON 저장/불러오기와 Markdown 내보내기."""

import json
from pathlib import Path

from prompt_manager.data import create_prompt

BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_JSON_PATH = BASE_DIR / "data" / "prompts.json"
DEFAULT_EXPORT_DIR = BASE_DIR / "exports"


def save_prompts(prompts, path=DEFAULT_JSON_PATH):
    """프롬프트 전체를 JSON 파일로 저장하고 저장 경로를 반환한다."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(prompts, file, ensure_ascii=False, indent=2)
    return path


def load_prompts(path=DEFAULT_JSON_PATH):
    """JSON 파일에서 프롬프트를 불러온다. 파일이 없으면 None, 형식이 잘못되면 ValueError."""
    path = Path(path)
    if not path.exists():
        return None
    try:
        with open(path, encoding="utf-8") as file:
            raw = json.load(file)
        return [
            create_prompt(
                item["title"],
                item["content"],
                item["category"],
                bool(item.get("favorite", False)),
                int(item.get("views", 0)),
            )
            for item in raw
        ]
    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        raise ValueError(f"JSON 형식이 올바르지 않습니다: {error}") from error


def safe_filename(name):
    """파일 이름에 쓸 수 없는 문자를 밑줄로 바꾼다."""
    return "".join("_" if ch in '\\/:*?"<>|' else ch for ch in name).strip() or "기타"


def export_markdown(prompts, directory=DEFAULT_EXPORT_DIR):
    """카테고리별 Markdown 파일을 만들고 생성한 파일 경로 목록을 반환한다."""
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    grouped = {}
    for prompt in prompts:
        grouped.setdefault(prompt["category"], []).append(prompt)

    paths = []
    for category, items in grouped.items():
        lines = [f"# {category}", ""]
        for prompt in items:
            star = " ⭐" if prompt["favorite"] else ""
            lines += [f"## {prompt['title']}{star}", "", prompt["content"], ""]
        path = directory / f"{safe_filename(category)}.md"
        path.write_text("\n".join(lines), encoding="utf-8")
        paths.append(path)
    return paths
