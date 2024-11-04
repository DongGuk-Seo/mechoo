from schemas.recommendation import RecommendByFlavorRequest, RecommendByIngredientRequest, RecommendByCountryRequest, RecommendByMenuTypeRequest
from api.deps import SessionDep

class RecommendationService:
    
    async def recommend_by_flavor(self, db: SessionDep, obj_in: RecommendByFlavorRequest) -> None:
        #TODO : ADD LOGIC
        return
    
    async def recommend_by_ingredient(self, db: SessionDep, obj_in: RecommendByIngredientRequest) -> None:
        #TODO : ADD LOGIC
        return
    
    async def recommend_by_country(self, db: SessionDep, obj_in: RecommendByCountryRequest) -> None:
        #TODO : ADD LOGIC
        return
    
    async def recommend_by_menu_type(self, db: SessionDep, obj_in: RecommendByMenuTypeRequest) -> None:
        #TODO : ADD LOGIC
        return
    