from app import app
from app import db
import os
import schedule
import time 
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
import mysql.connector
from app.scraper import skiarea

# setup flask restful api
api = Api(app)

# set config
app.secret_key = os.urandom(24)  # for cors to work
app_settings = os.getenv('APP_SETTINGS') 
app.config.from_object(app_settings)      

# updates snow totals every 10 mintutes
def update_data():
    print("[DEBUG] Updating Data")
    print("[DEBUG]", os.system("date"))


# create a scheduler to update every 10 minutes
# https://pypi.org/project/schedule/
schedule.every(10).minutes.do(update_data)


# handles get and post requests for flask server
@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify('Hello')


#####################
# flask-restful api #
#####################

parser = reqparse.RequestParser()
parser.add_argument("devicetoken", type=str, location="json")


class get_data(Resource):
    def get(self):
        return jsonify("data")


if __name__ == '__main__':
    app.run()


api.add_resource(get_data, '/get-data')

CORS(app, expose_headers='Authorization')
