from fastapi import APIRouter
from models.users import User

router = APIRouter()

users_db = []

@router.post("/", response_model=User)
def create_user(user: User):
    users_db.append(user)
    return user

@router.get("/", response_model=list[User])
def list_users():
    return users_db
