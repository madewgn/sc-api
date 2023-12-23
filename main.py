from fastapi import *
import trial

app = FastAPI()

@app.get("/")
async def index():
    return trial.trial_tr()
