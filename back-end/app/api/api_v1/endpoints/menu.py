from typing import Optional

from fastapi import APIRouter, Request, HTTPException
from crud import menu
from api.deps import SessionDep
from models.menu import Menu
from schemas.menu import MenuCreate, MenuUpdate, MenuOutput
from core.utils import exception_404_not_found

router = APIRouter()

@router.post("")
def create_menu(session: SessionDep, menu_in: MenuCreate) -> MenuOutput:
    menu_model = menu.create(db=session, obj_in=menu_in)
    res = MenuOutput(
        id=menu_model.id,
        name=menu_model.name
    )
    return res

@router.put("/summary")
def update_summary(session: SessionDep, menu_in: MenuUpdate) -> MenuOutput:
    menu_model = menu.get_menu_by_id(db=session, id=menu_in.id)
    if menu_model:
        new_menu = menu.update(db=session, db_obj=menu_model, obj_in= menu_in)
        res = MenuOutput(
            id=new_menu.id,
            name=new_menu.name
        )
        return res
    raise exception_404_not_found("존재하지 않는")