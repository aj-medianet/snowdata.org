# class for ski areas


class SkiArea:
    
    def __init__(self, name, cur_temp, cur_depth, ytd, wind_dir, wind_speed, new_snow_12, new_snow_24, new_snow_48):
        self.name = name
        self.cur_temp = cur_temp
        self.cur_depth = cur_depth
        self.ytd = ytd
        self.wind_dir = wind_dir
        self.wind_speed = wind_speed
        self.new_snow_12 = new_snow_12
        self.new_snow_24 = new_snow_24
        self.new_snow_48 = new_snow_48

    
    # gettr method
    def get_attr(attr_name):
        return self.name


    # settr method
    def set_attr(attr_name, val):
        self.attr_name = val