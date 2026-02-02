from fastapi.testclient import TestClient
import pytest
import math
from random import randint
from application.main import app
client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "hello world"

def test_square():
    response = client.get("/twice/2")
    res_json = response.json()
    expected = 8
    assert res_json == expected

list_of_numbers = [randint(1, 100) for i in range(10)]


@pytest.mark.parametrize("number", list_of_numbers)
def test_return_square_twice(number : int):
    response = client.get(f"/twice/{number}")
    assert response.status_code == 200
    assert response.json() == math.pow(number, 2)* 2