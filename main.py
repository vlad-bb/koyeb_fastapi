import uvicorn
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from src.routes import contacts, tags

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(contacts.router, prefix="/api")
app.include_router(tags.router, prefix="/api/1")


@app.get("/")
def read_root():
    return {"massage": "Contacts API"}


@app.get("/health_check", response_class=HTMLResponse)
async def read_item(request: Request):
    ip = request.headers.get('x-forwarded-for')
    print(f'IP: {ip}')
    print("Route /health_check was started")
    return templates.TemplateResponse(
        request=request, name="index.html", context={"ip": ip})


if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
