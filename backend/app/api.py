from app import app
from app import db
from app import utils
from scraper import skiarea
import os
import schedule
import time 
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse

api = Api(app)
app.secret_key = os.urandom(24)  # for cors to work
app_settings = os.getenv('APP_SETTINGS') 
app.config.from_object(app_settings)      


def check_pending():
    schedule.run_pending()

# schedule tasks to update the ski area data and reset api key counts 
schedule.every(10).minutes.do(skiarea.update_all)
schedule.every().day.at("10:30").do(db.reset_api_counts)
scheduler = BackgroundScheduler()
scheduler.add_job(func=check_pending, trigger="interval", seconds=300)
scheduler.start()

@app.route('/', methods=['GET', 'POST'])
def index():
    # test upate function TODO remove
    #skiarea.update_all()
    db.reset_api_counts()
    return jsonify('Hello')


#####################
# flask-restful api #
#####################

parser = reqparse.RequestParser()
parser.add_argument("skiareaname", type=str, location="json")
parser.add_argument("api_key", type=str, location="json")


class get_all_data(Resource):
    def get(self, api_key):
        if db.verify_api_key(api_key):
            data = db.get_all_data()
            if data:
                return jsonify(data)
        else:
            return jsonify("API daily limit has been exceeded")
        


class get_ski_area(Resource):
    def post(self):
        args = parser.parse_args()
        ski_area_name = args["skiareaname"]
        data = db.get_ski_area(ski_area_name)
        if data:
            return jsonify(data)


if __name__ == '__main__':
    app.run()


api.add_resource(get_all_data, '/get-all-data/<string:api_key>')
api.add_resource(get_ski_area, '/get-ski-area')

CORS(app, expose_headers='Authorization')
