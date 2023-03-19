from api import create_app
import uvicorn
from os import environ

app = create_app()

DEBUG = environ.get('DEBUG', False)

if __name__ == "__main__":
    uvicorn.run("__main__:app",port = 5000, reload = True)