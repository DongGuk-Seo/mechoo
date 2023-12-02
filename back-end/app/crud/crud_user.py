from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session
from core.security import get_password_hash, verify_password
from crud.base import CRUDBase
from models import user as user_model
from schemas import user as user_schemas

# class CRUDUser(CRUDBase[user_model.User, user_schemas.UserCreate, ])