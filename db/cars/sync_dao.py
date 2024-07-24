from sqlalchemy import select, insert, update
from sqlalchemy.exc import SQLAlchemyError

from db.dao.sync_base import SyncBaseRepository
from db.cars.cars import Cars
from db.users.users import Users
from db.db import sync_session_maker

from logger import logger


class SyncCarsRepository(SyncBaseRepository):
    model = Cars

    @classmethod
    def add_car(cls, user_id: int, **data):
        try:
            with sync_session_maker() as session:
                get_id = select(Users).filter_by(user_id=user_id)
                result_get = session.execute(get_id)

                result: int = result_get.scalar_one_or_none()

                if result:
                    query = insert(cls.model).values(**data)
                    session.execute(query)
                    session.commit()
        except SQLAlchemyError as e:
            if isinstance(e, SQLAlchemyError):
                message = 'Database'
            else:
                message = 'Unknown'
            extra = {"user_id": user_id}
            logger.error(message, extra=extra, exc_info=True)

    @classmethod
    def update_car(cls, user_id: int, field_name, new_value):
        try:
            with sync_session_maker() as session:
                query = update(cls.model).where(
                    cls.model.user_id == user_id
                ).values(
                    {field_name: new_value}
                )
                session.execute(query)
                session.commit()
        except SQLAlchemyError as e:
            if isinstance(e, SQLAlchemyError):
                message = 'Database'
            else:
                message = 'Unknown'
            extra = {
                "user_id": user_id,
                "field_name": field_name,
                "new_value": new_value
            }
            logger.error(message, extra=extra, exc_info=True)
