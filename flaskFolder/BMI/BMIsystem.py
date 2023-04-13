# File containing BMIsystem functions. Does not include main() for modularity purposes. 

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


