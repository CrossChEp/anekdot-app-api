from typing import Optional

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


class UserUpdateModel(BaseModel):
    username: Optional[str]
    password: Optional[str]

    class Config:
        orm_mode = True


class UserRequestModel(UserUpdateModel):
    id: Optional[int]

    class Config:
        orm_mode = True
