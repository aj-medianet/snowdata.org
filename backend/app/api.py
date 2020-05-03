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

# schedule tasks
schedule.every(20).minutes.do(skiarea.update("sa")) # update ski area data every 20 min
schedule.every(120).minutes.do(skiarea.update("temps")) # updates avg temps every 2 hours
schedule.every().day.at("10:30").do(db.reset_api_counts) # reset api counts once a day
scheduler = BackgroundScheduler()
scheduler.add_job(func=check_pending, trigger="interval", seconds=300)

# update monthly data on the first of every month
scheduler.add_job(func=skiarea.update("md"),trigger='cron', year='*', month='*', day='first')
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
parser.add_argument("username", type=str, location="json")
parser.add_argument("email", type=str, location="json")
parser.add_argument("password", type=str, location="json")


class get_all_data(Resource):
    def get(self, api_key):
        if db.verify_api_key(api_key):
            data = db.get_all_data()
            if data:
                return jsonify(data)
        return jsonify("API daily limit has been exceeded")
        

class get_ski_area(Resource):
    def post(self):
        args = parser.parse_args()
        ski_area_name = args["skiareaname"]
        api_key = args["api_key"]
        if db.verify_api_key(api_key):
            data = db.get_ski_area(ski_area_name)
            if data:
                return jsonify(data)
        return jsonify("API daily limit has been exceeded")


class create_user(Resource):
    def post(self):
        api_key = utils.generate_api_key()
        args = parser.parse_args()

        data = {
            "username" : args["username"],
            "email" : args["email"],
            "password" : args["password"],
            "api_key" : api_key
        }

        if db.create_user(data):
            return jsonify(api_key)
        return jsonify("Invalid Username")


class delete_user(Resource):
    def post(self):
        args = parser.parse_args()
        data = {
            "username" : args["username"],
            "password" : args["password"]
        }

        if db.login(data): # might take this out, but need to make sure user is logged in
            if db.delete_user(data):
                return jsonify("Success. {} deleted".format(args["username"]))
            return jsonify("Failed to delete")
        return jsonify("Failed. Incorrect username and password")


class login(Resource):
    def post(self):
        args = parser.parse_args()
        data = {
            "username" : args["username"],
            "password" : args["password"]
        }

        if db.login(data):
            return jsonify("Success")
        return jsonify("Failed")


class get_api_key(Resource):
    def post(self):
        args = parser.parse_args()
        data = {
            "username" : args["username"],
            "password" : args["password"]
        }

        if db.login(data): # might take this if out but need user to be logged in first
            api_key = db.get_api_key(data)
            return jsonify("Success. API Key: {}".format(api_key))
        return jsonify("Failed")


if __name__ == '__main__':
    app.run()


api.add_resource(get_all_data, '/get-all-data/<string:api_key>')
api.add_resource(get_ski_area, '/get-ski-area')
api.add_resource(create_user, '/create-user')
api.add_resource(delete_user, '/delete-user')
api.add_resource(login, '/login')
api.add_resource(get_api_key, '/get-api-key')

CORS(app, expose_headers='Authorization')
