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

