from app import app
from app import db, utils
from snow_data import skiarea
import os
import schedule
from apscheduler.schedulers.background import BackgroundScheduler
from flask import jsonify, session, make_response
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
from datetime import date
import uuid

api = Api(app)  
app.secret_key = os.urandom(24) 
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)


skiarea.update_sa()
# skiarea.check_website_change() # TODO get this working and then set a schedule for it
# skiarea.create_new_month()


# if it's the first of the month, create a new month for each ski area
def check_first_of_month():
    if date.today().day == 1:
        skiarea.create_new_month()


# checks all the pending scheduled jobs
def check_pending():
    schedule.run_pending()


# schedule tasks to update the database with ski area data
schedule.every(20).minutes.do(skiarea.update_sa)  # update ski area data every 20 min
schedule.every().day.at("10:30").do(db.reset_api_counts)  # reset api counts once a day
schedule.every().day.at("02:00").do(check_first_of_month)  # updates monthly data if it's first of month
scheduler = BackgroundScheduler()
scheduler.add_job(func=check_pending, trigger="interval", seconds=300)
scheduler.start()


#####################
# flask-restful api #
#####################

parser = reqparse.RequestParser()
parser.add_argument("skiareaname", type=str, location="json")
parser.add_argument("month", type=str, location="json")
parser.add_argument("year", type=str, location="json")
parser.add_argument("api_key", type=str, location="json")
parser.add_argument("username", type=str, location="json")
parser.add_argument("email", type=str, location="json")
parser.add_argument("newemail", type=str, location="json")
parser.add_argument("password", type=str, location="json")
parser.add_argument("newpassword", type=str, location="json")


class TestSession(Resource):
    def get(self):
        session["sessionId"] = uuid.uuid4()
        print("DEBUG session:", session["sessionId"])

        response = make_response()
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        # response.set_cookie('sessionId', str(session["sessionId"]), secure=False, httponly=False)
        return response



class GetAllData(Resource):
    def get(self, api_key):
        if db.verify_api_key(api_key):
            data = db.get_all_data()
            if data:
                return jsonify(data)
        return jsonify("Fail")


class GetAllMonthlyData(Resource):
    def get(self, api_key):
        if db.verify_api_key(api_key):
            data = db.get_all_monthly_data()
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


class GetSkiAreaMonthlyData(Resource):
    def post(self):
        args = parser.parse_args()
        ski_area_name = args["skiareaname"]
        api_key = args["api_key"]

        if db.verify_api_key(api_key):
            data = db.get_ski_areas_monthly_data(ski_area_name)
            if data:
                return jsonify(data)
        return jsonify("Fail")


class GetSkiAreaMonthYear(Resource):
    def post(self):
        args = parser.parse_args()
        ski_area_name = args["skiareaname"]
        month = args["month"]
        year = args["year"]
        api_key = args["api_key"]

        if db.verify_api_key(api_key):
            data = db.get_ski_areas_month_year(ski_area_name, month, year)
            if data:
                return jsonify(data)
        return jsonify("Fail")


class CreateUser(Resource):
    def post(self):
        api_key = utils.generate_api_key()
        args = parser.parse_args()

        data = {
            "username": args["username"],
            "email": args["email"],
            "password": args["password"],
            "api_key": api_key
        }

        if db.create_user(data):
            res = {
                "message": "Success",
                "api_key": api_key
            }
            return jsonify(**res)
        return jsonify("Fail")


class DeleteUser(Resource):
    def post(self):
        args = parser.parse_args()
        data = {
            "username": args["username"],
            "password": args["password"]
        }

        if db.check_password(data):
            if db.delete_user(data):
                res = {
                    "message": "Success"
                }
                return jsonify(**res)
        return jsonify("Fail")


class Login(Resource):
    def post(self):
        args = parser.parse_args()
        data = {
            "username": args["username"],
            "password": args["password"]
        }

        if db.check_password(data):
            api_key = db.get_api_key(data)
            res = {
                "message": "Success",
                "api_key": api_key
            }
            return jsonify(**res)
        return jsonify("Fail")


class UpdatePassword(Resource):
    def post(self):
        args = parser.parse_args()
        data = {
            "username": args["username"],
            "password": args["password"],
            "new_password": args["newpassword"]
        }

        if db.check_password(data):
            if db.update_password(data):
                res = {
                    "message": "Success"
                }
                return jsonify(**res)
        return jsonify("Fail")


class UpdateEmail(Resource):
    def post(self):
        args = parser.parse_args()
        data = {
            "username": args["username"],
            "password": args["password"],
            "new_email": args["newemail"]
        }

        if db.check_password(data):
            if db.update_email(data):
                res = {
                    "message": "Success"
                }
                return jsonify(**res)
        return jsonify("Fail")


if __name__ == '__main__':
    app.run()

api.add_resource(GetAllData, '/get-all-data/<string:api_key>')
api.add_resource(GetAllMonthlyData, '/get-all-monthly-data/<string:api_key>')
api.add_resource(GetSkiArea, '/get-ski-area')
api.add_resource(GetSkiAreaMonthlyData, '/get-ski-area-monthly-data')
api.add_resource(GetSkiAreaMonthYear, '/get-ski-area-month-year')
api.add_resource(CreateUser, '/create-user')
api.add_resource(DeleteUser, '/delete-user')
api.add_resource(Login, '/login')
api.add_resource(UpdateEmail, '/update-email')
api.add_resource(UpdatePassword, '/update-password')
api.add_resource(TestSession, '/test-session')

CORS(app, expose_headers='Authorization')
