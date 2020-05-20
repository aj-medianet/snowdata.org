import requests
import unittest


class TestApi(unittest.TestCase):

    def test_get_all_data(self):
        res = requests.get("http://localhost:7082/get-all-data/tmpkey")
        self.assertTrue(res.json() != "Fail")
        self.assertTrue(res.ok)

    def test_get_all_monthly_data(self):
        res = requests.get("http://localhost:7082/get-all-monthly-data/tmpkey")
        self.assertTrue(res.json() != "Fail")
        self.assertTrue(res.ok)

    def test_get_ski_area(self):
        res = requests.post("http://localhost:7082/get-ski-area",
                            data={
                                "skiareaname": "Mt Bachelor",
                                "api_key": "tmpkey"
                            })
        self.assertTrue(res.json() != "Fail")
        self.assertTrue(res.ok)

    def test_get_ski_area_monthly_data(self):
        res = requests.post("http://localhost:7082/get-ski-area-monthly-data",
                            data={
                                "skiareaname": "Mt Bachelor",
                                "api_key": "tmpkey"
                            })
        self.assertTrue(res.json() != "Fail")
        self.assertTrue(res.ok)

    def test_get_ski_area_month_year(self):
        res = requests.post("http://localhost:7082/get-ski-area-month-year",
                            data={
                                "skiareaname": "Mt Bachelor",
                                "api_key": "tmpkey",
                                "month": "3",
                                "year": "2020"
                            })
        self.assertTrue(res.json() != "Fail")
        self.assertTrue(res.ok)

    def test_create_user(self):
        res = requests.post("http://localhost:7082/create-user",
                            data={
                                "username": "testuser1234",
                                "email": "test@test.com",
                                "password": "temppassword"
                            })
        self.assertTrue(res.json() != "Fail")
        self.assertTrue(res.ok)

    def test_delete_user(self):
        res = requests.post("http://localhost:7082/delete-user",
                            data={
                                "username": "testuser1234",
                                "password": "temppassword"
                            })
        self.assertTrue(res.json() != "Fail")
        self.assertTrue(res.ok)

    def test_login(self):
        res = requests.post("http://localhost:7082/login",
                            data={
                                "username": "testuser1234",
                                "password": "temppassword"
                            })
        self.assertTrue(res.json() != "Fail")
        self.assertTrue(res.ok)


if __name__ == "__main__":
    unittest.main()
