from typing import Annotated
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends, HTTPException, status

from services.articles import ArticlesService
from schemas.articles import ArticleSchemaCreate, ARTICLE_ID_TYPE
from views.successes import json_success_response
from api.dependencies import articles_service_with_repo

router = APIRouter(
    prefix='/article',
    tags=['Articles']
)


@router.get('/{article_id}')
async def get_article(
        article_id: ARTICLE_ID_TYPE,
        articles_service: Annotated[ArticlesService, Depends(articles_service_with_repo)]
) -> JSONResponse:
    db_article = await articles_service.get_article(article_id)
    if db_article is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Article by this id is not found')
    return await json_success_response(db_article)


@router.post("/create")
async def create_article(
        article: ArticleSchemaCreate,
        articles_service: Annotated[ArticlesService, Depends(articles_service_with_repo)]
) -> JSONResponse:
    article_id = await articles_service.create_article(article)
    return await json_success_response({'article_id': article_id})
