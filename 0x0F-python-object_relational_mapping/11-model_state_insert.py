#!/usr/bin/python3
"""adds the State object “Louisiana” to the database hbtn_0e_6_usa"""


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
    res = State(name='Loisiana')
    session1.add(res)
    session1.commit()
    print(res.id)
    session1.close()
    session.close()
