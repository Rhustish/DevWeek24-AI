import os
from fastapi import FastAPI,UploadFile
from fastapi.middleware.cors import CORSMiddleware
import shutil
import pdfhandler
import main


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/hc",status_code=200)
def healthcheck():

    return "OK"

@app.post("/ep",status_code=200)
async def resolver(file:UploadFile,count:int):
    with open(file.filename,'wb') as buffer:
        shutil.copyfileobj(file.file, buffer);
    pdfbuffer = pdfhandler.loadPdf(file.filename)
    prompt = ""
    for element in pdfbuffer:
        tempdict = element.dict()
        prompt+=tempdict['page_content']
        prompt+=" "
    out = await main.operate(count , prompt)
    os.remove(file.filename)
    return out
    
    