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

# posts device token to db
def update_ski_area(name):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("use snow_db")
        query = """ INSERT INTO ski_areas (`token`) VALUES ("%s"); """ % name
        cursor.execute(query)
        db.commit()
        return True
    except:
        return False


# returns all the device tokens as a list
def get_all_device_tokens():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("use snow_db")
    cursor.execute("SELECT token FROM ios_device_tokens;")
    results = [token[0] for token in cursor.fetchall()]
    return results



