# STQA-Testing-Program

[![Coverage Status](https://coveralls.io/repos/github/RachelEJ/STQA-Testing-Program/badge.svg?branch=main)](https://coveralls.io/github/RachelEJ/STQA-Testing-Program?branch=main)

## Description  
This repository contains 4 Python files for CSE 4283.  
* `assignment2.py` contains the functions to take in height and weight as user input, calculate the user's BMI, and inform the user of what category their BMI is.  
* `test_assignment2.py` contains the functions from `assignment2.py` as well as pytest parametrization and assertions to test correct output of the functions.
* `assignment2-boundShift.py` contains the same code as `assignment2.py` but shifts the lower boundary of the normal category up 0.1
* `test_assignment2-boundShift.py` contains the functions from `assignment2-boundShift.py` as well as pytest parametrization and assertions to test correct output of the functions.

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
