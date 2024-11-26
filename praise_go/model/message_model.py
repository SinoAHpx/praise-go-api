from abc import abstractmethod


class Message:
    @abstractmethod
    def serialize(self) -> dict:
        pass

class ImageMessage(Message):
    def __init__(self, image_url: str, role: str = "user") -> None:
        self.role = role
        self.image_url = image_url
        
    def serialize(self) -> dict:
        return {
            "role": self.role,
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": self.image_url
                    }
                }
            ]
        }
        
class TextMessage(Message):
    def __init__(self, text: str, role: str = "user") -> None:
        self.text = text
        self.role = role
        
    def serialize(self) -> dict:
        return {
            "role": self.role,
            "content": self.text
        }