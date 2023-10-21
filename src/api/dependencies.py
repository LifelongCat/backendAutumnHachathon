from services.articles import ArticlesService
from repositories.articles import ArticlesRepository


def articles_service_with_repo():
    return ArticlesService(ArticlesRepository)
