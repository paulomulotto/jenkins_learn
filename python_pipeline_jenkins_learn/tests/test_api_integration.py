from fastapi.testclient import TestClient
from python_pipeline_jenkins_learn.main import app
import pytest

client = TestClient(app)


@pytest.mark.integtest
def test_add_handler():
    response = client.get("/add?x=10&y=2")
    assert response.status_code == 200
    assert response.json() == {"result": 12}

    response = client.get("/add?x=0&y=5")
    assert response.status_code == 200
    assert response.json() == {"result": 5}

    response = client.get("/add?x=-10&y=2")
    assert response.status_code == 200
    assert response.json() == {"result": -8}


@pytest.mark.integtest
def test_sub_handler():
    response = client.get("/sub?x=10&y=2")
    assert response.status_code == 200
    assert response.json() == {"result": 8}

    response = client.get("/sub?x=0&y=5")
    assert response.status_code == 200
    assert response.json() == {"result": -5}

    response = client.get("/sub?x=-10&y=2")
    assert response.status_code == 200
    assert response.json() == {"result": -12}


@pytest.mark.integtest
def test_mul_handler():
    response = client.get("/mul?x=10&y=2")
    assert response.status_code == 200
    assert response.json() == {"result": 20}

    response = client.get("/mul?x=0&y=5")
    assert response.status_code == 200
    assert response.json() == {"result": 0}

    response = client.get("/mul?x=-10&y=2")
    assert response.status_code == 200
    assert response.json() == {"result": -20}


class TestMul:
    @pytest.mark.integtest
    def test_div_handler(self):
        response = client.get("/div?x=10&y=2")
        assert response.status_code == 200
        assert response.json() == {"result": 5}

        response = client.get("/div?x=0&y=5")
        assert response.status_code == 200
        assert response.json() == {"result": 0}

        response = client.get("/div?x=-10&y=2")
        assert response.status_code == 200
        assert response.json() == {"result": -5}

    @pytest.mark.integtest
    def test_div_by_zero(self):
        response = client.get("/div?x=10&y=0")
        assert response.status_code == 400
        print(response.json())
        assert response.json() == {"detail": "Cannot divide by zero!"}
