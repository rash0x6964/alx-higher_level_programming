#!/usr/bin/python3
"""script that adds the State object “Louisiana”
    to the database hbtn_0e_6_usa
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

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    print(new_state.id)
    session.close()
