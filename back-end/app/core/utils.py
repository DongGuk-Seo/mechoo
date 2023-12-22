from fastapi import HTTPException

def exception_404_not_found(text:str) -> HTTPException:
    return HTTPException(404, text)

def exception_401_unauthorized(text: str) -> HTTPException:
    return HTTPException(401, text)