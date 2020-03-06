import uvicorn
from fastapi import FastAPI

app: FastAPI = FastAPI(debug=True)


@app.get("/")
async def index():
    return {"message": "Hello Fast Api"}

@app.get("/home")
async def home():
    return {"message": "Home end point"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
