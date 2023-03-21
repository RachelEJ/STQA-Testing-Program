import math
import pytest

# calculates BMI and returns answer rounded to 1 decimal place 
# uses height (given in feet and inches) and weight (given in pounds)
def CalcBMI(feet, inches, pounds):
    kgWeight = pounds * 0.45

    totalHeight = (feet * 12) + inches
    mHeight = totalHeight * 0.025

    squaredHeight = mHeight * mHeight

    finalBMI = kgWeight / squaredHeight
    return round(finalBMI, 1)

# defines arguments to pass into test_CalcBMI
@pytest.mark.parametrize("feet, inches, pounds, finalBMI", [(5, 10, 140, 20.6), (5, 3, 125, 22.7)])

# tests CalcBMI using arguments from above parametrization
def test_CalcBMI(feet, inches, pounds, finalBMI):
    assert CalcBMI(feet, inches, pounds) == finalBMI


# weight category key
# 1 - underweight
# 2 - normal weight
# 3 - overweight
# 4 - obese

# classifies BMI category
# uses BMI rounded to 1 decimal place
def ClassifyBMI(BMI):
    if (BMI < 18.5):
        return 1
    elif (BMI >= 18.5) and (BMI <= 24.9):
        return 2
    elif (BMI >= 25) and (BMI <= 29.9):
        return 3
    else:
        return 4

# defines arguments to pass into test_ClassifyBMI
@pytest.mark.parametrize("BMI, category", [(18.4, 1), (18.5, 2), (23, 2), (24.9, 2), (25, 3), (27, 3), (29.9, 3), (30, 4), (30.1, 4)])

# tests ClassifyBMI using arguments from above parametrization
def test_ClassifyBMI(BMI, category):
    assert ClassifyBMI(BMI) == category


# prompts user input for height and weight measurements
def GetMeasurements():
    print("Enter in your height and weight measurements below...")
    feet = ""
    inches = ""
    weight = ""
    while(True):
        feet = input("Enter feet: ")
        if (not (feet.isnumeric())):
            print("Invalid input. Try again.\n")
            continue


        inches = input("Enter inches: ")
        if (not (inches.isnumeric())):
            print("Invalid input. Try again.\n")
            continue

        weight = input ("Enter weight (in pounds): ")
        if (not (weight.isnumeric())):
            print("Invalid input. Try again.\n")
            continue

        if ((float(feet) <= 0) or (float(inches) < 0) or (float(weight) <= 0)):
            print("Enter in correct measurements this time :)\n")
        else:
            break
    
    feet = float(feet)
    inches = float(inches)
    weight = float(weight)
    measurements = (feet, inches, weight)
    return measurements

# ADD IN TESTS FOR THIS ONE LATER

# def test_GetMeasurements():

def main():
    measurements = GetMeasurements()
    BMI = CalcBMI(measurements[0], measurements[1], measurements[2])
    category = ClassifyBMI(BMI)
    if (category == 1):
        print("BMI: %.1f\n" % BMI)
        print("Category: Underweight\n")
    elif (category == 2):
        print("BMI: %.1f\n" % BMI)
        print("Category: Normal weight\n")
    elif (category == 3):
        print("BMI: %.1f\n" % BMI)
        print("Category: Overweight\n")
    else:
        print("BMI: %.1f\n" % BMI)
        print("Category: Obese\n")

main()
