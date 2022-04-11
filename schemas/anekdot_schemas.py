from pydantic import BaseModel


class AnekdotModel(BaseModel):
    content: str

    class Config:
        orm_mode = True
