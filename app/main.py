from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine 
from .routers import post,user, auth, vote
from . import models  
from .config import  settings
import logging
from .import database 


#models.Base.metadata.create_all(bind=engine)
log = logging.getLogger("uvicorn.error")

origins = ["*"]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.on_event("startup")
def verify_db_on_start():
    ok, msg = database.ping_db()
    if ok:
        log.info(msg)              # you'll see this in your console
    else:
        log.error(msg)


@app.get("/")
async def root():
   return {'message': "Hello world pelumi "}






