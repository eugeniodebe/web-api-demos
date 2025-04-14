from fastapi import FastAPI

import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola desde FastAPI 🚀"}

@app.get("/ping")
def ping():
    return {"status": "ok"}



if __name__ == "__main__":
    uvicorn.run(app, port=8080,host='0.0.0.0')
