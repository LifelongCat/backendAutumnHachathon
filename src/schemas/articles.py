from pydantic import BaseModel, Field

ARTICLE_ID_TYPE = str


class ArticleSchema(BaseModel):
    id: ARTICLE_ID_TYPE
    creation_date: str
    title: str = Field(min_length=1, max_length=76)
    subtitle: str = Field(min_length=0, max_length=76)
    content: str = Field(min_length=1, max_length=50_000)

    class Config:
        from_attributes = True


class ArticleSchemaCreate(BaseModel):
    title: str = Field(min_length=1, max_length=76)
    subtitle: str = Field(min_length=0, max_length=76)
    content: str = Field(min_length=1, max_length=50_000)
