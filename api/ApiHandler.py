from sqlite3 import Row
from flask_restful import Api, Resource, reqparse
from flask import Flask, request
import pandas as pd
import json
import re
import numpy as np

class ApiHandler(Resource):

    def read_data(csv):
        all_data = pd.read_csv(csv)
        lap_data = all_data.loc[all_data['ShortName'] == "LAP"]
        sorted_data = lap_data.nsmallest(400,'Time')
        ranked = sorted_data.drop_duplicates(subset=['LastName'], keep='first')

        return ranked

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
        correctedFrame = FileUploader.superDataFixer(file)
        result = correctedFrame.to_json(orient='records')
        parsed = json.loads(result)
        return parsed

    def get(self):
        global parsed
        data_frame = parsed
        return data_frame
    
    def superDataFixer(file):
        # Fix the errors in incoming data 
        all_data = pd.read_csv(file, on_bad_lines='skip')
        newFrame = all_data.loc[~np.isnan(pd.to_numeric(all_data['CarNumber'], errors='coerce')),:]
        correctedFrame = newFrame.astype({'CarNumber': int}, errors='ignore')
        floatFrame = correctedFrame.loc[~np.isnan(pd.to_numeric(correctedFrame['Time'], errors='coerce')),:]
        newfloatFrame = floatFrame.astype({'Time': float}, errors='ignore')
        entryFrame = newfloatFrame.loc[~np.isnan(pd.to_numeric(newfloatFrame['EntryTime'], errors='coerce')),:]
        newentryFrame = entryFrame.astype({'EntryTime': float}, errors='ignore')
        exitFrame = newentryFrame.loc[~np.isnan(pd.to_numeric(newentryFrame['ExitTime'], errors='coerce')),:]
        newexitFrame = exitFrame.astype({'ExitTime': float}, errors='ignore')
        lapFrame = newexitFrame.loc[~np.isnan(pd.to_numeric(newexitFrame['Lap'], errors='coerce')),:]
        newlapFrame = lapFrame.astype({'Lap': int}, errors='ignore')

        # Sorting the data
        lap_data = newlapFrame.loc[all_data['ShortName'] == "LAP"]
        sorted_data = lap_data.nsmallest(400,'Time')
        ranked = sorted_data.drop_duplicates(subset=['LastName'], keep='first')
        return ranked