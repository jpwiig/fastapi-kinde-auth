from kinde_sdk import OAuth
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse



app = FastAPI()
oauth = OAuth(
    framework="fastapi", 
    app=app
)

@app.get("/api/login")
async def login(req: Request): 
    url = await oauth.login()
    return RedirectResponse(url=url) 