# Description: pytest test file for the web_service.py file.
# Parameters: None
# Return value: None
# Path: test_web_service.py

from web_service import app
import json

def test_flood():
    with app.test_client() as client:
        response = client.post('/flood', data=json.dumps(
            {
                'originalGrid': [['#000000', '#000000', '#000000'], ['#000000', '#000000', '#000000'], ['#000000', '#000000', '#000000']],
                'cellPosition': [0, 0],
                'newColor': '#000000'
            }
        ), content_type='application/json')
        assert response.status_code == 201
        assert response.json['floodedGrid'] == 'Flooded grid'

def test_flood_no_json():
    with app.test_client() as client:
        response = client.post('/flood')
        assert response.status_code == 400

def test_flood_no_originalGrid():
    with app.test_client() as client:
        response = client.post('/flood', data=json.dumps(
            {
                'cellPosition': [0, 0],
                'newColor': '#000000'
            }
        ), content_type='application/json')
        assert response.status_code == 400

def test_flood_no_cellPosition():
    with app.test_client() as client:
        response = client.post('/flood', data=json.dumps(
            {
                'originalGrid': [['#000000', '#000000', '#000000'], ['#000000', '#000000', '#000000'], ['#000000', '#000000', '#000000']],
                'newColor': '#000000'
            }
        ), content_type='application/json')
        assert response.status_code == 400

def test_flood_no_newColor():
    with app.test_client() as client:
        response = client.post('/flood', data=json.dumps(
            {
                'originalGrid': [['#000000', '#000000', '#000000'], ['#000000', '#000000', '#000000'], ['#000000', '#000000', '#000000']],
                'cellPosition': [0, 0]
            }
        ), content_type='application/json')
        assert response.status_code == 400

# This test is executed from the command line using the command: pytest test_web_service.py