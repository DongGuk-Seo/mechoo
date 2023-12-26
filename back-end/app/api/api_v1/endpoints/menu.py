from typing import Optional, Union

from fastapi import APIRouter, Request, HTTPException, Response
from crud import menu, menu_detail
from api.deps import SessionDep
from models.menu import Menu
from schemas.menu import MenuCreate, MenuUpdate, MenuOutput
from schemas.menu_detail import MenuDetailCreate, MenuDetailOutput, MenuDetailUpdate
from core.utils import exception_400_already_exist, exception_404_not_found

router = APIRouter()

@router.post("")
async def create_menu(session: SessionDep, menu_in: MenuCreate) -> MenuOutput:
    menu_model = menu.create(db=session, obj_in=menu_in)
    return MenuOutput(**menu_model.__dict__)

@router.put("/summary")
async def update_summary(session: SessionDep, menu_in: MenuUpdate) -> MenuOutput:
    menu_model = menu.get_menu_by_id(db=session, id=menu_in.id)
    if menu_model:
        new_menu = menu.update(db=session, db_obj=menu_model, obj_in= menu_in)
        return MenuOutput(**new_menu.__dict__)
    raise exception_404_not_found("존재하지 않는 메뉴 입니다.")

@router.post("/detail")
async def create_menu_detail(session: SessionDep, menu_detail_in: MenuDetailCreate) -> MenuDetailOutput:
    if menu.get_menu_by_id(db=session,id=menu_detail_in.menu_id):
        menu_detail.valid_is_exist(db=session,menu_id=menu_detail_in.menu_id)
        menu_detail_model = menu_detail.create(db=session, obj_in=menu_detail_in)
        return MenuDetailOutput(**menu_detail_model.__dict__) 
    raise exception_404_not_found("존재하지 않는 메뉴 입니다.")

@router.put("/detail")
async def update_menu_detail(session: SessionDep, menu_detail_in: MenuDetailUpdate) -> MenuDetailOutput:
    if menu.get_menu_by_id(db=session,id=menu_detail_in.menu_id):
        menu_detail_model = menu_detail.get_menu_detail_by_menu_id(db=session, menu_id=menu_detail_in.menu_id)
        if menu_detail_model:
            new_menu_detail = menu_detail.update(db=session,db_obj=menu_detail_model, obj_in=menu_detail_in)
            return MenuDetailOutput(**new_menu_detail.__dict__)
        raise exception_404_not_found("존재하지 않는 메뉴 세부정보 입니다.")
    raise exception_404_not_found("존재하지 않는 메뉴 입니다.")
    