from fastapi import APIRouter, Depends
from .auth import verify_basic_auth, verify_api_key
from . import data_provider

router = APIRouter()

@router.get("/status")
def public_status():
    return data_provider.get_status()

@router.get("/info", dependencies=[Depends(verify_basic_auth)])
def protected_info():
    return data_provider.get_info()

@router.get("/data", dependencies=[Depends(verify_api_key)])
def protected_data():
    return data_provider.get_data()
