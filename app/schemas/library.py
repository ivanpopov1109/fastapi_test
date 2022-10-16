from pydantic import BaseModel

class BookBase(BaseModel):
    id:int
    author: str
    book_name: str
    pages:str
    owner_id: int




class UserBase(BaseModel):
    id: int
    name: str
    password: str
    mail: str



if __name__ == "__main__":
    pass

