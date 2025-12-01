import os
from kinde_sdk.auth.oauth import OAuth
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
load_dotenv()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SESSION_SECRET", "dev-secret-key"),
)

oauth = OAuth(
    framework="fastapi",
    app=app
)

@app.get("/")
async def hello():
   return ""
@app.get("/api/login")
async def login(req: Request): 
    url = await oauth.login()
    return RedirectResponse(url=url)

@app.get("/api/register")
async def  register(req: Request): 
    url = await oauth.register()
    return RedirectResponse(url=url)

@app.get("/api/user")
async def user(request: Request): 
    if not oauth.is_authenticated(request): 
        return RedirectResponse(await oauth.login)
    return oauth.get_user_info(request)