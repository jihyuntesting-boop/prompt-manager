import unittest

from prompt_manager.data import CATEGORIES, create_prompt, get_default_prompts
from prompt_manager.features import filter_by_category, find_prompts


class DefaultDataTest(unittest.TestCase):
    def test_at_least_three_defaults_with_required_keys(self):
        prompts = get_default_prompts()
        self.assertGreaterEqual(len(prompts), 3)
        for prompt in prompts:
            self.assertEqual(set(prompt), {"title", "content", "category", "favorite", "views"})
            self.assertIn(prompt["category"], CATEGORIES)

    def test_create_prompt_defaults_favorite_false(self):
        self.assertFalse(create_prompt("t", "c", "기타")["favorite"])


class FilterAndSearchTest(unittest.TestCase):
    def setUp(self):
        self.prompts = get_default_prompts()

    def test_filter_by_category_keeps_global_number(self):
        results = filter_by_category(self.prompts, "영상 생성")
        self.assertEqual([number for number, _ in results], [3])

    def test_filter_empty_category(self):
        self.assertEqual(filter_by_category(self.prompts, "기타"), [])

    def test_find_prompts_matches_title_or_content_case_insensitive(self):
        self.assertEqual(len(find_prompts(self.prompts, "블로그")), 1)
        self.assertEqual(len(find_prompts(self.prompts, "seo")), 1)

    def test_find_prompts_no_result(self):
        self.assertEqual(find_prompts(self.prompts, "존재하지않는검색어"), [])


if __name__ == "__main__":
    unittest.main()
