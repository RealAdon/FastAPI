from sqlalchemy.orm import Session
import schemas, models
from hashing import Hash

def create(request: schemas.CreateUser, db: Session):
    new_user = models.User(username=request.username,email=request.email,first_name=request.first_name,last_name=request.last_name,hashed_password=Hash.bcrypt(request.password),disabled = False)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db, username: str):
    user = db.query(models.User).filter(models.User.username==username).first()
    return user