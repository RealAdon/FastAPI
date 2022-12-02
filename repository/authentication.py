

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError, jwt

import database, schemas, oauth2
from repository import users
from hashing import Hash

# Define OAuth Scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Function to authenticate the user by password
def authenticate_user(username: str, password: str, db: Session):
    user = users.get_user(db, username)
    if not user:
        return False
    if not Hash.verify(password, user.hashed_password):
        return False
    return user


async def get_current_active_user(current_user: schemas.User = Depends(oauth2.get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user