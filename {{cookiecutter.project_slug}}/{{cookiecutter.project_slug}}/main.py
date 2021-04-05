import sys

import uvicorn
from fastapi import FastAPI

from {{cookiecutter.project_slug}} import settings
from {{cookiecutter.project_slug}}.api import api_router
# without this we can't run the project from a docker container
# we have to add the parent folder to sys.path
from os.path import abspath, dirname
parent_path = dirname(dirname(abspath(__file__)))
sys.path.append(parent_path)

def get_application():
    application = FastAPI(
        title=settings.PROJECT_NAME,
        debug=settings.DEBUG,
        version=settings.VERSION,
    )
    application.include_router(api_router, prefix=settings.PREFIX)
    return application


app = get_application()
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
