from {{cookiecutter.project_slug}}.db.database import SessionLocal


def get_db():
    """
    get a db session and make sure to always close it.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
