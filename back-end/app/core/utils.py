from fastapi import HTTPException, Response, Depends

def ok_204_no_content(text:str) -> Response:
    return Response(content=text, status_code=204)

def exception_400_already_exist(text:str) -> HTTPException:
    return HTTPException(status_code=400, detail=text)

def exception_404_not_found(text:str) -> HTTPException:
    return HTTPException(status_code=404, detail=text)

def exception_401_unauthorized(text: str) -> HTTPException:
    return HTTPException(status_code=401, detail=text)

