from pydantic import BaseModel, Field
from typing import Optional

class BookCreate(BaseModel):

    author: str = Field(..., min_length=1, max_length=100)
    book_name: str= Field(..., min_length=1, max_length=100)
    pages:int
    owner_id: int



class UserCreate(BaseModel):

    name: str  = Field(..., min_length=1, max_length=100)
    password: str  = Field(..., min_length=1, max_length=100)
    mail: str  = Field(..., min_length=1, max_length=100)



if __name__ == "__main__":
    pass

