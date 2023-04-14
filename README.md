# STQA-Testing-Program

[![Coverage Status](https://coveralls.io/repos/github/RachelEJ/STQA-Testing-Program/badge.svg?branch=main)](https://coveralls.io/github/RachelEJ/STQA-Testing-Program?branch=main)

## Description  
This repository contains several files and directories. A summary of the important ones are:  
`.coveralls.yml` - file that specifies repo token for Coveralls reports  
`requirements.txt` - file that specifies all pip packages required for proper setup and execution  
`.circleci` - directory that contains config.yml  
`config.yml` - file that defines the jobs and workflow to run in CircleCI following every commit  

`flaskFolder` - directory that contains the application files  
`app.py` - file that contains the Flask webpage setup  

`BMI` - directory that contains the BMIsystem files  
`BMIsystem.py` - file that contains the CalcBMI() and ClassifyBMI() functions  
`run_BMIsystem.py` - file that contains the main() function to run the BMIsystem in the command line only  

`templates` - directory that contains index.html  
`index.html` - file that contains the base HTML template for the Flask webpage  

`tests` - directory that contains the testing files  
`conftest.py` - file that defines the client fixture for testing Flask webpage  
`test_BMIsystem.py` - file that contains the test functions for CalcBMI() and ClassifyBMI()  
`test_app.py` - file that contains the test functins for the Flask webpage  


## Setup Instructions  
1. Open your command line window of choice  
2. Ensure that Python 3 is installed  
    - Verify using `python3 --version`
    - If not, follow installation instructions at https://docs.python.org/3.6/using/windows.html#installing-python  
3. Ensure that pip is installed  
    - Verify using `pip --version`  
    - If not, follow installation instructions at https://pip.pypa.io/en/stable/installation/  
4. Clone this repository into a directory of your choice  
5. Navigate into the directory that requirements.txt is located in  
6. Install packages using pip  
    - Use `pip install -r requirements.txt`  
7. Ensure that pytest is installed  
    - Verify using `pytest --version`  
    - If not, follow installation instructions at https://docs.pytest.org/en/6.2.x/getting-started.html  
8. Ensure that Flask is installed  
    - Verify using `flask --version`  
    - If not, follow installation instructions at https://flask.palletsprojects.com/en/2.2.x/installation/  

## Execution Instructions
1. Open your command line window of choice
2. Navigate to the flaskFolder directory
3. Run `flask run`
4. Open your web browser window of choice
5. Navigate to http://127.0.0.1:5000 
6. Enter in your measurements
7. Click Calculate
8. Observe results
