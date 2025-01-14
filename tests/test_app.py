import pytest
import subprocess
import time
from fastapi.testclient import TestClient
from main import app

@pytest.fixture(scope="module")
def start_server():
    process = subprocess.Popen(["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"])
    time.sleep(2)
    yield
    process.terminate()

client = TestClient(app)

@pytest.mark.usefixtures("start_server")
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

@pytest.mark.usefixtures("start_server")
def test_get_version():
    response = client.get("/get_version")
    assert response.status_code == 200
    assert "version" in response.json()

@pytest.mark.usefixtures("start_server")
def test_check_prime_2():
    response = client.get("/check_prime/2")
    assert response.status_code == 200
    assert response.json() == {"number": 2, "is_prime": True}

@pytest.mark.usefixtures("start_server")
def test_check_prime_3():
    response = client.get("/check_prime/3")
    assert response.status_code == 200
    assert response.json() == {"number": 3, "is_prime": True}

@pytest.mark.usefixtures("start_server")
def test_check_prime_4():
    response = client.get("/check_prime/4")
    assert response.status_code == 200
    assert response.json() == {"number": 4, "is_prime": False}

@pytest.mark.usefixtures("start_server")
def test_check_prime_5():
    response = client.get("/check_prime/5")
    assert response.status_code == 200
    assert response.json() == {"number": 5, "is_prime": True}

@pytest.mark.usefixtures("start_server")
def test_check_prime_6():
    response = client.get("/check_prime/6")
    assert response.status_code == 200
    assert response.json() == {"number": 6, "is_prime": False}

@pytest.mark.usefixtures("start_server")
def test_check_prime_7():
    response = client.get("/check_prime/7")
    assert response.status_code == 200
    assert response.json() == {"number": 7, "is_prime": True}

@pytest.mark.usefixtures("start_server")
def test_check_prime_8():
    response = client.get("/check_prime/8")
    assert response.status_code == 200
    assert response.json() == {"number": 8, "is_prime": False}

@pytest.mark.usefixtures("start_server")
def test_check_prime_9():
    response = client.get("/check_prime/9")
    assert response.status_code == 200
    assert response.json() == {"number": 9, "is_prime": False}

@pytest.mark.usefixtures("start_server")
def test_check_prime_11():
    response = client.get("/check_prime/11")
    assert response.status_code == 200
    assert response.json() == {"number": 11, "is_prime": True}
