from app import db
import unittest

ski_area_test_data = {
    "name":"Alpental",
    "cur_temp": "12",
    "ytd": "100",
    "wind_dir": "W",
    "wind_speed": "12",
    "new_snow_12": "",
    "new_snow_24": "",
    "new_snow_48": "1"
}

monthly_test_data = {
    "month": "4",
    "year": "2020",
    "ski_area_name": "Alpental",
    "total_new_snow": "50",
    "snow_depth": "100",
    "avg_temp": "22",
    "ytd": "200"
}

user_test_data = {
    "username": "testusername",
    "email": "test@test.com",
    "password": "testpassword",
    "api_key": "testapikey"
}


class TestDB(unittest.TestCase):

    def test_get_all_data(self):
        data = db.get_all_data()
        self.assertTrue(data)

    def test_get_ski_area(self):
        data = db.get_ski_area("Alpental")
        self.assertTrue(data)

    def test_update_ski_area(self):
        res = db.update_ski_area(ski_area_test_data)
        self.assertTrue(res)

    def test_get_all_monthly_data(self):
        data = db.get_all_monthly_data()
        self.assertTrue(data)

    def test_get_ski_areas_monthly_data(self):
        data = db.get_ski_areas_monthly_data("Alpental")
        self.assertTrue(data)

    def test_get_ski_areas_month_year(self):
        data = db.get_ski_areas_month_year("Alpental", 4, 2020)
        self.assertTrue(data)

    def test_create_new_month(self):
        res = db.create_new_month(monthly_test_data)
        self.assertTrue(res)

    def test_update_monthly_data(self):
        res = db.update_monthly_data(monthly_test_data)
        self.assertTrue(res)

    def test_get_avg_temp(self):
        data = db.get_avg_temp(ski_area_test_data)
        self.assertTrue(data)

    def test_update_avg_temp(self):
        res = db.update_avg_temp(ski_area_test_data)
        self.assertTrue(res)

    def test_reset_avg_temp(self):
        res = db.reset_avg_temp(ski_area_test_data)
        self.assertTrue(res)

    def test_create_user(self):
        res = db.create_user(user_test_data)
        self.assertTrue(res)

    def test_check_password(self):
        res = db.check_password(user_test_data)
        self.assertTrue(res)

    def test_update_password(self):
        user_test_data["password"] = "testpassword1"
        res = db.update_avg_temp(user_test_data)
        self.assertTrue(res)

    def test_update_email(self):
        user_test_data["email"] = "test1@test.com"
        res = db.update_email(user_test_data)
        self.assertTrue(res)

    def test_get_api_key(self):
        data = db.get_api_key(user_test_data)
        self.assertTrue(data == "testapikey")

    def test_verify_api_key(self):
        res = db.verify_api_key("testapikey")
        self.assertTrue(res)

    def test_increment_api_count(self):
        res = db.increment_api_count("testapikey", 2)
        self.assertTrue(res)

    def test_reset_api_counts(self):
        res = db.reset_api_counts()
        self.assertTrue(res)

    def test_delete_user(self):
        res = db.delete_user(user_test_data)
        self.assertTrue(res)

    def test_get_content(self):
        data = db.get_api_key(ski_area_test_data["name"])
        self.assertTrue(data)

    def test_set_content(self):
        res = db.set_content("test content", ski_area_test_data["name"])
        self.assertTrue(res)


if __name__ == "__main__":
    unittest.main()