# File containing BMIsystem functions. Does not include main() for modularity purposes. 

import math

# calculates BMI and returns answer rounded to 1 decimal place 
# uses height (given in feet and inches) and weight (given in pounds)
def CalcBMI(feet, inches, pounds):
    kgWeight = pounds * 0.45

    totalHeight = (feet * 12) + inches
    mHeight = totalHeight * 0.025

    squaredHeight = mHeight * mHeight

    finalBMI = kgWeight / squaredHeight
    return round(finalBMI, 1)

# weight category key
# 1 - underweight
# 2 - normal weight
# 3 - overweight
# 4 - obese

# classifies BMI category
# uses BMI rounded to 1 decimal place
def ClassifyBMI(BMI):
    if (BMI > 0) and (BMI < 18.5):
        return 1
    elif (BMI >= 18.5) and (BMI <= 24.9):
        return 2
    elif (BMI >= 25) and (BMI <= 29.9):
        return 3
    elif (BMI >= 30):
        return 4
    else:
        return -1

def main():
    print("Enter in your height and weight measurements below...")
    while(True):
        feet = input("Enter feet: ")
        if (not (feet.isnumeric())):
            print("Invalid input. Try again.\n")
            continue


        inches = input("Enter inches: ")
        if (not (inches.isnumeric())):
            print("Invalid input. Try again.\n")
            continue

        pounds = input ("Enter weight (in pounds): ")
        if (not (pounds.isnumeric())):
            print("Invalid input. Try again.\n")
            continue

        if ((float(feet) <= 0) or (float(inches) < 0) or (float(pounds) <= 0)):
            print("Enter in correct measurements this time :)\n")
        else:
            break
    
    feet = float(feet)
    inches = float(inches)
    pounds = float(pounds)
    measurements = (feet, inches, pounds)

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
    elif (categorry == 4):
        print("BMI: %.1f\n" % BMI)
        print("Category: Obese\n")
    else:
        print("An error has occurred. Please try again later\n")

