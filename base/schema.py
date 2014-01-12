from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy import func
from unidecode import unidecode


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    """
    name: the fullname of the user
    handle: the hanle of the user (ie. @liwen)
    email: the email address of the user
    """

    id = Column(Integer, primary_key=True)
    name = Column(String(45), unique=True)
    handle = Column(String(45), unique=True)
    email = Column(String(45))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __repr__(self):
        return "<User('{0}')>".format(unidecode(self.name))
