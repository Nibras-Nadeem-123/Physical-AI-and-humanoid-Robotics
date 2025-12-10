import os
from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=True)

def get_api_key(api_key: str = Security(api_key_header)):
    if api_key == os.environ.get("API_KEY"):
        return api_key
    raise HTTPException(
        status_code=403, detail="Could not validate credentials"
    )
