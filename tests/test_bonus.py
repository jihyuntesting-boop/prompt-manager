import unittest

from prompt_manager.bonus import top_prompts
from prompt_manager.data import get_default_prompts


class TopPromptsTest(unittest.TestCase):
    def test_sorted_by_views_then_number(self):
        prompts = get_default_prompts()
        prompts[2]["views"] = 5
        prompts[4]["views"] = 5
        prompts[1]["views"] = 9
        numbers = [number for number, _ in top_prompts(prompts, limit=3)]
        self.assertEqual(numbers, [2, 3, 5])

    def test_limit(self):
        self.assertEqual(len(top_prompts(get_default_prompts(), limit=2)), 2)


if __name__ == "__main__":
    unittest.main()
