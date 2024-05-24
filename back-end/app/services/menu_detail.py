from crud import menu, menu_detail
from models.menu import MenuDetail
from fastapi import Response
from api.deps import SessionDep
from schemas.menu_detail import MenuDetailCreate, MenuDetailUpdate
from utils.exceptions import exception_400_client_error, exception_404_not_found

class MenuDetailService:
        
    async def create_menu_detail(self, db: SessionDep, obj_in: MenuDetailCreate) -> MenuDetail:
        if not menu.get_menu_by_id(db=db, id=obj_in.menu_id):
            raise exception_404_not_found("존재하지 않는 메뉴입니다.")
        if menu_detail.get_menu_detail_by_menu_id(db=db, menu_id=obj_in.menu_id):
            raise exception_400_client_error("이미 존재하는 메뉴 상세정보입니다.")
        menu_detail_model = menu_detail.create(db=db, obj_in=obj_in)
        return menu_detail_model
    
    async def update_menu_detail(self, db: SessionDep, obj_in: MenuDetailUpdate) -> MenuDetail:
        if not menu.get_menu_by_id(db=db, id=obj_in.menu_id):
            raise exception_404_not_found("존재하지 않는 메뉴입니다.")
        menu_detail_model = menu_detail.get_menu_detail_by_menu_id(db=db, menu_id=obj_in.menu_id)
        if not menu_detail_model:
            raise exception_404_not_found("존재하지 않는 메뉴 상세정보입니다.")
        updated_menu_detail_model = menu_detail.update(db=db, db_obj=menu_detail_model, obj_in=obj_in)
        return updated_menu_detail_model
    
    async def delete_menu_detail(self, db: SessionDep, id: int) -> Response:
        result = menu.delete(db=db, id=id)
        if result:
            return Response("상세 메뉴를 성공적으로 삭제했습니다.")
        raise exception_404_not_found("존재하지 않는 메뉴 입니다.")