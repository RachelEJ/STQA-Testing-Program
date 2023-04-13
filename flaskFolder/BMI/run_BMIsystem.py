# File to run for BMIsystem execution. Separates main() call for modularity purposes.

from BMIsystem import CalcBMI, ClassifyBMI

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
    elif (category == 4):
        print("BMI: %.1f\n" % BMI)
        print("Category: Obese\n")

main()