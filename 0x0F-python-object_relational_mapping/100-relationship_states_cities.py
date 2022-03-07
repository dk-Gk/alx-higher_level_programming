#!/usr/bin/python3
"""creates the State “California” with the City “San Francisco” from the database"""


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
    st = State(name='California')
    ci = City(name='San Francisco')
    st.cities.append(ci)
    session.add_all([ci, st])
    session.commit()
    session.close()
