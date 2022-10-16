from sqlite3 import Row
from flask_restful import Api, Resource, reqparse
from flask import Flask, request
import pandas as pd
import json
import re

class ApiHandler(Resource):

    parsed = ''
    file_name = ''

    def __init__(self, message):
        self.message = message
    
    def get(self):
        data_frame = self.message
        return data_frame

    def post(self):
        # print(self)
        parser = reqparse.RequestParser()
        parser.add_argument('type', type=str)
        parser.add_argument('message', type=str)

        args = parser.parse_args()

        # print(args)
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

# class FileHandler(Resource):
#     def __init__(self, event, session):
#         self.event = event
#         self.session = session
#     def get(self):
#         event = self.event
#         session = self.session
#         return {
#         'event': event,
#         'session': session
#         }
#     def post(self):
#         event = self.event
#         session = self.session
#         return {
#         'event': event,
#         'session': session
#         }

class FileHandler(Resource):
    def post(self):
        global file_name 
        data = request.get_json(force=True)
        file_name = data
        return file_name

    def get(self):
        global file_name
        file_name_str = str(file_name)
        event = re.search(r'(.*?)(?=\_)',file_name_str)
        session = re.search(r'(?<=\_)(.*?)(?=\.)', file_name_str)
        event = re.sub(r'\{(.*?)\:','', event.group(0))
        event = re.sub(r'\ (.*?)\'', '', event)

        return {
        'event': str(event),
        'session': session.group(0)
        }

class FileUploader(Resource):
    def __init__(self, message):
        self.message = message
    
    def post(self):
        global parsed 

        file = request.files['file']
        all_data = pd.read_csv(file, on_bad_lines='skip')
        lap_data = all_data.loc[all_data['ShortName'] == "LAP"]
        sorted_data = lap_data.nsmallest(400,'Time')
        ranked = sorted_data.drop_duplicates(subset=['LastName'], keep='first')
        
        # try:
        #     ranked.astype({'CarNumber': 'int'}).dtypes
        # except ValueError:
        #     filtered = ranked.drop([2948])
        #     print("Hopefully i dropped a row")
        # print(type(ranked.loc[2948, 'CarNumber']))
        # ranked.loc[ranked['CarNumber'].apply(type) != numpy.float64]
        # print(filtered)

        result = ranked.to_json(orient='records')
        parsed = json.loads(result)
        return parsed

    def get(self):
        global parsed
        data_frame = parsed
        return data_frame