import tempfile
import unittest
from pathlib import Path

from prompt_manager.data import get_default_prompts
from prompt_manager.storage import export_markdown, load_prompts, save_prompts


class StorageTest(unittest.TestCase):
    def test_save_and_load_roundtrip(self):
        prompts = get_default_prompts()
        with tempfile.TemporaryDirectory() as tmp:
            path = save_prompts(prompts, Path(tmp) / "nested" / "p.json")
            self.assertEqual(load_prompts(path), prompts)

    def test_load_missing_file_returns_none(self):
        self.assertIsNone(load_prompts("/nonexistent/prompts.json"))

    def test_load_invalid_json_raises_value_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "bad.json"
            bad.write_text("{not json", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_prompts(bad)

    def test_export_markdown_one_file_per_category(self):
        prompts = get_default_prompts()
        with tempfile.TemporaryDirectory() as tmp:
            paths = export_markdown(prompts, tmp)
            self.assertEqual(len(paths), len({p["category"] for p in prompts}))
            text = (Path(tmp) / "텍스트 생성.md").read_text(encoding="utf-8")
            self.assertIn("회의록 정리 요청 (v1) ⭐", text)


if __name__ == "__main__":
    unittest.main()
