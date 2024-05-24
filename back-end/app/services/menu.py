from crud import menu
from fastapi import Response
from api.deps import SessionDep
from schemas.menu import MenuCreate, MenuUpdate
from utils.exceptions import exception_400_client_error, exception_404_not_found

class MenuService:
    
    async def create_menu(self, db: SessionDep, obj_in: MenuCreate):
        if menu.get_menu_by_name(db=db, name=obj_in.name):
            raise exception_400_client_error("이미 존재하는 메뉴입니다.")
        menu_model = menu.create(db=db, obj_in=obj_in)
        return menu_model
    
    async def update_menu(self, db: SessionDep, obj_in: MenuUpdate):
        menu_model = menu.get_menu_by_id(db=db, id=obj_in.id)
        if menu_model:
            updated_menu_model = menu.update(db=db, db_obj=menu_model, obj_in=obj_in)
            return updated_menu_model
        raise exception_404_not_found("존재하지 않는 메뉴 입니다.")
    
    async def delete_menu(self, db: SessionDep, id: int):
        menu_model = menu.delete(db=db, id=id)
        if menu_model:
            return Response("메뉴를 성공적으로 삭제했습니다.")
        raise exception_404_not_found("존재하지 않는 메뉴 입니다.")