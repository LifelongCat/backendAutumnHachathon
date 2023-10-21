from fastapi import status
from fastapi.responses import JSONResponse


async def json_success_response(details: dict):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'data': details
        }
    )
