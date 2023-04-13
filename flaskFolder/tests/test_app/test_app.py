import pytest
import requests
import json
from flask import request
from flaskFolder.app import app

@pytest.mark.e2e
def test_page_status(client):
    requests.post(
        "http://localhost:5000/"
    )
    response = requests.get(
        "http://localhost:5000/index"
    )

    assert response.status_code == 200

@pytest.mark.e2e
def test_inputs(client):
    
    landing = client.post("/index", method="POST", data = { "feetInput" : 6, "inchesInput" : 2, "poundsInput" : 160 })
    html = landing.data.decode()

    assert "21.0" in html
    assert "normal weight" in html
        
    