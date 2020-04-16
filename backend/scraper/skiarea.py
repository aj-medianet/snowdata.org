# class for ski areas
from app import db
from scraper import resort_scraper

class SkiArea:
    
    def __init__(self, name, cur_temp=None, cur_depth=None, ytd=None, wind_dir=None, wind_speed=None, new_snow_12=None, new_snow_24=None, new_snow_48=None):
        self.name = name
        self.cur_temp = cur_temp
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


    # TODO
    def update(self):
        print("in update")
        print(self.name)

    # TODO
    def update_db():
        db.update_ski_area()


# run through the list of ski areas and update all of them
def update_all():
    ski_areas = ["mt_bachelor"]
    for ski_area in ski_areas:
        data = resort_scraper.get_data(ski_area)
        sa = SkiArea(data)
        sa.update()


if __name__ == "__main__":
    update_all()   