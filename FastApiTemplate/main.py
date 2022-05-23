# Created by Ken Yeung
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import og.og as og

host = "0.0.0.0"
port = 80
credentials = False
methods = ["GET"]
headers = ["*"]
origins = []

app = FastAPI(debug=False, docs_url="/documentation", redoc_url=None)

app.mount("/css", StaticFiles(directory="web/css"), name="css")

@app.get("/")
async def main():
    return HTMLResponse(og.html("index.html"))

@app.get("/pages/{page}")
async def serve_pages(page:str):
    if page != "index.html":
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

app = CORSMiddleware(
    app=app,
    allow_origins=origins,
    allow_credentials=credentials,
    allow_methods=methods,
    allow_headers=headers,
)

if __name__ == "__main__":
    uvicorn.run(app, host = host, port = port, log_level="info")
