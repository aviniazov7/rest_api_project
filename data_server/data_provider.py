def get_status():
    return {"status": "OK", "service": "Data Server", "version": "1.0"}

def get_info():
    return {
        "info": "Welcome to the API service.",
        "description": "This endpoint requires authentication.",
        "author": "OpenAI"
    }

def get_data():
    return {
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ]
    }
