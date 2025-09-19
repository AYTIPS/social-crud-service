from sqlalchemy import create_engine,text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import time 
import psycopg2
from psycopg2.extras  import RealDictCursor
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
   db = SessionLocal()
   try:
      yield db
   finally:
      db.close() 

def ping_db() -> tuple[bool, str]:
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return True, "DB connection OK"
    except SQLAlchemyError as e:
        return False, f"DB connection FAILED: {e.__class__.__name__}: {e}"

#while True:
  # try:
           # conn = psycopg2.connect(host='localhost', database='Fastapi', user='postgres', password = 'GA05niyu#', cursor_factory= RealDictCursor)
           # cursor = conn.cursor()
          #  print(" Database connection was successful")
         #   break
   #except Exception as error:
      #   print("connection to database failed ")
       #  print("Error", error)
        # time.sleep(2)
