from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI, Request, status, UploadFile
from starlette.exceptions import HTTPException as StarletteHTTPException

from api.routers import all_routers
from views.exceptions import json_error_response


app = FastAPI(
    title='Backend Autemn Hackathon'
)
for router in all_routers:
    app.include_router(router)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException) -> JSONResponse:
    return await json_error_response(exc.status_code, exc.detail)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    return await json_error_response(status.HTTP_422_UNPROCESSABLE_ENTITY,
                                     {exc['loc'][1]: exc['msg'] for exc in exc.errors()})

