from src.utils import format_size
import unittest

class TestUtils(unittest.TestCase):
    def test_format_size(self):
        self.assertEqual(format_size(1024), "1.00 KB")
        self.assertEqual(format_size(1048576), "1.00 MB")

if __name__ == "__main__":
    unittest.main()
