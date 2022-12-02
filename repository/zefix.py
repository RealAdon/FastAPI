from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import schemas, models
from utils import zefix

# Get Data from Zefix
def search(request: schemas.ZefixRequest, db: Session):
    data = zefix.search(request.name,
        languageKey=request.languageKey,
        maxEntries = request.maxEntries,
        offset = request.offset,
        searchType=request.searchType)
    # Create new Database entry
    new_search = models.ZefixSearches(name=request.name,results=data['search']['len'])
    # Add entry to Database
    db.add(new_search)
    # Commit entry to Database
    db.commit()
    # Refresh DB
    db.refresh(new_search)
    # Raise HTTP_Error if no Entry found
    if data['zefix_request']['status_code'] == 404:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
        detail='No entry found for: {}'.format(request.name))
    return data

# Show entries of the Searches
def searches(db: Session):
    return db.query(models.ZefixSearches).all()