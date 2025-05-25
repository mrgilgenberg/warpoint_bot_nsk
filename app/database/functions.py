from .connection import sessions_db
from sqlalchemy import text
from app.config import settings
from .models import UserRow, PresenterRow
from app.utils import logger


class BotDB:

    @classmethod
    async def get_user(cls, n_telegram_id: int) -> UserRow:
        sql_query = f'''
        SELECT
               uu_user_id,
               n_telegram_id,
               vc_full_name,
               d_birthday,
               vc_phone,
               b_blocked,
               uu_presenter_id
                FROM {settings.DB_SCHEME}.users
         WHERE 1=1
           AND n_telegram_id = :n_telegram_id
        '''
        params = {
            'n_telegram_id': n_telegram_id
        }
        async with sessions_db() as session:
            result = await session.execute(text(sql_query), params or {})
            user = result.mappings().first()
            logger.debug(user)
            if user:
                user = UserRow(**user)
                logger.debug('NOOOON')
        return user

    @classmethod
    async def get_presenter(cls, n_presenter_id: int) -> PresenterRow:
        sql_query = f'''
        SELECT
            uu_presenter_id,
            n_presenter_id
                FROM {settings.DB_SCHEME}.presenters
         WHERE 1=1
           AND n_presenter_id = :n_presenter_id
        '''
        params = {
            'n_presenter_id': n_presenter_id
        }
        async with sessions_db() as session:
            result = await session.execute(text(sql_query), params or {})
            presenter = result.mappings().first()
            if presenter:
                presenter = PresenterRow(**presenter)
        return presenter

    @classmethod
    async def post_user(cls,
                        n_telegram_id: int,
                        uu_presenter_id) -> UserRow:
        sql_query = f'''
        INSERT INTO {settings.DB_SCHEME}.users(
            n_telegram_id,
            uu_presenter_id
        )
        VALUES (
            :n_telegram_id,
            :uu_presenter_id
        )
        RETURNING uu_user_id;
        '''
        params = {
            'n_telegram_id': n_telegram_id,
            'uu_presenter_id': uu_presenter_id
        }
        async with sessions_db() as session:
            result = await session.execute(text(sql_query), params or {})
            user = result.scalar()
            await session.commit()
        return user

    @classmethod
    async def update_user(cls,
                          n_telegram_id: int,
                          key: str,
                          value):
        sql_query = f'''
        UPDATE {settings.DB_SCHEME}.users
           SET {key} = '{value}'
         WHERE 1=1
           AND n_telegram_id = :n_telegram_id
        '''
        params = {
            'n_telegram_id': n_telegram_id
        }
        async with sessions_db() as session:
            try:
                await session.execute(text(sql_query), params or {})
                await session.commit()
            except Exception as e:
                logger.error(e)
                return False
        return True