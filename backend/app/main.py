from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Daily Task Management Backend is running 🚀"}
