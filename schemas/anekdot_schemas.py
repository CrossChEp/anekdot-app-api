from pydantic import BaseModel


class AnekdotAdd(BaseModel):
    content: str

    class Config:
        orm_mode = True
