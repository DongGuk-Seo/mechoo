from sqlalchemy.orm import Session

from app.models import user as user_model
from app.schemas import user as user_schemas

def get_user(db: Session, user_id:int):
    return db.query(user_model.User).filter(user_model.User.id == user_id).first()

