import requests
from praise_go.model.message_model import Message

def request_chat(base_url: str, model: str, api_key: str, system_prompt: str, prompts: list[Message]) -> str:
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            }
        ]
    }
    
    payload["messages"].extend(prompt.serialize() for prompt in prompts)

    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.post(base_url, json=payload, headers=headers)
    
    if response.status_code != 200:
        raise SystemError(f'Response error: {response.text}')
    
    json = response.json()
 
    return json["choices"][0]["message"]["content"]