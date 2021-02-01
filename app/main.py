from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from dotenv import load_dotenv
load_dotenv() 


import api.service_1.urls as service_1
import api.service_2.urls as service_2
import api.service_3.urls as service_3


app = FastAPI()

app.include_router(service_1.router, prefix="/api/v1/service_1")
app.include_router(service_2.router, prefix="/api/v1/service_2")
app.include_router(service_3.router, prefix="/api/v1/service_3")


# Mounting default Vue files after running npm run build 
app.mount("/css", StaticFiles(directory="ui/vue-app/dist/css"), name="css")
app.mount("/img", StaticFiles(directory="ui/vue-app/dist/img"), name="img")
app.mount("/js", StaticFiles(directory="ui/vue-app/dist/js"), name="js")
templates = Jinja2Templates(directory="ui/vue-app/dist/")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



# pipenv lock -r > requirements.txt
# uvicorn main:app --reload --host 0.0.0.0 --port 3000
