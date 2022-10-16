from flask_restful import Api, Resource, reqparse
from flask import Flask, request
import pandas as pd
import json

class ApiHandler(Resource):

    parsed = ''

    def __init__(self, message):
        self.message = message
    
    def get(self):
        data_frame = self.message
        return data_frame

    def post(self):
        print(self)
        parser = reqparse.RequestParser()
        parser.add_argument('type', type=str)
        parser.add_argument('message', type=str)

        args = parser.parse_args()

        print(args)
        # note, the post req from frontend needs to match the strings here (e.g. 'type and 'message')

        request_type = args['type']
        request_json = args['message']
        # ret_status, ret_msg = ReturnData(request_type, request_json)
        # currently just returning the req straight
        ret_status = request_type
        ret_msg = request_json

        if ret_msg:
            message = "Your Message Requested: {}".format(ret_msg)
        else:
            message = "No Msg"
        
        final_ret = {"status": "Success", "message": message}

        return final_ret

    def read_data(csv):
        all_data = pd.read_csv(csv)
        lap_data = all_data.loc[all_data['ShortName'] == "LAP"]
        sorted_data = lap_data.nsmallest(400,'Time')
        ranked = sorted_data.drop_duplicates(subset=['LastName'], keep='first')

        return ranked

class FileHandler(Resource):
    def __init__(self, event, session):
        self.event = event
        self.session = session
    def get(self):
        event = self.event
        session = self.session
        return {
      'event': event,
      'session': session
      }

class FileUploader(Resource):
    def __init__(self, message):
        self.message = message
    
    def post(self):
        global parsed 
        print(request.files)
        file = request.files['file']
        all_data = pd.read_csv(file)
        lap_data = all_data.loc[all_data['ShortName'] == "LAP"]
        sorted_data = lap_data.nsmallest(400,'Time')
        ranked = sorted_data.drop_duplicates(subset=['LastName'], keep='first')
        result = ranked.to_json(orient='records')
        parsed = json.loads(result)
        return parsed

    def get(self):
        global parsed
        data_frame = parsed
        return data_frame