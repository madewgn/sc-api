from fastapi import *


app = FastAPI()

@app.get("/")
async def index():
    return "ini index"
