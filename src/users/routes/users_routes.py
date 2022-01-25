from fastapi import APIRouter

from src.users.models import UserModel, CreateUserModel
from src.users.services import CreateUser

router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.post('/create', response_model=UserModel)
def create_user(create_user_model: CreateUserModel):
    service = CreateUser()
    return service.create(create_user_model)