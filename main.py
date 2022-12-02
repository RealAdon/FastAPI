from fastapi import FastAPI
from utils import zefix
import models
from database import engine
from routers import authentication, users, zefix
# Create app
app = FastAPI(
    title='ER personal API',
    description = 'API to interact with my coded interfaces',
    version= '0.1'
)

# Load database model
models.Base.metadata.create_all(engine)

# Include Routers
app.include_router(authentication.router)
app.include_router(users.router)
app.include_router(zefix.router)