from fastapi import FastAPI
from auth import check_user

app = FastAPI(title="ISP CLOUD SYSTEM")

@app.get("/")
def home():
    return {
        "status": "LIVE",
        "system": "ISP CLOUD"
    }

@app.get("/dashboard")
def dashboard():
    return {
        "online_users": 120,
        "offline_users": 25,
        "revenue": 50000
    }

@app.post("/login")
def login(username: str, password: str):

    user = check_user(username, password)

    return {
        "status": "SUCCESS",
        "role": user["role"]
    }
