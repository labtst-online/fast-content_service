import logging
import uuid
from typing import Annotated

from auth_lib import CurrentUserUUID
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.core.database import get_async_session
from app.models.post import Post
from app.schemas.post import PostCreate, PostRead

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post(
    "/posts",
    response_model=PostRead,
    summary="Create a new post",
    description="Retrieves the post associated with the authenticated user.",
)
async def create_post(
    post_create: PostCreate,
    creator_id: CurrentUserUUID,
    session: AsyncSession = Depends(get_async_session),
):
    """Creates a new post and bind user to post"""
    logger.info(f"Creating new post with creator_id: {creator_id}")
    create_data = post_create.model_dump()
    db_post = Post(**create_data, creator_id=creator_id)
    session.add(db_post)
    post_to_return = db_post

    try:
        await session.commit()
        await session.refresh(post_to_return)
        logger.info(f"Successfully committed post changes for post_id: {post_to_return.id}")
        return post_to_return
    except IntegrityError:
        await session.rollback()
        logger.error(f"Integrity error for post_id: {post_to_return.id}")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Content potentially already exists or data conflict.",
        )
    except Exception as e:
        await session.rollback()
        logger.exception(f"Error saving content for post_id: {post_to_return.id} - {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Could not save content"
        )


@router.get(
    "/posts/{post_id}",
    response_model=PostRead,
    summary="Get a single post",
    description="Retrieves the post associated with the authenticated user.",
)
async def get_one_post(post_id: uuid.UUID, session: AsyncSession = Depends(get_async_session)):
    """Fetches the post"""
    statement = select(Post).where(Post.id == post_id)
    result = await session.execute(statement)
    post = result.scalar_one_or_none()

    if not post:
        logger.info(f"Post not found for post_id: {post_id}")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    logger.info(f"Retrieved post for post_id: {post_id}")
    return post


router.get(
    "/posts",
    response_model=list[PostRead],
    summary="Get recent posts",
    description="Retrieves recently published posts",
)


async def get_resent_posts(
    limit: Annotated[int, Query(ge=1, le=50)] = 50,
    offset: Annotated[int, Query(ge=0)] = 0,
    session: AsyncSession = Depends(get_async_session),
):
    """Fetches the first 50 posts"""
    statement = select(Post).order_by(Post.created_at.desc()).offset(offset).limit(limit)
    result = await session.execute(statement)
    posts = result.scalars().all()

    logger.info(f"Retrieved {len(posts)} recent posts (limit={limit}, offset={offset})")
    return posts


@router.get(
    "/users/{user_id}/posts",
    response_model=list[PostRead],
    summary="Get posts filtered by creator",
    description="Retrieves the posts created by a specific user.",
)
async def get_posts_by_creator(
    user_id: uuid.UUID,
    limit: Annotated[int, Query(ge=1, le=50)] = 20,
    offset: Annotated[int, Query(ge=0)] = 0,
    session: AsyncSession = Depends(get_async_session),
):
    """Fetches the posts filtered by creator_id"""
    statement = (
        select(Post)
        .where(Post.creator_id == user_id)
        .order_by(Post.created_at.desc())
        .offset(offset)
        .limit(limit)
    )
    result = await session.execute(statement)
    posts = result.scalars().all()

    logger.info(f"Retrieved {len(posts)} posts for creator_id: {user_id}")
    return posts
