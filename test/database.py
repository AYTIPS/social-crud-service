from fastapi.testclient import TestClient
import pytest
from fastapi import status
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.main import app 
from app import schemas
from app.config import settings
from app. database import get_db, Base
from alembic import command 

client = TestClient(app)

@pytest.fixture()
def session ():
    Base.metadata.create_all(bind=engine)
    #command.upgrade(head)
    Base.metadata.drop_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close() 

    
@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)       


def test_root(client):
    res = client.get("/")
    print(res.json().get('message'))
    assert res.json().get('message') =='Hello World'
    assert res.status_code ==  200    
#SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:GA05niyu#@localhost:5432/fastapi_test'

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


#def override_get_db():
#    db = TestingSessionLocal()
#    try:
#       yield db
#    finally:
#       db.close() 

# app.dependency_overrides[get_db] = override_get_db


# def test_root():
#     res = client.get("/")
#     print(res.json().get('message'))
    

def test_create_user(client):
    res =client.post("/users", json={"email":"ayo1234@gmail.com", "password":"Ga05niyu"})
    new_user =schemas.UserOut(**res.json())
    assert res.status_code ==201