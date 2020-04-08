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

# # posts device token to db
# def update_ski_area(name):
#     try:
#         db = get_db()
#         cursor = db.cursor()
#         cursor.execute("use snow_db")
#         query = """ INSERT INTO ski_area VALUES ("%s"); """ % name
#         cursor.execute(query)
#         db.commit()
#         return True
#     except:
#         return False


# returns a ski areas data
def get_all_data():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("use snow_db")
    cursor.execute(""" SELECT * FROM ski_area; """)
    results = cursor.fetchall()
    return results


def get_ski_area(name):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("use snow_db")
    cursor.execute(""" SELECT * FROM ski_area WHERE name="%s";  """ % name)
    results = cursor.fetchall()
    return results
