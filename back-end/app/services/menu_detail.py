from crud import menu, menu_detail
from api.deps import SessionDep
from schemas.menu_detail import MenuDetailCreate, MenuDetailUpdate
from utils.exceptions import exception_400_client_error, exception_404_not_found

class MenuDetailService:
    async def is_existed_menu_by_id(self, db: SessionDep, id: int):
        return menu.get_menu_by_id(db=db, id=id)
    
    async def is_existed_menu_detail_by_menu_id(self, db: SessionDep, menu_id: int):
        return menu_detail.get_menu_detail_by_menu_id(db=db, menu_id=menu_id)
    
    async def valid_create_menu_detail(self, db: SessionDep, menu_id: int):
        if not await self.is_existed_menu_by_id(db=db, id=menu_id):
            raise exception_404_not_found("존재하지 않는 메뉴입니다.")
        if await self.is_existed_menu_detail_by_menu_id(db=db, menu_id=menu_id):
            raise exception_400_client_error("이미 존재하는 메뉴 상세정보입니다.")
        
    async def valid_update_menu_detail(self, db: SessionDep, menu_id: int):
        if not await self.is_existed_menu_by_id(db=db, id=menu_id):
            raise exception_404_not_found("존재하지 않는 메뉴입니다.")
        menu_detail_model = await self.is_existed_menu_detail_by_menu_id(db=db, menu_id=menu_id)
        if not menu_detail_model:
            raise exception_404_not_found("존재하지 않는 메뉴 상세정보입니다.")
        return menu_detail_model
        
    async def create_menu_detail(self, db: SessionDep, obj_in: MenuDetailCreate):
        await self.valid_create_menu_detail(db=db, menu_id=obj_in.menu_id)
        menu_detail_model = menu_detail.create(db=db, obj_in=obj_in)
        return menu_detail_model
    
    async def update_menu_detail(self, db: SessionDep, obj_in: MenuDetailUpdate):
        menu_detail_model = await self.valid_update_menu_detail(db=db, menu_id=obj_in.menu_id)
        updated_menu_detail_model = menu_detail.update(db=db, db_obj=menu_detail_model, obj_in=obj_in)
        return updated_menu_detail_model