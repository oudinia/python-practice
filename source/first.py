import uvicorn
from fastapi import FastAPI

app: FastAPI = FastAPI(debug=True)


@app.get("/")
async def root():
    return {"message": "Hello Fast Api"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
