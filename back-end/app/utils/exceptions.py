from fastapi import HTTPException

def exception_400_client_error(text:str) -> HTTPException:
    return HTTPException(status_code=400, detail=text)

def exception_401_unauthorized(text: str) -> HTTPException:
    return HTTPException(status_code=401, detail=text)

def exception_404_not_found(text:str) -> HTTPException:
    return HTTPException(status_code=404, detail=text)
