from app import app
from app import utils
from app import login
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash


################
# DB functions #
################

# returns the database connection
def get_db():
    config = {
        'user': 'user',
        'password': 'password',
        'host': 'db',
        'port': '3306',
        'database': 'snow_db'
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
def get_ski_area(name):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("use snow_db")
    query = """ SELECT * FROM ski_areas WHERE name="{}";  """.format(name)
    cursor.execute(query)
    res = cursor.fetchone()
    del res["id"]
    return res


# updates a ski area with all of its data
def update_ski_area(data):
    print("\n\n[DEBUG] db.update_ski_area() data:", data)
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("use snow_db")
        query = """ UPDATE ski_areas SET cur_temp = "{}", cur_depth = "{}", ytd = "{}", \
            wind_dir = "{}", wind_speed = "{}", new_snow_12 = "{}", new_snow_24 = "{}", \
                new_snow_48 = "{}", ts = curdate() WHERE name = "{}";  """.format(data["cur_temp"], \
                    data["cur_depth"], data["ytd"], data["wind_dir"], data["wind_speed"], \
                        data["new_snow_12"], data["new_snow_24"], data["new_snow_48"], data["name"])
        cursor.execute(query)
        db.commit()
        print("[DEBUG] Updated {}\n\n".format(data["name"]))
    except:
        print("[DEBUG] Error updating {}\n\n".format(data["name"]))


# possible TODO if we have an admin web page
def create_ski_area(data):
    pass


# possible TODO if we have an admin web page
def delete_ski_area(data):
    pass


#########################
# monthlydata functions #
#########################

def get_previous_month(ski_area_name, month, year):
    print("DEBUG db.get_prev_month()")
    print("DEBUG ski_area_name:", ski_area_name)
    print("DEBUG month:", month)
    print("DEBUG year", year)
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("use snow_db")
    query = """ SELECT * FROM monthly_data WHERE (ski_area_name="{}" AND month="{}" AND year="{}");  """.format(ski_area_name, month, year)
    cursor.execute(query)
    res = cursor.fetchone()
    return res


def create_new_month(data):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("use snow_db")
        hashed_pwd = generate_password_hash(data["password"])
        query = """INSERT INTO monthly_data (month, year, ski_area_name, total_new_snow, snow_depth, avg_temp, ytd) VALUES  ("{}", "{}", "{}", "{}", "{}", "{}", "{}"); \
            """.format(data["month"], data["year"], data["ski_area_name"], data["total_new_snow"], data["snow_depth"], data["avg_temp"], data["ytd"]) 
        cursor.execute(query)
        db.commit()
        return True
    except:
        return False


# updates the montly data db with a ski areas calcualted montly data
def update_monthly_data(data):
    print("\n\n[DEBUG] db.update_monthly_data() data:", data)
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("use snow_db")
        query = """ UPDATE monthly_data SET total_new_snow = "{}", \
            snow_depth = "{}", avg_temp = "{}", ytd = "{}" WHERE ski_area_name = "{}", month = "{}", year = "{}";  """.format( \
            data["total_new_snow"], data["snow_depth"], data["avg_temp"], \
            data["ytd"], data["ski_area_name"], data["month"], data["year"])
        cursor.execute(query)
        db.commit()
        print("[DEBUG] Updated monthly data for {}\n\n".format(data["ski_area_name"]))
    except:
        print("[DEBUG] Error updating monthly data for {}\n\n".format(data["ski_area_name"]))



#######################
# avg_temps functions #
#######################


def get_avg_temp(data):
    print("\n\n[DEBUG] db.get_avg_temp()")
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("use snow_db")
        query = """ SELECT * FROM avg_temps WHERE ski_area_name="{}";  """.format(data["name"])
        cursor.execute(query)
        res = cursor.fetchone()
        return res["avg_temp"]
    except:
        print("[DEBUG] Error getting avg_temp from db")


# updates the average temperature for a ski area
# uses ski areas current temp and adds it to the overall average
def update_avg_temp(data):
    print("\n\n[DEBUG] db.update_avg_temps()")
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("use snow_db")
        query = """ SELECT * FROM avg_temps WHERE ski_area_name="{}";  """.format(data["name"])
        cursor.execute(query)
        res = cursor.fetchone()
        new_total_temp = float(res["total_temp"]) + float(data["cur_temp"])
        new_count = res["count"] + 1
        new_avg_temp = int(new_total_temp / new_count)
        
    except:
        print("[DEBUG] Error getting temps")

    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("use snow_db")
        query = """ UPDATE avg_temps SET avg_temp="{}", total_temp="{}", count="{}" WHERE ski_area_name = "{}"; """.format(new_avg_temp, new_total_temp, new_count, data["name"])
        cursor.execute(query)
        db.commit()
        print("[DEBUG] Updated average temp for {}\n\n".format(data["name"]))
    except:
        print("[DEBUG] Error updating average temp for {}\n\n".format(data["name"]))



def reset_avg_temp(data):
    print("\n\n[DEBUG] db.reset_avg_temps()")
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("use snow_db")
        query = """ UPDATE avg_temps SET avg_temp="0", total_temp="0", count="0" WHERE ski_area_name = "{}"; """.format(data["name"])
        cursor.execute(query)
        db.commit()
        print("[DEBUG] Reset avg temp for {}\n\n".format(data["name"]))
    except:
        print("[DEBUG] Error resetting avg temp for {}\n\n".format(data["name"]))



##################
# user functions #
##################


def create_user(data):
    print("\n\n[DEBUG] db.create_user() data:", data)
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("use snow_db")
        hashed_pwd = generate_password_hash(data["password"])
        query = """INSERT INTO users (username, email, password, api_key, api_count) VALUES ("{}", "{}", "{}", "{}", 0); \
            """.format(data["username"], data["email"], hashed_pwd, data["api_key"]) 
        cursor.execute(query)
        db.commit()
        return True
    except:
        return False


def delete_user(data):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("use snow_db")
        query = """ SET FOREIGN_KEY_CHECKS=0; DELETE from users where username="{}"; """.format(data["username"])
        cursor.execute(query)
        db.commit()
        return True
    except:
        return False


def update_password(data):
    print("\n\n[DEBUG] db.update_password() data:", data)
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("use snow_db")
        hashed_pwd = generate_password_hash(data["password"])
        query = """ UPDATE users SET password="{}" WHERE username="{}"; """.format(hashed_pwd, data["username"]) 
        cursor.execute(query)
        db.commit()
        return True
    except:
        return False


def login(data):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("use snow_db")
    query = """ SELECT password FROM users WHERE username="{}"; """.format(data["username"])
    cursor.execute(query)
    pwhash = cursor.fetchone()
    return check_password_hash(pwhash[0], data["password"])


#####################
# API key functions #
#####################


def get_api_key(data):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("use snow_db")
    query = """ SELECT api_key FROM users WHERE username="{}"; """.format(data["username"])
    cursor.execute(query)
    res = cursor.fetchone()
    return res
    

def verify_api_key(api_key):
    # if the api_key is from our web frontend
    # TODO - make this better
    if api_key == "tmpkey":
        return True

    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("use snow_db")
    query = """ SELECT api_count FROM users WHERE api_key="{}"; """.format(api_key)
    cursor.execute(query)
    res = cursor.fetchone()
    print("\n\n[DEBUG] api_count: {}\n".format(res["api_count"]))
    if res["api_count"] < 5:
        increment_api_count(api_key, res["api_count"])
        return True
    return False


def increment_api_count(api_key, cur_count):
    cur_count += 1
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("use snow_db")
    query = """ UPDATE users SET api_count="{}"; """.format(cur_count)
    cursor.execute(query)
    db.commit()


def reset_api_counts():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("use snow_db")    
    query = """ UPDATE users SET api_count="0"; """
    cursor.execute(query)
    db.commit()

