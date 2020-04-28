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

    
    # gets an individual attribute value
    def get_attr(self, attr_name):
        return self.attr_name


    # sets an individual attributes value
    def set_attr(self, attr_name, val):
        self.attr_name = val


    # updates the database with all of the ski areas data
    def update_db(self):
        db.update_ski_area(self.__dict__)


# run through the list of ski areas, get the current data and update the db
def update_all():
    ski_areas = ["alpental","jackson_hole", "mt_bachelor", "mt_hood", "ski49n", "snowbird", "whitefish"] #, "jackson_hole", "mt_hood"]
    for ski_area in ski_areas:
        try:
            data = resort_scraper.get_data(ski_area)
            sa = SkiArea(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])
            sa.update_db()
        except:
            print("[DEBUG] Error scraping and updating {}".format(ski_area))


if __name__ == "__main__":
    update_all()   