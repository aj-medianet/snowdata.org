# class for ski areas
from app import db
from scraper import resort_scraper
from app import utils
from datetime import date, timedelta

# global list of ski areas we're parsing
SKI_AREAS = ["alpental", "jackson_hole", "mt_bachelor", "mt_hood", "ski49n", "snowbird", "whitefish"]


class SkiArea:

    def __init__(self, name, cur_temp=None, cur_depth=None, ytd=None, wind_dir=None, wind_speed=None, new_snow_12=None,
                 new_snow_24=None, new_snow_48=None, avg_temp=None):
        self.name = name
        self.cur_temp = cur_temp
        self.cur_depth = cur_depth
        self.ytd = ytd
        self.wind_dir = wind_dir
        self.wind_speed = wind_speed
        self.new_snow_12 = new_snow_12
        self.new_snow_24 = new_snow_24
        self.new_snow_48 = new_snow_48
        self.avg_temp = avg_temp

    # updates the database with all of the ski areas data
    def update_ski_areas(self):
        db.update_ski_area(self.__dict__)

    # calculates monthly data for a ski area and updates the db
    def update_monthly_data(self):
        print("[DEBUG] sa.update_monthly_data()")
        prev = utils.get_prev_month()
        previous_month_data = db.get_previous_month(self.name, prev.month, prev.year)

        data = {
            "ski_area_name": self.name,
            "month": date.today().month,
            "year": date.today().year,
            "total_new_snow": int(self.ytd) - int(previous_month_data["ytd"]),
            "snow_depth": self.cur_depth,
            "avg_temp": db.get_avg_temp(self.__dict__),
            "ytd": self.ytd
        }

        print("[DEBUG] update_monthly_data():", data)
        db.update_monthly_data(data)

        self.reset_avg_temp()  # reset so we can start calculating next months avg

    # updates avg temp
    def update_avg_temp(self):
        db.update_avg_temp(self.__dict__)

    # resets avg temp at beginning of new month
    def reset_avg_temp(self):
        db.reset_avg_temp(self.__dict__)


# loop through the list of ski areas, get the current data and update the db
def update_sa():
    for ski_area in SKI_AREAS:
        try:
            data = resort_scraper.get_data(ski_area)
            sa = SkiArea(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])
            sa.update_ski_areas()
        except:
            print("[DEBUG] Error scraping and updating {}".format(ski_area))


def update_avg_temps():
    for ski_area in SKI_AREAS:
        try:
            data = resort_scraper.get_data(ski_area)
            sa = SkiArea(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])
            sa.update_avg_temp()
        except:
            print("[DEBUG] Error updating average temp for {}".format(ski_area))


def update_monthly_data():
    for ski_area in SKI_AREAS:
        try:
            data = resort_scraper.get_data(ski_area)
            sa = SkiArea(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])
            sa.update_monthly_data()
        except:
            print("[DEBUG] Error updating monthly data for {}".format(ski_area))
