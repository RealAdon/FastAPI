from pydantic import BaseModel
from typing import Optional, Union

class ZefixRequest(BaseModel):
    name : str
    languageKey: Optional[str] = 'de'
    maxEntries: Optional[int] = 100
    offset: Optional[int] = 0
    searchType: Optional[str] = 'exact'

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None
    # Because we use SQLAlchemy in ORM Mode, we need to define the Config
    class Config():
        orm_mode = True


class CreateUser(BaseModel):
    username: str
    email: Union[str, None] = None
    first_name: Union[str, None] = None
    last_name: Union[str, None] = None
    password: str
    disabled: Union[bool, None] = None
    # Because we use SQLAlchemy in ORM Mode, we need to define the Config
    class Config():
        orm_mode = True

class User(BaseModel):
    username: str
    email: Union[str, None] = None
    first_name: Union[str, None] = None
    last_name: Union[str, None] = None
    disabled: Union[bool, None] = None
    # Because we use SQLAlchemy in ORM Mode, we need to define the Config
    class Config():
        orm_mode = True

class UserInDB(User):
    hashed_password: str
    # Because we use SQLAlchemy in ORM Mode, we need to define the Config
    class Config():
        orm_mode = True

class ShowUser(BaseModel):
    username:str
    disabled: Union[bool, None] = None
    # Because we use SQLAlchemy in ORM Mode, we need to define the Config
    class Config():
        orm_mode = True

class Login(BaseModel):
    username:str
    password:str