from fastapi import Depends, HTTPException, Header
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

VALID_API_KEY = "my-secret-api-key"

security = HTTPBasic()

def verify_basic_auth(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, VALID_USERNAME)
    correct_password = secrets.compare_digest(credentials.password, VALID_PASSWORD)
    if not (correct_username and correct_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return True

def verify_api_key(x_api_key: str = Header(...)):
    if not secrets.compare_digest(x_api_key, VALID_API_KEY):
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return True
