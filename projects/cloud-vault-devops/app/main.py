from fastapi import FastAPI
import os

app = FastAPI(title="Cloud Vault API", version="1.0.0")

@app.get("/")
def read_root():
    return {
        "status": "healthy",
        "service": "Cloud Vault API",
        "environment": os.getenv("APP_ENV", "development")
    }

@app.get("/healthz")
def health_check():
    return {"status": "ok"}
