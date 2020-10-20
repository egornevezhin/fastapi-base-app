from fastapi import Depends, FastAPI
import os, sys
from datetime import timedelta, datetime

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from . import crud, database, models, schemas
from .database import db_state_default


database.db.connect()
database.db.create_tables([])
database.db.close()

app = FastAPI()

sleep_time = 10


async def reset_db_state():
    database.db._state._state.set(db_state_default.copy())
    database.db._state.reset()


def get_db(db_state=Depends(reset_db_state)):
    try:
        database.db.connect()
        yield
    finally:
        if not database.db.is_closed():
            database.db.close()
