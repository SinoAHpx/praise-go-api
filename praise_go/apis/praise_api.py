import os
from pydantic import BaseModel

from praise_go.model.message_model import ImageMessage
from praise_go.services.chat_service import request_chat
from praise_go.utils.image_manipulation import from_image2compressed_base64
from praise_go.utils.prompts_utils import load_prompt

class PraiseInfo(BaseModel):
    image_path: str
    role: str

def praise(info: PraiseInfo):
    prompt = load_prompt(info.role)
    params = {
        "base_url": os.getenv('base'),
        "model": "Pro/Qwen/Qwen2-VL-7B-Instruct",
        "api_key": os.getenv('apikey'),
        "system_prompt": prompt,
        "prompts": [ImageMessage(from_image2compressed_base64(info.image_path))]
    }
    
    resp = request_chat(**params)
    
    return resp