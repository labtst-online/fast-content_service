import datetime
import uuid

from sqlalchemy import TEXT, DateTime, func
from sqlmodel import Column, Field, SQLModel


class PostBase(SQLModel):
    title: str = Field(index=True, max_length=100)
    content: str | None = Field(default=None, sa_column=Column(TEXT))


class Post(PostBase, table=True):
    id: uuid.UUID | None = Field(default_factory=uuid.uuid4, primary_key=True)
    creator_id: uuid.UUID = Field(index=True, nullable=False)
    created_at: datetime.datetime | None = Field(
        sa_column=Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    )
    updated_at: datetime.datetime | None = Field(
        sa_column=Column(
            DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now()
        )
    )
