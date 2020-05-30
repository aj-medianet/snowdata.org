from snow_data import skiarea
import unittest


class TestSkiAreas(unittest.TestCase):

    def test_ski_areas(self):
        sa = skiarea.SkiArea("TestName", "TestTemp", "TestDepth", "TestYTD", "TestWindDir", "TestWindSpeed",\
                             "Test12", "Test24", "Test48")
        self.assertTrue(sa.name == "TestName")
        self.assertTrue(sa.cur_temp == "TestTemp")
        self.assertTrue(sa.cur_depth == "TestDepth")
        self.assertTrue(sa.ytd == "TestYTD")
        self.assertTrue(sa.wind_dir == "TestWindDir")
        self.assertTrue(sa.wind_speed == "TestWindSpeed")
        self.assertTrue(sa.new_snow_12 == "Test12")
        self.assertTrue(sa.new_snow_24 == "Test24")
        self.assertTrue(sa.new_snow_48 == "Test48")


if __name__ == "__main__":
    unittest.main()