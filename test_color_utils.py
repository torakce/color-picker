import unittest
from app import rgb_to_hsv, ColorHistory

class TestColorUtils(unittest.TestCase):
    def test_rgb_to_hsv_red(self):
        h, s, v = rgb_to_hsv(255, 0, 0)
        self.assertAlmostEqual(h, 0.0)
        self.assertAlmostEqual(s, 1.0)
        self.assertAlmostEqual(v, 1.0)

    def test_color_history_order(self):
        history = ColorHistory()
        history.add("#ffffff")
        history.add("#000000")
        self.assertEqual(history.colors, ["#000000", "#ffffff"])

if __name__ == '__main__':
    unittest.main()
