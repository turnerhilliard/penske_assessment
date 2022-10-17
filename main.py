import pandas as pd
from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api.ApiHandler import FileHandler, FileUploader, SectorLoader

app = Flask(__name__, static_url_path='', static_folder='lap_viewer/build')
CORS(app) #comment this on deployment
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

api.add_resource(FileHandler, '/filename')

api.add_resource(FileUploader, '/upload')

api.add_resource(SectorLoader, '/sector')
