from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import Category, Base, Item, User

engine = create_engine('sqlite:///babystuff.db')

Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session = DBSession()

puppies=session.query(User).order_by(User.name).all()
for puppy in puppies:
     print puppy.name

