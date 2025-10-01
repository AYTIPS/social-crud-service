from app import schemas
import pytest
from app.config import settings
from jose import  jwt

# def test_root(client):
#     res = client.get("/")
#     print(res.json().get('message'))
#     assert res.json().get('message') =='Hello World'
#     assert res.status_code ==  200    
#SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:GA05niyu#@localhost:5432/fastapi_test'




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
    res =client.post("/users/", json={"email":"ayo1234@gmail.com", "password":"Ga05niyu"})
    new_user =schemas.UserOut(**res.json())
    assert res.status_code ==201
    assert new_user == "ayo1234@gmail.com"


def test_login_user(client, test_user):
    res = client.post("/login", data={"username": test_user['email'], "password": test_user['password']})
    LOGIN_RES = schemas.Token(**res.json())
    payload = jwt.decode(LOGIN_RES.access_token, settings.secret_key, algorithms=[settings.algorithm])
    uid = payload.get("user_id")
    assert uid == test_user['uid']
    assert LOGIN_RES.token_type == "bearer"
    assert  res.status_code == 200


@pytest.mark.pararmetrize("email, password, status_code",[ ('wrongemail@gmail.com', 'password123', 403), 
('ganiyu@gmail.com', 'GA05niyu#', 403), 
('wronemail@gmail.com', 'wrongpassword', 403), 
(None, 'GA05niyu#', 422), 
('ayo1234@gmail.com', None, 422)])

def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post("login", data={"username": test_user['email'], "password": "gwhshHAHADS"})
    assert res.status_code == status_code