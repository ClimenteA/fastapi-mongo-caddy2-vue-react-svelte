from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

import api.service_1.urls as service_1
import api.service_2.urls as service_2
import api.service_3.urls as service_3


from api.commun.mongo_connection import get_db



app = FastAPI()


origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(service_1.router, prefix="/api/v1/service_1")
app.include_router(service_2.router, prefix="/api/v1/service_2")
app.include_router(service_3.router, prefix="/api/v1/service_3")



@app.get("/")
async def root():
    
    db = get_db()
    
    db.MyCollection.insert_one({"message": "Mongo database works!"})

    return {"status": "FastAPI", "message": "Data was fetched!"}


















# uvicorn main:app --reload