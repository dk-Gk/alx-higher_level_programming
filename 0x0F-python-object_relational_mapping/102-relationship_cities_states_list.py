#!/usr/bin/python3
"""script that lists all City objects from the database hbtn_0e_101_usa"""


if __name__ == "__main__":
    import sys
    from relationship_city import Base, City
    from relationship_state import State
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine
    
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    for st in session.query(State).order_by(State.id).all():
        for ci in st.cities:
            print("{}: {} -> {}".format(ci.id, ci.name, st.name))
    session.close()
