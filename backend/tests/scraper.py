from snow_data import resort_scraper, const
import unittest


class TestResortScraper(unittest.TestCase):

    def test_resort(self):
        # loop through all the ski areas and check that they return data
        for ski_area in const.SKI_AREAS:
            data = resort_scraper.get_data(ski_area)
            self.assertTrue(data)


if __name__ == "__main__":
    unittest.main()