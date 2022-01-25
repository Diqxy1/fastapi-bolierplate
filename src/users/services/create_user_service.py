from src.config.database import db
from src.users.models import CreateUserModel, UserModel
from src.users.repositories import UserRepository

class CreateUser:

    def __init__(self):
        self._repository = UserRepository(session_factory=db.session)
    
    def create(self, create_user_model: CreateUserModel) -> UserModel:
        create = self._create(create_user_model)
        return create
    
    def _create(self, create_user_model: CreateUserModel) -> UserModel:
        create_user = self._repository.create_user(create_user_model)
        return create_user