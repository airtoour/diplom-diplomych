from db.base_repository import BaseRepository
from db.models import Cars


class CarsRepository(BaseRepository):
    """Репозиторий для определения методов работы с таблицей Cars"""
    model = Cars
