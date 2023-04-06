import math
import pytest
import numbers


## takes two numbers and returns
## the result of a division
def numbers(num1, num2):
    try:
        try:
            temp1 = int(num1)
            temp2 = int(num2)
        except:
            print("num1 and num2 must be numbers")
            return
        if num2 == 0:
            print("NO DIVIDING BY ZERO")
            return
        return (num1 / num2)
    except:
        print("error processing input.")

@pytest.mark.parametrize("numb1, numb2, quotient", [(4, 2, 2), (7, 3, 3), ("hey", "uh", "no"), (0, 0, 0), ("", "", "")])

def test_numbers(numb1, numb2, quotient):
    assert numbers(numb1, numb2) == quotient
