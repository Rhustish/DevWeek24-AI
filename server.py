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
async def resolver(file:UploadFile):
    with open(file.filename,'wb') as buffer:
        shutil.copyfileobj(file.file, buffer);
    prompt = pdfhandler.loadPdf(file.filename)
    count = 200
    print(prompt)
    main.operate(count,prompt)
    os.remove(file.filename)
    
    