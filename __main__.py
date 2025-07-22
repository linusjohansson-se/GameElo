import uvicorn
from startup import initialize_app

if __name__ == "__main__":
    app = initialize_app()   
    uvicorn.run(app, host="0.0.0.0", port=8000)