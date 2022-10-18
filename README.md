# penske_assessment

Welcome to the Team Penske lap time viewer!

This project utilizes a Python flask server with a React.js front-end to create a web application that allows a user to view csv files containing lap time data. The python flask server stores the uploaded files locally in memory -- with no need for a database -- then serves those files via API to the front-end UI. The React.js UI is served statically via Flask, and can be accessed on port 5000 (http://127.0.0.1:5000/).

# Getting Started

First ensure that the latest version of python is installed from https://www.python.org/downloads/

Next, pull the repository. Then in terminal, cd to the local directory in which it is stored.

## Imports

Now is a good time to import the libraries necessary to run the code. Each of the following commands should be executed in the project directory:
- `python3 -m ensure pip --upgrade`
- `pip3 install flask`
- `pip3 install flask_restful`
- `pip3 install flask_cors`
- `pip3 install pandas`

## Starting the app

In terminal, execute the command `flask --app main run` (still in the project directory).

Now you should be good to go, just visit http://127.0.0.1:5000/ and the web app will be ready to execute.

# How to use the app

The app is very simple, select 'Choose a file...' to be prompted to pick a CSV file from your file system. Once selected, click the 'Upload' button and the lap times viewer will display the data from fastest to slowest. Please be patient, larger files will take a few seconds (usually around 5, depending on your machine) to process the data file.
