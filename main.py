from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello_world"}

# Route để lấy phiên bản
@app.get("/get_version")
def get_version():
    return {"version": "1.0.0"}

# Hàm kiểm tra số nguyên tố
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Route để kiểm tra số nguyên tố
@app.get("/check_prime/{number}")
def check_prime(number: int):
    if is_prime(number):
        return {"number": number, "is_prime": True}
    else:
        return {"number": number, "is_prime": False}

# Comment for changes
# Comment for another change
# Another comment for another change