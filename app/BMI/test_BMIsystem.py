import math
import pytest
from BMIsystem import CalcBMI, ClassifyBMI


# defines arguments to pass into test_CalcBMI
@pytest.mark.parametrize("feet, inches, pounds, finalBMI", [(5, 10, 250, 36.7), (5, 3, 125, 22.7)])

# tests CalcBMI using arguments from above parametrization
def test_CalcBMI(feet, inches, pounds, finalBMI):
    assert CalcBMI(feet, inches, pounds) == finalBMI


# weight category key
# 1 - underweight
# 2 - normal weight
# 3 - overweight
# 4 - obese

# defines arguments to pass into test_ClassifyBMI
@pytest.mark.parametrize("BMI, category", [(0, -1), (0.1, 1), (9, 1), (18.4, 1), (18.5, 2), (23, 2), (24.9, 2), (25, 3), (27, 3), (29.9, 3), (30, 4)])

# tests ClassifyBMI using arguments from above parametrization
def test_ClassifyBMI(BMI, category):
    assert ClassifyBMI(BMI) == category

# def geninputs1():
#     inputs = ["5", "4", "100"]

#     for item in inputs:
#         yield item

# GEN1 = geninputs1()

# def test_main1(monkeypatch, capsys):
#     monkeypatch.setattr('builtins.input', lambda _: next(GEN1))
#     main()
#     captured_stdout, captured_stderr = capsys.readouterr()
#     assert captured_stdout.strip() == "Enter in your height and weight measurements below...\nBMI: 17.6\nCategory: Underweight"