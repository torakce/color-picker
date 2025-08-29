import unittest
from app import rgb_to_hsv, add_to_history

class TestColorUtils(unittest.TestCase):
    def test_rgb_to_hsv_red(self):
        h, s, v = rgb_to_hsv(255, 0, 0)
        self.assertAlmostEqual(h, 0.0)
        self.assertAlmostEqual(s, 1.0)
        self.assertAlmostEqual(v, 1.0)

    def test_add_to_history_limit_and_order(self):
        history = []
        colors = [f"#{i}{i}{i}{i}{i}{i}" for i in "012345"]
        for color in colors:
            history = add_to_history(history, color, limit=5)
        expected = ['#555555', '#444444', '#333333', '#222222', '#111111']
        self.assertEqual(history, expected)

if __name__ == '__main__':
    unittest.main()
