from app import app
from app import db
from app import utils
from scraper import skiarea
import os
import schedule
from apscheduler.schedulers.background import BackgroundScheduler
from flask import jsonify, session
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
from datetime import date


api = Api(app)  # sets up flask restful api
app.secret_key = os.urandom(24)  # for cors to work
app_settings = os.getenv('APP_SETTINGS') 
app.config.from_object(app_settings)      


# if it's the first of the month, create a new month for each ski area
def check_first_of_month():
    if date.today().day == 1:
        skiarea.create_new_month()


# checks all the pending scheduled jobs
def check_pending():
    schedule.run_pending()


#
# schedule tasks to update the database with ski area data
#

schedule.every(20).minutes.do(skiarea.update_sa)  # update ski area data every 20 min
schedule.every(120).minutes.do(skiarea.update_avg_temps)  # updates avg temps every 2 hours
schedule.every().day.at("10:30").do(db.reset_api_counts)  # reset api counts once a day
schedule.every().day.at("02:00").do(check_first_of_month)  # updates monthly data if it's first of month
scheduler = BackgroundScheduler()
scheduler.add_job(func=check_pending, trigger="interval", seconds=300)
scheduler.start()


@app.route('/', methods=['GET', 'POST'])
def index():
    # TODO remove this after it is working
    skiarea.create_new_month()
    
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


class GetAllData(Resource):
    def get(self, api_key):
        if db.verify_api_key(api_key):
            data = db.get_all_data()
            if data:
                return jsonify(data)
        return jsonify("Fail")
        

class GetSkiArea(Resource):
    def post(self):
        args = parser.parse_args()
        ski_area_name = args["skiareaname"]
        api_key = args["api_key"]

        if db.verify_api_key(api_key):
            data = db.get_ski_area(ski_area_name)
            if data:
                return jsonify(data)
        return jsonify("Fail")


class CreateUser(Resource):
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
            session["username"] = data["username"]
            print("DEBUG create_user session[username]:", session["username"])
            return jsonify(api_key)
        return jsonify("Fail")


class DeleteUser(Resource):
    def post(self):
        args = parser.parse_args()
        data = { "username" : args["username"] }

        if data["username"] in session: 
            if db.delete_user(data):
                session.pop(data["username"], None)
                return jsonify("Success")
            return jsonify("Fail")
        return jsonify("Fail")


class Login(Resource):
    def post(self):
        args = parser.parse_args()
        data = {
            "username" : args["username"],
            "password" : args["password"]
        }

        if db.login(data):
            session["username"] = data["username"]
            print("DEBUG login session[username]:", session["username"])
            return jsonify("Success")
        return jsonify("Fail")


class Logout(Resource):
    def post(self):
        args = parser.parse_args()
        data = { "username" : args["username"] }

        if data["username"] in session:
            print("DEBUG login session[username]:", session["username"])
            session.pop(data["username"], None)
            return jsonify("Success")
        return jsonify("Fail")


class GetAPIKey(Resource):
    def post(self):
        args = parser.parse_args()
        data = { "username" : args["username"] }

        print("DEBUG get_api_key session[username]:", session["username"])

        if data["username"] in session: 
            print("DEBUG login session[username]:", session["username"])
            api_key = db.get_api_key(data)
            print("DEBUG api_key:", api_key)
            return jsonify(api_key)
        return jsonify("Fail")


if __name__ == '__main__':
    app.run()


api.add_resource(GetAllData, '/get-all-data/<string:api_key>')
api.add_resource(GetSkiArea, '/get-ski-area')
api.add_resource(CreateUser, '/create-user')
api.add_resource(DeleteUser, '/delete-user')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(GetAPIKey, '/get-api-key')

CORS(app, expose_headers='Authorization')
