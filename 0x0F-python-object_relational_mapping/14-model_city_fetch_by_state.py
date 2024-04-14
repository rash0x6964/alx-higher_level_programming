#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""

import sys
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    ))

    session = Session(bind=engine)

    res = session.query(State.name, City.id, City.name).join(
        City, State.id == City.state_id
    ).all()
    
    for col in res:
        print("{}: ({}) {}".format(col[0], col[1], col[2]))
