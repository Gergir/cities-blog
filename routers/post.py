from typing import Annotated

from fastapi import APIRouter, Body
from models.post import Post


router = APIRouter(prefix="/post", tags=["post"])


@router.get("/all")
def get_all_posts():
    return {"message": "fetching all posts"}


@router.get("/{post_id}")
def get_post(post_id: int):
    return {"post_id": post_id}


@router.post("/new")
def create_post(post: Annotated[Post, Body()]):
    return post


@router.patch("/update/{post_id}")
def update_post(post_id: int, post: Annotated[Post, Body()]):
    return {
        "post_id": post_id,
        "post": post
    }


@router.delete("/delete/{post_id}")
def delete_post(post_id):
    return {"message": f"post with id {post_id} deleted"}