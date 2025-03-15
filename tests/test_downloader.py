import unittest
from src.downloader import Aria2Downloader

class TestAria2Downloader(unittest.TestCase):
    def setUp(self):
        """ Setup before each test """
        self.downloader = Aria2Downloader()

    def test_add_download(self):
        """ Test adding a download """
        url = "https://example.com/sample.zip"
        response = self.downloader.add_download(url)
        self.assertIsInstance(response, dict)

    def test_pause_download(self):
        """ Test pausing a download (Mock GID) """
        gid = "12345"
        response = self.downloader.pause_download(gid)
        self.assertIsInstance(response, dict)

    def test_resume_download(self):
        """ Test resuming a download """
        gid = "12345"
        response = self.downloader.resume_download(gid)
        self.assertIsInstance(response, dict)

    def test_remove_download(self):
        """ Test removing a download """
        gid = "12345"
        response = self.downloader.remove_download(gid)
        self.assertIsInstance(response, dict)

if __name__ == "__main__":
    unittest.main()
