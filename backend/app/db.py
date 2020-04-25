from app import app
from app import utils
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


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


# returns all data
def get_all_data():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("use snow_db")
    cursor.execute(""" SELECT * FROM ski_areas; """)
    res = cursor.fetchall()
    for item in res:
        del item["id"]
    return res


# returns a ski areas data
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
                new_snow_48 = "{}" WHERE name = "{}";  """.format(data["cur_temp"], \
                    data["cur_depth"], data["ytd"], data["wind_dir"], data["wind_speed"], \
                        data["new_snow_12"], data["new_snow_24"], data["new_snow_48"], data["name"])
        cursor.execute(query)
        db.commit()
        print("[DEBUG] Updated {}\n\n".format(data["name"]))
    except:
        print("[DEBUG] Error updating {}\n\n".format(data["name"]))


def create_user(data):
    print("\n\n[DEBUG] db.create_user() data:", data)
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("use snow_db")
        hashed_pwd = generate_password_hash(data["password"])
        query = """INSERT INTO users (username, email, password, api_key) VALUES ({}, {}, {}, {}) \
            """.format(data["username"], data["email"], hashed_pwd, data["api_key"]) 
        cursor.execute(query)
        db.commit()
        return True
    except:
        return False


def login(data):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("use snow_db")
    query = """ SELECT password FROM users WHERE username="{}" """.format(data["username"])
    cursor.execute(query)
    pwhash = cursor.fetchone()
    return check_password_hash(pwhash, data["password"])


def verify_api_key(api_key):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("use snow_db")
    query = """ SELECT api_count FROM users WHERE api_key="{}" """.format(api_key)
    cursor.execute(query)
    res = cursor.fetchone()
    print( "api_count:", res["api_count"] )
    if res["api_count"] < 5:
        increment_api_count(api_key, res["api_count"])
        return True
    return False


def increment_api_count(api_key, cur_count):
    cur_count += 1
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("use snow_db")
    query = """ UPDATE users SET api_count="{}" """.format(cur_count)
    cursor.execute(query)
    db.commit()


def reset_api_counts():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("use snow_db")    
    query = """ UPDATE users SET api_count="0" """
    cursor.execute(query)
    db.commit()

