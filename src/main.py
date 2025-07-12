from pathlib import Path

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount(f"/static", StaticFiles(directory="src/static"), name="static")
templates = Jinja2Templates(directory="src/templates")


@app.get("/", response_class=HTMLResponse, summary="Главная страница")
async def get_main(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        "main.html",
        {"request": request}
    )

@app.get("/favicon.ico", response_class=HTMLResponse, summary="Favicon")
async def get_favicon():
    return FileResponse("src/static/images/favicon.ico",
        media_type="image/x-icon")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)