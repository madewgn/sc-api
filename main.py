from fastapi import *
import trial
import create
app = FastAPI()

@app.get("/vps/trialvlessws")
async def index():
    return trial.trial_vl()


@app.get("/vps/trialtrojanws")
async def trialtr():
    return trial.trial_tr()

    

@app.get("/vps/trialvmessws")
async def trialws():
    return trial.trial_vm()



@app.get("/vps/trialssh")
async def trialssh():
    return trial.trial_ssh()



# create

@app.post("/vps/sshvpn")
async def sshv():
    return create.ssh()


@app.post("/vps/trojanws")
async def tr(u,pw,exp):
    return create.trojan(u,pw,exp)
