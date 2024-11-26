import datetime
from fastapi import FastAPI
import platform

from src.utils.image_manipulation import compressImgToBase64

# api = FastAPI()

# @api.get('/')
# def root():
#     return {
#         "arch": platform.machine(),
#         "python": platform.python_version(),
#         "os": platform.platform(),
#         "time": datetime.datetime.now()
#     }
    
compressImgToBase64("/Users/a1/Misc/Snipshots/Snipaste_2024-11-20_23-03-50.png")