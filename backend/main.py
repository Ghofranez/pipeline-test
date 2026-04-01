from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI fonctionne "}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Bonjour {name}"}