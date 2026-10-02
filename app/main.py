import os
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(
    title="Cloud Vault API",
    description="Zero-Knowledge Cloud Vault Backend Service",
    version="1.0.0"
)

class VaultData(BaseModel):
    secret_key: str
    encrypted_payload: str

vault_storage = {}

@app.get("/")
def read_root():
    return {"status": "healthy", "service": "Cloud Vault API"}

@app.post("/api/vault/store", status_code=status.HTTP_201_CREATED)
def store_vault(data: VaultData):
    vault_storage[data.secret_key] = data.encrypted_payload
    return {"message": "Data successfully stored in vault"}

@app.get("/api/vault/{secret_key}")
def get_vault(secret_key: str):
    payload = vault_storage.get(secret_key)
    if not payload:
        raise HTTPException(status_code=404, detail="Vault entry not found")
    return {"secret_key": secret_key, "encrypted_payload": payload}
