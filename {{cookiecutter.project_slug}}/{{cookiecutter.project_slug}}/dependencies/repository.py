from fastapi import Depends
from sqlalchemy.orm import Session

from {{cookiecutter.project_slug}}.dependencies.database import get_db


def get_repositories(*repositories):
    """
    Returns a list of repository instances.
    Every repo needs a session, we need to call get_db() for that
    """

    def _get_repositories(session: Session = Depends(get_db)):
        instantiated_repositories = []
        for repo in repositories:
            instantiated_repositories.append(repo(session))
        return instantiated_repositories

    return _get_repositories

