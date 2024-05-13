# main/api/routes/posts.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from main.database import get_db
from main.models.posts import Post
from main.models.users import User
from main.controllers.schemas import PostCreate, Post as PostSchema
from main.services import auth_service
from typing import List

router = APIRouter()

def get_current_user(db: Session = Depends(get_db), token: str = Depends(auth_service.oauth2_scheme)):
    return auth_service.get_current_user(db=db, token=token)

@router.post("/posts/", response_model=PostSchema)
def create_post(post: PostCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    new_post = Post(**post.dict(), user_id=current_user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/posts/", response_model=List[PostSchema])
def get_posts(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(Post).filter(Post.user_id == current_user.id).all()

@router.delete("/posts/{post_id}", response_model=PostSchema)
def delete_post(post_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="You don't have permission to delete this post")
    db.delete(post)
    db.commit()
    return post
