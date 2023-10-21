from fastapi.responses import JSONResponse


async def json_error_response(status_code: int, detail: str | dict) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={
            'error': {
                'status_code': status_code,
                'message': detail
            }
        }
    )
