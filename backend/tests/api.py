import requests
import unittest


class TestApi(unittest.TestCase):

    def test_index(self):
        res = requests.get("http://localhost:7082/")
        self.assertTrue(res.ok)

    def test_get_all_data(self):
        res = requests.get("http://localhost:7082/get-all-data/tmpkey")
        self.assertTrue(res.ok)

    def test_get_ski_area(self):
        res = requests.post("http://localhost:7082/get-ski-area",
                            data={"skiareaname": "Snowbird",
                                  "api_key": "tmpkey"
                                  })


if __name__ == "__main__":
    unittest.main()
