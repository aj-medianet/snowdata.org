import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
import credentials
from app import utils


################
# DB functions #
################


# returns the database connection
def get_db():
    config = {
        'user': credentials.db_user,
        'password': credentials.db_password,
        'host': credentials.db_host,
        'port': credentials.db_port,
        'database': credentials.db_name
    }
    connection = mysql.connector.connect(**config)
    return connection


###########################
# ski area data functions #
###########################

# returns all ski areas data
def get_all_data():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("use snow_db")
    cursor.execute(""" SELECT * FROM ski_areas; """)
    res = cursor.fetchall()
    for item in res:
        del item["id"]
    return res


# returns a single ski areas data
def get_ski_area(ski_area):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("use snow_db")
    cursor.execute(""" SELECT * FROM ski_areas WHERE name= %(ski_area)s;""", {'ski_area': ski_area})
    res = cursor.fetchone()
    del res["id"]
    return res


# updates a ski area with all of data
def update_ski_area(data):
    print("\n\n[DEBUG] db.update_ski_area() data:", data)
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("use snow_db")
        query = """ UPDATE ski_areas SET cur_temp = %(cur_temp)s, cur_depth = %(cur_depth)s, ytd = %(ytd)s, \
            wind_dir = %(wind_dir)s, wind_speed = %(wind_speed)s, new_snow_12 = %(new_snow_12)s, \
            new_snow_24 = %(new_snow_24)s, new_snow_48 = %(new_snow_48)s, ts = curdate() \
            WHERE name = %(name)s;""", {"cur_temp": data["cur_temp"], "cur_depth": data["cur_depth"],
                                        "ytd": data["ytd"], "wind_dir": data["wind_dir"],
                                        "wind_speed": data["wind_speed"], "new_snow_12": data["new_snow_12"],
                                        "new_snow_24": data["new_snow_24"], "new_snow_48": data["new_snow_48"],
                                        "name": data["name"]
                                        }
        cursor.execute(query)
        db.commit()
        print("[DEBUG] Updated {}\n\n".format(data["name"]))
    except:
        utils.print_error_message("Error updating {}".format(data["name"]))


# possible TODO if we have an admin web page
def create_ski_area(data):
    pass


# possible TODO if we have an admin web page
def delete_ski_area(data):
    pass


##########################
# monthly data functions #
##########################


# returns all of the monthly data for every ski area
def get_all_monthly_data():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("use snow_db")
    query = """ SELECT * FROM monthly_data;  """
    cursor.execute(query)
    res = cursor.fetchall()
    for item in res:
        del item["id"]
    return res


# returns all monthly data for a single ski area
def get_ski_areas_monthly_data(ski_area):
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("use snow_db")
        cursor.execute("""SELECT * FROM monthly_data WHERE ski_area_name = %(ski_area)s;""", {"ski_area": ski_area})
        res = cursor.fetchall()
        return res
    except:
        return "Error getting data. Data may not exist"


# returns the previous months monthly data
def get_ski_areas_month_year(ski_area, month, year):
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("use snow_db")
        cursor.execute("""SELECT * FROM monthly_data WHERE (ski_area_name = %(ski_area)s AND month=%(month)s \
         AND year=%(year)s);""", {"ski_area": ski_area, "month": month, "year": year})
        res = cursor.fetchone()
        del res["id"]
        return res
    except:
        return "Error getting data. Data may not exist"


# creates a new month for a ski area
def create_new_month(data):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("use snow_db")
        cursor.execute("""INSERT INTO monthly_data (month, year, ski_area_name, total_new_snow, snow_depth, avg_temp, \
         ytd) VALUES  (%(month)s, %(year)s, %(ski_area_name)s, %(total_new_snow)s, %(snow_depth)s, %(avg_temp)s, \
          %(ytd)s);""", {"month": data["month"], "year": data["year"], "ski_area_name": data["ski_area_name"],
                         "total_new_snow": data["total_new_snow"], "snow_depth": data["snow_depth"],
                         "avg_temp": data["avg_temp"], "ytd": data["ytd"]})
        db.commit()
        print("[DEBUG] Updated monthly data for {}\n\n".format(data["ski_area_name"]))
        return True
    except:
        utils.print_error_message("DB error creating new month")
        return False


# updates the monthly data table with a ski areas calculated monthly data
def update_monthly_data(data):
    print("\n\n[DEBUG] db.update_monthly_data() snow_data:", data)
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("use snow_db")
        cursor.execute(""" UPDATE monthly_data SET total_new_snow = %(total_new_snow)s, snow_depth = %(snow_depth)s, \
         avg_temp = %(avg_temp)s, ytd = %(ytd)s WHERE (ski_area_name = %(ski_area_name)s AND month = %(month)s AND \
         year = %(year)s);""", {"total_new_snow": data["total_new_snow"],"snow_depth": data["snow_depth"],
                                "avg_temp": data["avg_temp"], "ytd": data["ytd"], "ski_area_name": data["ski_area_name"],
                                "month": data["month"], "year": data["year"]})
        db.commit()
        print("[DEBUG] Updated monthly data for {}\n\n".format(data["ski_area_name"]))
    except:
        utils.print_error_message("Error updating monthly data for {}".format(data["ski_area_name"]))


#######################
# avg_temps functions #
#######################


def get_avg_temp(data):
    print("\n\n[DEBUG] db.get_avg_temp()")
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("use snow_db")
        cursor.execute("""SELECT * FROM avg_temps WHERE ski_area_name=%(ski_area_name)s;""",
                       {"ski_area_name": data["name"]})
        res = cursor.fetchone()
        return res["avg_temp"]
    except:
        utils.print_error_message("Error getting avg_temp from db")


# updates the average temperature for a ski area
# uses ski areas current temp and adds it to the overall average
def update_avg_temp(data):
    print("\n\n[DEBUG] db.update_avg_temps()")
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("use snow_db")
        cursor.execute(""" SELECT * FROM avg_temps WHERE ski_area_name=%(ski_area_name)s;  """,
                       {"ski_area_name": data["name"]})
        res = cursor.fetchone()
        new_total_temp = float(res["total_temp"]) + float(data["cur_temp"])
        new_count = res["count"] + 1
        new_avg_temp = int(new_total_temp / new_count)
    except:
        utils.print_error_message("Error getting temps")

    if new_avg_temp and new_total_temp and new_count:
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("use snow_db")
            cursor.execute(""" UPDATE avg_temps SET avg_temp=%(avg_temp)s, total_temp=%(total_temp)s, count=%(count)s \
            WHERE ski_area_name = %(ski_area_name)s; """, {"avg_temp": new_avg_temp, "total_temp": new_total_temp,
                                                           "count": new_count, "ski_area_name": data["name"]})
            db.commit()
            print("[DEBUG] Updated average temp for {}\n\n".format(data["name"]))
        except:
            utils.print_error_message("Error updating average temp for {}\n\n".format(data["name"]))


def reset_avg_temp(data):
    print("\n\n[DEBUG] db.reset_avg_temps()")
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("use snow_db")
        cursor.execute(""" UPDATE avg_temps SET avg_temp="0", total_temp="0", count="0" WHERE ski_area_name = \
        %(ski_area_name)s; """, {"ski_area_name": data["name"]})
        db.commit()
        print("[DEBUG] Reset avg temp for {}\n\n".format(data["name"]))
    except:
        utils.print_error_message("Error resetting avg temp for {}\n\n".format(data["name"]))


##################
# user functions #
##################


def create_user(data):
    print("\n\n[DEBUG] db.create_user() snow_data:", data)
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("use snow_db")
        hashed_pwd = generate_password_hash(data["password"])
        cursor.execute("""INSERT INTO users (username, email, password, api_key, api_count) VALUES (%(username)s, \
        %(email)s, %(password)s, %(api_key)s, 0);""", {"username": data["username"], "email": data["email"],
                                                       "password": hashed_pwd, "api_key": data["api_key"]})
        db.commit()
        return True
    except:
        utils.print_error_message("create_user mysql error")
        return False


def delete_user(data):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("use snow_db")
        cursor.execute("""DELETE from users where username=%(username)s;""", {"username": data["username"]})
        db.commit()
        return True
    except:
        utils.print_error_message("delete_user mysql error")
        return False


def update_password(data):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("use snow_db")
        hashed_pwd = generate_password_hash(data["new_password"])
        cursor.execute(""" UPDATE users SET password=%(password)s WHERE username=%(username)s; """,
                       {"password": hashed_pwd, "username": data["username"]})
        db.commit()
        return True
    except:
        utils.print_error_message("update_password mysql error")
        return False


def update_email(data):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("use snow_db")
        cursor.execute(""" UPDATE users SET email=%(email)s WHERE username=%(username)s; """,
                       {"email": data["new_email"], "username": data["username"]})
        db.commit()
        return True
    except:
        utils.print_error_message("update_email mysql error")
        return False


def check_password(data):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("use snow_db")
        cursor.execute(""" SELECT password FROM users WHERE username=%(username)s; """, {"username": data["username"]})
        pw_hash = cursor.fetchone()
        return check_password_hash(pw_hash[0], data["password"])
    except:
        utils.print_error_message("check_password mysql error")
        return False


#####################
# API key functions #
#####################


def get_api_key(data):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("use snow_db")
    cursor.execute("""SELECT api_key FROM users WHERE username=%(username)s;""", {"username": data["username"]})
    res = cursor.fetchone()
    return res


def verify_api_key(api_key):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("use snow_db")
    cursor.execute("""SELECT api_count FROM users WHERE api_key=%(api_key)s;""", {"api_key": api_key})
    res = cursor.fetchone()

    if res is not None:
        # if the api_key is from our web frontend / proxy server
        if api_key == "tmpkey" and res["api_count"] < 10000000:
            increment_api_count(api_key, res["api_count"])
            return True
        if res["api_count"] < credentials.api_limit:
            increment_api_count(api_key, res["api_count"])
            return True
    return False


def increment_api_count(api_key, count):
    count += 1
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("use snow_db")
    cursor.execute("""UPDATE users SET api_count=%(api_count)s WHERE api_key=%(api_key)s;""",
                   {"api_count": count, "api_key": api_key})
    db.commit()


def reset_api_counts():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("use snow_db")
    query = """UPDATE users SET api_count="0";"""
    cursor.execute(query)
    db.commit()


##########################
# website content checks #
##########################

def get_content(ski_area):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("use snow_db")
        cursor.execute("""SELECT content FROM websites WHERE ski_area_name=%(ski_area_name)s;""",
                       {"ski_area_name": ski_area})
        res = cursor.fetchone()
        return res[0]
    except:
        return None


def set_content(new_content, ski_area):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("use snow_db")
        cursor.execute("""UPDATE websites SET content=%(content)s WHERE ski_area_name=%(ski_area_name)s;""",
                       {"content": new_content, "ski_area_name": ski_area})
        db.commit()
        print("DEBUG commited")
        return True
    except:
        utils.print_error_message("Error setting content for {}".format(ski_area))
        return False
