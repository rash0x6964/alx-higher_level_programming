#!/usr/bin/python3
"""script that prints the first State object from the database hbtn_0e_6_usa"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    ))
    session = Session(bind=engine)
    res = session.query(State).order_by(State.id).first()
    if res:
        print('{0}: {1}'.format(res.id, res.name))
    else:
        print('Nothing')
