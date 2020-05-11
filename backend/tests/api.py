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
                            data={
                                "skiareaname": "Snowbird",
                                "api_key": "tmpkey"
                            })
        self.assertTrue(res.ok)

    def test_create_user(self):
        res = requests.post("http://localhost:7082/create-user",
                            data={
                                "username": "andrew",
                                "email": "andrew@aj-media.net",
                                "password": "temppassword"
                            })
        self.assertTrue(res.ok)

    def test_login(self):
        res = requests.post("http://localhost:7082/login",
                            data={
                                "username": "andrew",
                                "password": "temppassword"
                            })
        self.assertTrue(res.ok)

    def test_logout(self):
        res = requests.post("http://localhost:7082/logout",
                            data={
                                "username": "andrew",
                            })
        self.assertTrue(res.ok)

    def test_get_api_key(self):
        res = requests.post("http://localhost:7082/get-api-key",
                            data={
                                "username": "andrew"
                            })
        self.assertTrue(res.ok)


if __name__ == "__main__":
    unittest.main()
