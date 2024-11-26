from typing import Any

import requests

def request_chat(baseUrl: str, model: str, apiKey: str, system_prompt: str, propmt: Any):
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": propmt
            }
        ]
    }
    headers = {
        "Authorization": f"Bearer {apiKey}"
    }
    response = requests.post(baseUrl, json=payload, headers=headers)
    
    if response.status_code != 200:
        raise SystemError(f'Response error: {response.text}')
    
    json = response.json()
    return json["choices"][0]["message"]["content"]