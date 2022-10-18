# penske_assessment

Welcome to the Team Penske lap time viewer!

This project utilizes a Python flask server with a React.js front-end to create a web application that allows a user to view csv files containing lap time data. The python flask server stores the uploaded files locally in memory -- with no need for a database -- then serves those files via API to the front-end UI. The React.js UI is served statically via Flask, and can be accessed on port 5000 (http://127.0.0.1:5000/).

# Getting Started

First pull the repository, then in terminal, cd to the local directory in which it is stored.

Next start the python virtual environment by using the command '. .(venv)/bin/activate' without the quotations.

Once the Virtual environment is active, execute the command 'flask --app main run' in the main directory.

Now you should be good to go, just visit http://127.0.0.1:5000/ and the web app will be ready to execute.

# How to use the app

The app is very simple, select 'Choose a file...' to be prompted to pick a CSV file from your file system. Once selected, click the 'Upload' button and the lap times viewer will display the data from fastest to slowest. Please be patient, larger files will take a few seconds (usually around 5) to process the data file.
