from src.users.models import CreateUserModel, UserModel
from src.entities.users.users import User

class UserRepository:

    def __init__(self, session_factory):
        self._session_factory = session_factory
    
    def create_user(self, create_user_model: CreateUserModel) -> UserModel:
        with self._session_factory() as session:
            user_entity = User(**create_user_model.dict())
            
            session.add(user_entity)
            session.commit()
            session.refresh(user_entity)

            return CreateUserModel.from_orm(user_entity)

