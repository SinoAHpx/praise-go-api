import datetime
from fastapi import Body, FastAPI, Header
import platform

from praise_go.apis.praise_api import PraiseInfo, praise

api = FastAPI()

@api.get('/')
def root():
    return {
        "arch": platform.machine(),
        "python": platform.python_version(),
        "os": platform.platform(),
        "time": datetime.datetime.now()
    }

@api.post('/praise')
def go(info: PraiseInfo = Body(), key: str = Header(alias="Authorization")):
    msg = praise(info, key)
    return {
        "role": info.role,
        "message": msg
    }