import re
from typing import Type
from time import gmtime, strftime
from transliterate import translit

from utils.repository import AbstractRepository
from schemas.articles import ArticleSchemaCreate, ARTICLE_ID_TYPE


class ArticlesService:
    def __init__(self, articles_repo: Type[AbstractRepository]):
        self.articles_repo: AbstractRepository = articles_repo()

    async def create_id(self, article_dict: dict) -> ARTICLE_ID_TYPE:
        article_id = translit(article_dict['title'], 'ru', reversed=True)
        # удаление остаточных кавычек от перевода букв Ь и Ъ
        article_id = re.sub(r"'", '', article_id)
        # разделение по знакам препинания
        delimiters = r'[ \n\t?!(),.-]+'
        delimited_ai = re.split(delimiters, article_id)
        # создание единообразия конца списка
        delimited_ai.append("") if delimited_ai[-1] != "" else ""

        full_ai = "-".join(delimited_ai) + article_dict["creation_date"]
        count_sim_ais = await self.articles_repo.check_count(full_ai)
        if count_sim_ais == 0:
            return full_ai
        else:
            return f'{full_ai}-{count_sim_ais + 1}'

    async def get_article(self, article_id: ARTICLE_ID_TYPE) -> dict | None:
        db_article = await self.articles_repo.get_one(article_id)
        if db_article is None:
            return None
        return db_article.to_read_model().model_dump()

    async def create_article(self, article: ArticleSchemaCreate) -> int:
        article_dict = article.model_dump()
        article_dict['creation_date'] = strftime("%m-%d", gmtime())
        article_dict['id'] = await self.create_id(article_dict)
        article_id = await self.articles_repo.create_one(article_dict)
        return article_id


