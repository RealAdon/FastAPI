from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
import schemas, database
from repository import users

router = APIRouter(
    prefix='/user',
    tags=['users']
    )

# Create User
@router.post('/', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User,db: Session = Depends(database.get_db)):
    return users.create(request,db)