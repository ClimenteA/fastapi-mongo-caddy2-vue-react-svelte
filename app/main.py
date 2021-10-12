from fastapi import FastAPI 
# from fastapi import Request
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates

# import os
# from dotenv import load_dotenv
# load_dotenv() 


import api.service_1.urls as service_1
import api.service_2.urls as service_2
import api.service_3.urls as service_3


app = FastAPI()

app.include_router(service_1.router, prefix="/api/v1/service_1")
app.include_router(service_2.router, prefix="/api/v1/service_2")
app.include_router(service_3.router, prefix="/api/v1/service_3")


@app.get("/")
async def root():
    return {"status": "FastAPI"}, 200


# Mounting default Vue files after running npm run build 
# app.mount("/dist", StaticFiles(directory="dist/"), name="dist")
# app.mount("/css", StaticFiles(directory="dist/css"), name="css")
# app.mount("/img", StaticFiles(directory="dist/img"), name="img")
# app.mount("/js", StaticFiles(directory="dist/js"), name="js")
# templates = Jinja2Templates(directory="dist")

# @app.get("/", response_class=HTMLResponse)
# async def root(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})
