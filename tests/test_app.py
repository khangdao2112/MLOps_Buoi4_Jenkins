import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}  

@pytest.mark.asyncio
async def test_get_version():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.get("/get_version")
    assert response.status_code == 200
    assert "version" in response.json()

@pytest.mark.asyncio
async def test_check_prime_2():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.get("/check_prime/2")
    assert response.status_code == 200
    assert response.json() == {"number": 2, "is_prime": True}

@pytest.mark.asyncio
async def test_check_prime_3():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.get("/check_prime/3")
    assert response.status_code == 200
    assert response.json() == {"number": 3, "is_prime": True}

@pytest.mark.asyncio
async def test_check_prime_4():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.get("/check_prime/4")
    assert response.status_code == 200
    assert response.json() == {"number": 4, "is_prime": False}

@pytest.mark.asyncio
async def test_check_prime_5():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.get("/check_prime/5")
    assert response.status_code == 200
    assert response.json() == {"number": 5, "is_prime": True}

@pytest.mark.asyncio
async def test_check_prime_6():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.get("/check_prime/6")
    assert response.status_code == 200
    assert response.json() == {"number": 6, "is_prime": False}

@pytest.mark.asyncio
async def test_check_prime_7():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.get("/check_prime/7")
    assert response.status_code == 200
    assert response.json() == {"number": 7, "is_prime": True}

@pytest.mark.asyncio
async def test_check_prime_8():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.get("/check_prime/8")
    assert response.status_code == 200
    assert response.json() == {"number": 8, "is_prime": False}

@pytest.mark.asyncio
async def test_check_prime_9():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.get("/check_prime/9")
    assert response.status_code == 200
    assert response.json() == {"number": 9, "is_prime": False}

@pytest.mark.asyncio
async def test_check_prime_11():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        response = await ac.get("/check_prime/11")
    assert response.status_code == 200
    assert response.json() == {"number": 11, "is_prime": True}