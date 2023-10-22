from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base
from schemas.articles import ArticleSchema


class Article(Base):
    __tablename__ = "articles"

    id: Mapped[str] = mapped_column(primary_key=True)
    creation_date: Mapped[str] = mapped_column()
    title: Mapped[str] = mapped_column(String(76))
    subtitle: Mapped[str] = mapped_column(String(76), nullable=True)
    content: Mapped[str] = mapped_column(String(50_000))
    theme: Mapped[str] = mapped_column(String(10))

    def to_read_model(self) -> ArticleSchema:
        return ArticleSchema(
            id=self.id,
            creation_date=self.creation_date,
            title=self.title,
            subtitle=self.subtitle,
            content=self.content,
            theme=self.theme
        )
