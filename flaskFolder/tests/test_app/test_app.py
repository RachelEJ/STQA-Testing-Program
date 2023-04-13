import pytest
import requests
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

