from fastapi import *
import trial
import create
import uvicorn
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
async def tr(u,exp):
    return create.trojan(u,exp)

@app.post("/vps/vmessws")
async def vm(u,pw,exp):
    return create.vmess(u,pw,exp)

@app.post("/vps/vlessws")
async def vl(u,pw,exp):
    return create.vless(u,pw,exp)

if __name__ == "__main__":
   uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

