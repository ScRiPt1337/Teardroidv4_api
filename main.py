from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse,FileResponse,StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from starlette.exceptions import HTTPException as StarletteHTTPException
from routers.client import client
from routers.command import command
from routers.notification import notification
from routers.auth import auth
from pathlib import Path
import requests,io
# from config import USER_AGENT


app = FastAPI(
    redoc_url=None,
    docs_url=None
)

origins = ["*"]
app.include_router(client.router)
app.include_router(command.router)
app.include_router(notification.router)
app.include_router(auth.router)
auth.check_auth()
app.mount("/v4", StaticFiles(directory="build", html=True), name="build")
# app.mount("/static", StaticFiles(directory="static", html=True), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
REDIRCT_URL = "https://en.wikipedia.org/wiki/Special:Random?action=render"


class Settings(BaseModel):
    authjwt_secret_key: str = "jaihind"


@AuthJWT.load_config
def get_config():
    return Settings()


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    if exc.status_code == 404:
        return HTMLResponse(open("build/index.html", "rb").read())
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})


@app.route("/v4")
async def index(request: Request):
    return HTMLResponse(open("build/index.html", "rb").read())


@app.get("/")
async def root(request: Request):
    return RedirectResponse(REDIRCT_URL)

@app.get("/static/{file_path:path}")
async def serve_static_file(file_path: str):
    git_host_url = "https://raw.githubusercontent.com/ScRiPt1337/Teardroidv4_api/NanoEffect/static/"
    final_url = git_host_url + file_path
    data = requests.get(final_url).content
    if file_path.endswith((".jpeg", ".png")):
        return StreamingResponse(io.BytesIO(data), media_type="image/jpeg")
    elif file_path.endswith(".svg"):
        return StreamingResponse(io.BytesIO(data),media_type="image/svg+xml")
    else:
        return HTMLResponse(data)
