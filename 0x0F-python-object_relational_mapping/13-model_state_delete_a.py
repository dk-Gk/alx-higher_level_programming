#!/usr/bin/python3
"""deletes all State objects with a name containing the letter a"""


if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session1 = Session()
    res = session1.query(State).filter(State.nmae.like('%a%')).order_by(State.id)
    for s in res:
        session1.delete(s)
    session1.commit()
    session1.close()
    engine.dispose()
