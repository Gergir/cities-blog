import shutil
import string
from typing import Annotated
from fastapi import APIRouter, Body, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from models.post import Post, PostRequest, PostResponse
from services.db_service import get_db
import string
import random

router = APIRouter(prefix="/post", tags=["post"])


@router.get("/all")
def get_all_posts(db: Session = Depends(get_db)):
    db_post = db.query(Post).all()
    return db_post


@router.get("/{post_id}", response_model=PostResponse)
def get_post(post_id: int, db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail=f"Entity with id {post_id} not found")
    return db_post


@router.post("/new", response_model=PostResponse)
def create_post(post: Annotated[PostRequest, Body()], db: Session = Depends(get_db)):
    db_post = Post(**post.model_dump())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@router.post("/new/image")
def upload_image(image: UploadFile = File(...)):
    letter = string.ascii_letters
    rand_str = ''.join(random.choice(letter) for i in range(6))
    new = f"_{rand_str}."
    filename = new.join(image.filename.rsplit('.', 1))
    path = f"images/{filename}"

    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {"filename": path}

@router.patch("/update/{post_id}", response_model=PostResponse)
def update_post(post_id: int, post: Annotated[PostRequest, Body()], db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail=f"Entity with id {post_id} not found")

    for key, value in post.dict(exclude_unset=True).items():
        setattr(db_post, key, value)

    db.commit()
    db.refresh(db_post)

    return db_post


@router.delete("/delete/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail=f"Entity with id {post_id} not found")
    db.delete(db_post)
    db.commit()
    return {"message": f"post with id {post_id} deleted"}