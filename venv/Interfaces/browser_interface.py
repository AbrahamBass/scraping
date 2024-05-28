from pydantic import BaseModel

class Alone(BaseModel):
    text: str
    id: str
    className: str