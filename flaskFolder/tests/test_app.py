# File containing E2E tests for Flask webpage

import pytest
import requests

# E2E test that verifies page is up and running
def test_page_status(client):
    requests.post(
        "http://localhost:5000/"
    )
    response = requests.get(
        "http://localhost:5000/index"
    )

    assert response.status_code == 200


@pytest.mark.parametrize("feetInput, inchesInput, poundsInput, finalBMI, classification", 
    [(5, 4, 100, 17.6, "underweight"), (5, 3, 125, 22.7, "normal weight"), (6, 0, 200, 27.8, "overweight"), 
    (5, 10, 250, 36.7, "obese")])

# E2E test that verifies page displays correct results given specified input
def test_inputs(client, feetInput, inchesInput, poundsInput, finalBMI, classification):
    
    # passes in feetInput, inchesInput, poundsInput
    landing = client.post("/index", method="POST", data = { "feetInput" : feetInput, "inchesInput" : inchesInput, "poundsInput" : poundsInput })
    html = landing.data.decode()

    # searches for finalBMI and classification in the page's html
    assert str(finalBMI) in html
    assert str(classification) in html
        
    