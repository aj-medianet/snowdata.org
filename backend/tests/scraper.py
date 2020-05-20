from scraper import resort_scraper
import unittest


class TestResortScraper(unittest.TestCase):

    def test_resort(self):
        data = resort_scraper.get_data("mt_bachelor")
        self.assertTrue(data)


if __name__ == "__main__":
    unittest.main()