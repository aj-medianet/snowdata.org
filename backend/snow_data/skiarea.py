from app import db, utils
from snow_data import resort_scraper, const, website_parser, weather


class SkiArea:
    """
    build a ski area obj so we can update snow_data, get snow_data, create monthly snow_data etc
    """

    def __init__(self, name, cur_temp=None, cur_depth=None, ytd=None, wind_dir=None, wind_speed=None, new_snow_12=None,
                 new_snow_24=None, new_snow_48=None, avg_temp=""):
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

    # gets snow data from resort scraper and assigns to instance variables
    def get_snow_data(self):
        snow_data = resort_scraper.get_data(self.name)
        self.cur_depth = snow_data["cur_depth"]
        self.ytd = snow_data["ytd"]
        self.new_snow_12 = snow_data["new_snow_12"]
        self.new_snow_24 = snow_data["new_snow_24"]
        self.new_snow_48 = snow_data["new_snow_48"]

    # gets the forecast from weather.gov api, assigns to instance variables and returns forecast as JSON obj
    def get_forecast_data(self):
        forecast_data = weather.get_current_forecast(const.SKI_AREAS[self.name]["weather_gov_url"])
        self.cur_temp = str(forecast_data["properties"]["periods"][0]["temperature"])
        self.wind_dir = forecast_data["properties"]["periods"][0]["windDirection"]
        self.wind_speed = forecast_data["properties"]["periods"][0]["windSpeed"].split(" ")[0]
        return forecast_data

    # updates the database with all of the ski areas snow_data
    def update_ski_areas(self):
        self.get_snow_data()
        db.update_forecast(self.name, self.get_forecast_data())
        db.update_ski_area(self.__dict__)
        self.update_avg_temp()

    # calculates monthly snow_data for a ski area and updates the db
    def create_new_month(self):
        prev = utils.get_prev_month()
        prev_prev = utils.get_two_months_ago()
        previous_month_data = db.get_ski_areas_month_year(self.name, prev_prev.month, prev_prev.year)
        data = {
            "ski_area_name": self.name,
            "month": prev.month,
            "year": prev.year,
            "total_new_snow": int(self.ytd) - int(previous_month_data["ytd"]),
            "snow_depth": self.cur_depth,
            "avg_temp": db.get_avg_temp(self.__dict__),
            "ytd": self.ytd
        }
        db.create_new_month(data)
        self.reset_avg_temp()  # reset so we can start calculating next months avg

    # updates avg temp
    def update_avg_temp(self):
        db.update_avg_temp(self.__dict__)

    # resets avg temp at beginning of new month
    def reset_avg_temp(self):
        db.reset_avg_temp(self.__dict__)


"""
 driver functions
"""


# loop through the list of ski areas, get the current snow_data/forecast and update the db
def update_sa():
    for ski_area in const.SKI_AREAS:
        try:
            sa = SkiArea(name=ski_area)
            sa.update_ski_areas()
        except:
            utils.print_error_message("Error scraping and updating {}".format(ski_area))


def create_new_month():
    for ski_area in const.SKI_AREAS:
        try:
            data = resort_scraper.get_data(ski_area)
            sa = SkiArea(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])
            sa.create_new_month()
        except:
            utils.print_error_message("SkiAreas error creating monthly snow_data for {}".format(ski_area))


# TODO
def check_website_change():
    for ski_area, value in const.SKI_AREAS.items():
        for key, url in value.items():
            old_content = db.get_content(ski_area)
            new_content = website_parser.get_plain_text(url)

            # compare old content to new content and update the db with the new content
            if old_content:
                if website_parser.compare_plain_texts(old_content, new_content) < 90:
                    try:
                        utils.send_email("{} has updated their website".format(ski_area))
                    except:
                        utils.print_error_message("Error sending email")
            updated = db.set_content(new_content, ski_area)

            if not updated:
                utils.print_error_message("Error updating website change db")
