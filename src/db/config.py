from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.models import Base
from get_env import get_env

DB_URL = f'postgresql://{get_env("BD_USERNAME")}:{get_env("BD_PASSWORD")}@{get_env("BD_HOST")}/{get_env("BD_NAME")}'

engine = create_engine(DB_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
