import uuid
from datetime import datetime

from app.models.post import PostBase


class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    title: str | None = None
    content: str | None = None

class PostRead(PostBase):
    id: uuid.UUID
    creator_id: uuid.UUID
    created_at: datetime
    updated_at: datetime
