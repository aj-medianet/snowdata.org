# class for ski areas
from app import db
from scraper import resort_scraper

class SkiArea:
    
    def __init__(self, name, temp=None, cur_depth=None, ytd=None, wind_dir=None, wind_speed=None, new_snow_12=None, new_snow_24=None, new_snow_48=None):
        self.name = name
        self.temp = temp
        self.cur_depth = cur_depth
        self.ytd = ytd
        self.wind_dir = wind_dir
        self.wind_speed = wind_speed
        self.new_snow_12 = new_snow_12
        self.new_snow_24 = new_snow_24
        self.new_snow_48 = new_snow_48

    
    def get_attr(self, attr_name):
        return self.attr_name


    def set_attr(self, attr_name, val):
        self.attr_name = val


    def test_print(self):
        print(self.name)
        print(self.temp)
        print(self.cur_depth)
        print(self.ytd)
        print(self.wind_dir)
        print(self.wind_speed)
        print(self.new_snow_12)
        print(self.new_snow_24)
        print(self.new_snow_48)


    # TODO
    def update_db(self):
        print("in update_db method")
        db.update_ski_area()


# run through the list of ski areas, get the current data and update the db
def update_all():
    ski_areas = ["mt_bachelor"] #, "jackson_hole", "mt_hood"]
    for ski_area in ski_areas:
        data = resort_scraper.get_data(ski_area)
        sa = SkiArea(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])
        sa.test_print()


if __name__ == "__main__":
    update_all()   