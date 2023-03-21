# STQA-Testing-Program

## Description  
This repository contains 4 Python files for CSE 4283.  
* `assignment2.py` contains the functions to take in height and weight as user input, calculate the user's BMI, and inform the user of what category their BMI is.  
* `test_assignment2.py` contains the functions from `assignment2.py` as well as pytest parametrization and assertions to test correct output of the functions.
* `assignment2-boundShift.py` contains the same code as `assignment2.py` but shifts the lower boundary of the normal category up 0.1
* `test_assignment2-boundShift.py` contains the functions from `assignment2-boundShift.py` as well as pytest parametrization and assertions to test correct output of the functions.

## Setup Instructions  
1. Open your command line window of choice  
2. Ensure that Python3 is installed  
    - Verify using `python3 --version`  
    - If not, follow installation instructions at https://docs.python.org/3.6/using/windows.html#installing-python  
3. Ensure that pip is installed  
    - Verify using `pip --version`  
    - If not, follow installation instructions at https://pip.pypa.io/en/stable/installation/  
4. Ensure that pytest is installed  
    - Verify using `pytest --version`  
    - If not, follow installation instructions at https://docs.pytest.org/en/6.2.x/getting-started.html  
5. Download `assignment2.py` and `test_assignment2.py` into a directory

## Execution Instructions
1. Open your command line window of choice
2. Navigate to the directory the files are located in
3. Use `python3 assignment2.py` to execute base BMI Calculation functionality
4. Use `pytest` to automatically execute tests using pytest
