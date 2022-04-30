from distutils.command.upload import upload
from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse

from uuid import uuid4 as uuid
from datetime import datetime

from defaults import uploads_db, uploads_drive


app = FastAPI()
app.mount("/assets",
          StaticFiles(directory="templates/dist/assets"), name="assets")

templates = Jinja2Templates(directory="templates/dist")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/add")
async def api_add(file: UploadFile = File(...), title: str = Form(...), publisher: str = Form(...)):

    len_uploads_db = len(uploads_db.fetch())

    print(len_uploads_db)

    file_extention = file.filename.split(".")[-1]

    upload_info = {"title": title, "publisher": publisher, "content_filename": f"{uuid()}.{file_extention}",
                   "index": len_uploads_db}

    uploads_db.insert(upload_info)
    uploads_drive.put(upload_info["content_filename"], file.file)
    return {"details": "success"}


# @app.get("/api/get")
# @app.get("/api/read")
# async def api_read():
