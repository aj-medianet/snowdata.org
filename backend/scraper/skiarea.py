# class for ski areas
from app import db
from scraper import resort_scraper
from app import utils
from datetime import date

# global list of ski areas we're parsing
SKI_AREAS = ["alpental","jackson_hole", "mt_bachelor", "mt_hood", "ski49n", "snowbird", "whitefish"]


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
    def update_ski_areas_db(self):
        db.update_ski_area(self.__dict__)


    # returns a dictonary of last months data 
    def get_last_month(self):
        return db.get_last_month(self.name)
    

    # calculates monthly data for a ski area and updates the db
    def update_monthly_data(self):
        last_month_data = self.get_last_month()

        data = {
            "ski_area_name" : self.name,
            "month" : date.today().month,
            "year" : date.today().year,
            "total_new_snow" : self.ytd - last_month_data["ytd"],
            "snow_depth" : self.cur_depth,
            "avg_temp" : "",
            "ytd" : self.ytd
        } 

        print("[DEBUG] update_monthly_data():", data)
        #db.update_monthly_data(data)


# loop through the list of ski areas, get the current data and update the db
def update(func_call):
    for ski_area in SKI_AREAS:
        try:
            data = resort_scraper.get_data(ski_area)
            sa = SkiArea(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])

            if func_call == "sa":
                sa.update_ski_areas_db()
            elif func_call == "md":
                sa.update_monthly_data()
            elif func_call == "temps":
                sa.update_avg_temps()

        except:
            print("[DEBUG] Error scraping and updating {}".format(ski_area))



