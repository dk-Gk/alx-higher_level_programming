#!/usr/bin/python3
"""relation_city"""

from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey
from relationship_state import Base


class City(Base):
    '''Class city model'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
