from pydantic import BaseModel

from praise_go.model.message_model import ImageMessage
from praise_go.services.chat_service import request_chat
from praise_go.utils.image_manipulation import from_image_to_compressed_base64
from praise_go.utils.prompts_utils import load_prompt

class PraiseInfo(BaseModel):
    image_path: str
    role: str

def praise(info: PraiseInfo, api_key: str, url: str, model: str):
    prompt = load_prompt(info.role)
    params = {
        "base_url": url,
        "model": model,
        "api_key": api_key,
        "system_prompt": prompt,
        "prompts": [ImageMessage(from_image_to_compressed_base64(info.image_path))]
    }
    
    resp = request_chat(**params)
    
    return resp