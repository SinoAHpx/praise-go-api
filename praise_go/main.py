import datetime
from fastapi import FastAPI
import platform

api = FastAPI()

@api.get('/')
def root():
    return {
        "arch": platform.machine(),
        "python": platform.python_version(),
        "os": platform.platform(),
        "time": datetime.datetime.now()
    }