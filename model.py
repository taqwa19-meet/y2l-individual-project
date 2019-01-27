from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class User(Base):
   __tablename__ = 'users'
   id = Column(Integer, primary_key=True)
   username = Column(String)
   password = Column(Integer)

class Post(Base):
    __tablename__ = "Post"
    id_table = Column(Integer, primary_key = True)
    post_string = Column(String)
    username = Column(String)
    def __repr__():
      return("Post post_string: {},Post username: {}".format(self.post_string , self.username))

    # def __repr__(self):
    #     return ("{} \n "
    #         "\n").format(
    #             self.post_string)