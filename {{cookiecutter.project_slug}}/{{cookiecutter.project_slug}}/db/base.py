# Import all the models, so that Base has them before being
# imported by Alembic
from {{cookiecutter.project_slug}}.db.database import Base
# from users.models import User # example