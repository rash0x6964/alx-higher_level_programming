#!/usr/bin/python3
"""script that deletes all State objects with a name
    containing the letter a from the database hbtn_0e_6_usa
"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    ))

    session = Session(bind=engine)
    
    res = session.query(State).filter(State.name.contains('a'))
    for col in res:
        session.delete(col)

    session.commit()
    session.close()
