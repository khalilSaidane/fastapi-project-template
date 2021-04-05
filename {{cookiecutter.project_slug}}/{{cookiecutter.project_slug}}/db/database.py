from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from {{cookiecutter.project_slug}} import settings
from {{cookiecutter.project_slug}}.db.utils import get_connect_args_for_sqlite
from sqlalchemy.ext.declarative import declarative_base

url = settings.DATABASE_URL
connect_args = get_connect_args_for_sqlite(url)
engine = create_engine(str(url), **connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# all other apps models will inherit from this class
Base = declarative_base()