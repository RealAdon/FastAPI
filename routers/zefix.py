from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas, models, database, oauth2
from repository import zefix

# Set up router
router = APIRouter(
    prefix='/zefix',
    tags=['zefix']
)

# Post request to get data from Zefix
@router.post('/', status_code=200)
def get_zefix(request: schemas.ZefixRequest, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    # Search Zefix
    return zefix.search(request, db)

# Get the last searches
@router.get('/', status_code=200)
def last_searches(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return zefix.searches(db)