# File containing E2E tests for Flask webpage

import pytest
import requests
from flask import request
from flaskFolder.app import app

# E2E test that verifies page is up and running
@pytest.mark.e2e
def test_page_status(client):
    requests.post(
        "http://localhost:5000/"
    )
    response = requests.get(
        "http://localhost:5000/index"
    )

    assert response.status_code == 200

# E2E test that verifies page displays correct results given specified input
@pytest.mark.e2e
def test_inputs(client):
    
    # passes in 6, 2, 160 as feetInput, inchesInput, poundsInput
    landing = client.post("/index", method="POST", data = { "feetInput" : 6, "inchesInput" : 2, "poundsInput" : 160 })
    html = landing.data.decode()

    # searches for "21.0" and "normal weight" in the page's html
    assert "21.0" in html
    assert "normal weight" in html
        
    