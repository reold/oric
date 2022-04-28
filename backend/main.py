from fastapi import FastAPI, Request, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse

from defaults import uploads_db, uploads_drive


app = FastAPI()
app.mount("/assets",
          StaticFiles(directory="templates/dist/assets"), name="assets")

templates = Jinja2Templates(directory="templates/dist")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/contribute")
async def api_contribute(file: UploadFile = File(...)):
    print(file)
    uploads_drive.put(file.filename, file.file)
    return {"details": "success"}
