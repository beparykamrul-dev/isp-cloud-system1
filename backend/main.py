from fastapi import FastAPI

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
        "offline_users": 20,
        "revenue": 55000,
        "database": "CONNECTED",
        "redis": "CONNECTED"
    }
