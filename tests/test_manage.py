import unittest
from src.manager import DownloadManager

class TestDownloadManager(unittest.TestCase):
    def setUp(self):
        """ Setup before each test """
        self.manager = DownloadManager()

    def test_categorize_file(self):
        """ Test file categorization """
        self.assertEqual(self.manager.categorize_file("video.mp4"), "videos")
        self.assertEqual(self.manager.categorize_file("document.pdf"), "documents")
        self.assertEqual(self.manager.categorize_file("unknown.xyz"), "others")

    def test_add_to_queue(self):
        """ Test adding to queue """
        self.manager.add_to_queue("https://example.com/file.zip", "file.zip")
        self.assertEqual(len(self.manager.queue), 1)

if __name__ == "__main__":
    unittest.main()
