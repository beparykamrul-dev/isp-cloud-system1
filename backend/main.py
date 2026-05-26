from fastapi import FastAPI

app = FastAPI(title="ISP CLOUD SYSTEM")

@app.get("/")
def home():
    return {"status": "LIVE ISP SYSTEM"}
