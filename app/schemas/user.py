from pydantic import BaseModel, Field, validator
from typing import Optional

class UserBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    mail: str = Field(..., min_length=1, max_length=100)


class UserCreate(UserBase):
    password: str = Field(..., min_length=1, max_length=100)


class UserDB(UserBase):
    id: int
    mail: Optional[str]

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    @validator('password')
    def pass_cannot_be_null(cls, value):
        if value is None:
            raise ValueError('Пароль не может быть пустым!')
        return value

    password: Optional[str] = Field(None, min_length=1, max_length=100)
    name: Optional[str] = Field(None,  min_length=1, max_length=100)
    mail: Optional[str] = Field(None, min_length=1, max_length=100)

if __name__ == "__main__":
    pass
