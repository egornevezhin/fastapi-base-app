import uvicorn

import os
os.environ['DB_SERVER'] = 'localhost'
from '{{ cookiecutter.project_slug}}'.main import app


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
