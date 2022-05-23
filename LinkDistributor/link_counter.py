# Created by Ken Yeung

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse, StreamingResponse, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import og.og as og
from io import BytesIO
import traceback #traceback.print_exception(*sys.exc_info())
import sys
from PIL import Image

host = "0.0.0.0"
port = 2196
credentials = False
methods = ["GET"]
headers = ["*"]
origins = []

app = FastAPI(debug=False, redoc_url=None)

app.mount("/css", StaticFiles(directory="web/css"), name="css")

@app.get("/")
async def main():
    return HTMLResponse(og.html("index.html"))

@app.get("/result")
async def get_result(pw:str=""):
    if pw == "mymagic":
        return og.glob_file()
    else:
        return "Bad requests"

@app.get("/pages/{page}")
async def serve_pages(page:str, store:str=""):
    if page != "index.html":
        if store == "ios" or store == "android":
            og.recorder(store)
        return HTMLResponse(og.html(page))
    else:
        return "Bad requests"

@app.get("/cdn/{script}", response_class=PlainTextResponse)
async def cdn_deliver(script: str):
    try:
        res = og.deliver("js", script)
        return res
    except Exception as e:
        print("Requests: CDN Error")
        return "Bad requests"

@app.get("/icon/{image}") #Get img by path
async def get_img(image:str):
    try:
        typepo = image.split(".")[1]

        image = Image.open(f"./resources/icon/{image}")
        filtered_image = BytesIO()
        image.save(filtered_image, typepo)
        filtered_image.seek(0)
        return StreamingResponse(filtered_image, media_type=f"image/{typepo}")

    except Exception as err:
        traceback.print_exception(*sys.exc_info())
        return "Bad Requests"

app = CORSMiddleware(
    app=app,
    allow_origins=origins,
    allow_credentials=credentials,
    allow_methods=methods,
    allow_headers=headers,
)

if __name__ == "__main__":
    uvicorn.run(app, host = host, port = port, log_level="info")