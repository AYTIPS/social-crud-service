from fastapi import FastAPI, Response, status, HTTPException , Depends,  APIRouter
from typing import Optional,List
from sqlalchemy.orm import Session
from ..import models,schemas, oauth2
from ..database import engine , get_db
from sqlalchemy import func

router = APIRouter(
   prefix="/posts",
   tags = ['Posts']
)

@router.get('/', response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db),  current_user : int = Depends(oauth2.get_current_user), Limit: int = 10, skip:int = 0, search: Optional[str] = ""):
   #cursor.execute(""" SELECT * FROM posts """)
   #posts = cursor.fetchall()
   #posts =  db.query(models.Post).filter(models.Post.title.contains(search)).limit(Limit).offset(skip).all()

   post = db.query(models.Post, func.count(models.Vote.post_id).label("VOTES")).join(models.Vote,models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(Limit).offset(skip)

   return  post



@router.post("/", status_code=status.HTTP_201_CREATED, response_model= schemas.Post)
def create_posts(post:schemas.PostCreate, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
   #cursor.execute(''' INSERT INTO posts (title, content , published )  VALUES (%s, %s, %s) RETURNING *''',(post.title, post.content, post.published))
   #NEW_POST = cursor.fetchone()
   #conn.commit()
   print(current_user)
   NEW_POST= models.Post( owner_id = current_user.id, **post.dict())
   db.add(NEW_POST)
   db.commit()
   db.refresh(NEW_POST)
   return  NEW_POST 


@router.get("/{id}", response_model=schemas.PostOut)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
   #cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id)))
   #test = cursor.fetchone()
  # print(test)
  # post = test

#post = db.query(models.Post).filter(models.Post.id == id).first()
   post = db.query(models.Post, func.count(models.Vote.post_id).label("VOTES")).join(models.Vote,models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()

   print(current_user)

   if not post:
       raise   HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"post with id: {id} was not found ")
   return  post



@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db:Session=Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
   post_query = db.query(models.Post).filter(models.Post.id == id)
   post = post_query.first()

   if post.first() == None:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details=f"post with id : {id} does not exist")
   
   if post.owner_id != current_user.id:
      raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not Authorized to perform this action")
   
   post.delete(synchronize_session=False)
   db.commit()

   return Response(status_code=status.HTTP_204_NO_CONTENT)

