from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def sign_up(username, password):
	user_object = User(name=username,
		password=password)
	    session.add(user_object)
	    session.commit()
    pass
