#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    ))
    session = Session(bind=engine)
    result = session.query(State).order_by(State.id)
    for col in result:
        print('{0}: {1}'.format(col.id, col.name))
