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
    cursor = db.cursor()
    cursor.execute("use snow_db")
    cursor.execute(""" SELECT * FROM ski_area; """)
    results = list(cursor.fetchall()) # convert outer tuple to list
    results = [list(i) for i in results] # convert nested tuples to lists

    for item in results: # pop id off each list
        item.pop(0)
    return results


# returns a ski areas data
def get_ski_area(name):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("use snow_db")
    cursor.execute(""" SELECT * FROM ski_area WHERE name="%s";  """ % name)
    results = list(cursor.fetchall()[0])
    results.pop(0)
    return results
