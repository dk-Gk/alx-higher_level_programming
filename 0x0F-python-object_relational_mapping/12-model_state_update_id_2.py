#!/usr/bin/python3
"""changes the name of a State object from the database hbtn_0e_6_usa"""


if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine
    
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session1 = Session()
    res = session1.query(State).filter(State.id == 2).first()
    res.name = 'New Mexico'
    session1.commit()
    session1.close()
    engine.dispose()
