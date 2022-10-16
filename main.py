import pandas as pd
from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api.ApiHandler import ApiHandler, FileHandler, FileUploader
import json
import re

app = Flask(__name__, static_url_path='', static_folder='lap_viewer/build')
CORS(app) #comment this on deployment
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

filePath = '/Users/turnerhilliard/Downloads/Chevrolet Detroit Grand Prix_Practice 2.csv'

fileName = re.sub(r'^\/(.+\/)*','',filePath)

event = re.search(r'(.*?)(?=\_)',fileName)

session = re.search(r'(?<=\_)(.*?)(?=\.)', fileName)

data = ApiHandler.read_data(filePath)

result = data.to_json(orient='records')
parsed = json.loads(result)
json.dumps(parsed)

api.add_resource(ApiHandler, '/flask/hello',
            resource_class_kwargs={'message': parsed})

api.add_resource(FileHandler, '/filename',
            resource_class_kwargs={'event': event.group(0), 'session': session.group(0)})

api.add_resource(FileUploader, '/upload', 
            resource_class_kwargs={'message': ''})