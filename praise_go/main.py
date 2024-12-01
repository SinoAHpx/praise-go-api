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
def go(
    model: str = "Pro/Qwen/Qwen2-VL-7B-Instruct",
    url: str = "https://api.siliconflow.cn/v1/chat/completions",
    info: PraiseInfo = Body(),
    key: str = Header(alias="Authorization")
) -> dict:
    msg = praise(info, key, url, model)
    return {
        "role": info.role,
        "message": msg
    }