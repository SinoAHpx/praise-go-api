import requests
from praise_go.model.message_model import ImageMessage, Message, TextMessage

def request_chat(baseUrl: str, model: str, apiKey: str, system_prompt: str, *prompts: list[Message]):
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
        "Authorization": f"Bearer {apiKey}"
    }
    response = requests.post(baseUrl, json=payload, headers=headers)
    
    if response.status_code != 200:
        raise SystemError(f'Response error: {response.text}')
    
    json = response.json()
    return json["choices"][0]["message"]["content"]