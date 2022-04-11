from pydantic import BaseModel


class UserModel(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class UserGetModel(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
