from fastapi import Response

def ok_204_no_content(text:str) -> Response:
    return Response(content=text, status_code=204)
