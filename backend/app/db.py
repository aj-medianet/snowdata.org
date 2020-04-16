import mysql.connector

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
    try:
        connection = mysql.connector.connect(**config)
        return connection
    except:
        return "connection error"


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
    cursor.execute(""" SELECT * FROM ski_areas WHERE name="%s";  """ % name)
    res = cursor.fetchone()
    del res["id"]
    return res


# updates a ski area with all of its data
def update_ski_area(data):
    print("inside update ski area")
    print("[DEBUG] data:", data)
    db = get_db()
    cursor = db.cursor()
    cursor.execute("use snow_db")
    query = """ UPDATE ski_areas SET cur_temp = "25" WHERE name = "Snowbird"  """
    cursor.execute(query)
    db.commit()




