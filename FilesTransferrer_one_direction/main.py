# Created by Ken Yeung
# C:\Windows\System32\drivers\etc domain = ken.server
# pip install python-multipart
import uvicorn
from fastapi import FastAPI, Form, UploadFile, File
from fastapi.responses import HTMLResponse, PlainTextResponse
import script.kit as kit
from typing import List, Optional
import aiofiles
import os
import traceback #traceback.print_exception(*sys.exc_info())
import sys
from script.ip import get_ip_address
from script.get_path import target_path
from script.convert_path import convert_path
from script.qrcode import qrcode
# from time import sleep
# from multiprocessing import Process
# import multiprocessing

# POST http://192.168.0.122/uploadfiles 422 (Unprocessable Entity)
# 400

try:
    ip = get_ip_address()

    print(f"Running on: http://{ip}")

    path = target_path()
    path = os.path.realpath(path)
    path = convert_path(path)

    os.startfile(path)
    qrcode(f"http://{ip}")

except:
    traceback.print_exception(*sys.exc_info())

app = FastAPI(debug=True)

@app.get("/")
async def main():
    return HTMLResponse(kit.html()) # {"message": "WiFi Host worked"}

@app.get("/weed_master/{name}")
async def master(name: str):
    return {"message": f"Hello {name}"}

@app.get("/favicon.ico")
async def favicon():
    return {"detail": None}

@app.get("/cdn/{script}", response_class=PlainTextResponse)
async def get_cdn(script: str):
    try:
        return kit.cdn(script)
    except Exception as e:
        sys.stdout.write(f"CDN Err: {e}\n")
        return "Bad requests"

@app.post("/uploadfiles")
async def catch_file(files: UploadFile = File(...)):
    file_fullname = files.filename.split(".")
    file_type = file_fullname[-1]
    sys.stdout.write("="*54 + "\n")
    filepath = rf"{path}/{files.filename}"
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    async with aiofiles.open(filepath, 'wb') as out_file:
        content = await files.read()
        await out_file.write(content) # Saving files
        if len(file_fullname) > 1: # Normal type
            sys.stdout.write(f"Filename: {'.'.join(file_fullname[:-1])}\n")
            sys.stdout.write(f"File type: {file_type}\n")
        else: # No File type
            sys.stdout.write(f"Filename: {files.filename}\n")
            sys.stdout.write("File type: No File type inputed\n")
        sys.stdout.write("="*54 + "\n")
    return {"result": True}

# @app.on_event("startup")
# async def startup_event():
#     logger = logging.getLogger("uvicorn.access")
#     handler = logging.StreamHandler()
#     handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
#     logger.addHandler(handler)

if __name__ == "__main__":
    try:
        # manager = multiprocessing.Manager()
        # shared_list = manager.list()
        # pool = multiprocessing.Pool()

        # pool.apply_async(sys.stdout.write(f"Please Go To: http://{ip}"))
        # pool.apply_async(uvicorn.run(app, host = "0.0.0.0", port = 80, log_level="info"))

        # pool.close()
        # pool.join()

        # sys.stdout.write(f"Please Go To: http://{ip}")

        log_config = uvicorn.config.LOGGING_CONFIG
        log_config["formatters"]["access"]["fmt"] = "%(asctime)s - - %(levelname)s - %(message)s"
        log_config["formatters"]["default"]["fmt"] = "%(asctime)s - " + f"Running on: http://{ip}" + " - %(levelname)s - %(message)s"

        uvicorn.run(app, host = "0.0.0.0", port = 80, log_config=log_config)
        input("Push Enter to Quit: ")
        # uvicorn.run(app, host = "0.0.0.0", port = 80, log_level="info")
    except:
        traceback.print_exception(*sys.exc_info())
        input()