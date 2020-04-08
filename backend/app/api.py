from app import app
from app import db
import os
import schedule
from apscheduler.schedulers.background import BackgroundScheduler
import time 
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
import mysql.connector
from scraper import skiarea

# setup flask restful api
api = Api(app)

# set config
app.secret_key = os.urandom(24)  # for cors to work
app_settings = os.getenv('APP_SETTINGS') 
app.config.from_object(app_settings)      

# test func to see if scheduler is working
def update_data():
    print("\n\n\n[DEBUG] Updating Data")
    print("[DEBUG]", os.system("date"))
    print("\n\n")

def check_pending():
    schedule.run_pending()

# create a scheduler to update every 10 minutes
schedule.every(2).minutes.do(update_data)
scheduler = BackgroundScheduler()
scheduler.add_job(func=check_pending, trigger="interval", seconds=300)
scheduler.start()

@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify('Hello')


#####################
# flask-restful api #
#####################

parser = reqparse.RequestParser()
parser.add_argument("skiareaname", type=str, location="json")


class get_all_data(Resource):
    def get(self):
        data = db.get_all_data()
        if data:
            return jsonify(data)
        else:
            return jsonify("[DEBUG] Failed get data")


class get_ski_area(Resource):
    def get(self):
        return jsonify("Error. Must be POST Request")

    def post(self):
        args = parser.parse_args()
        ski_area_name = args["skiareaname"]
        data = db.get_ski_area(ski_area_name)
        if data:
            return jsonify(data)
        else:
            return jsonify("[DEBUG] Failed get data")

        




if __name__ == '__main__':
    app.run()


api.add_resource(get_all_data, '/get-all-data')
api.add_resource(get_ski_area, '/get-ski-area')

CORS(app, expose_headers='Authorization')
