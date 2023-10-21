from models.articles import Article
from utils.repository import SQLAlchemyRepository


class ArticlesRepository(SQLAlchemyRepository):
    model = Article
