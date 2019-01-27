from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def sign_ups(username, password):
    user_object = User(username=username,
        password=password)
    session.add(user_object)
    session.commit()

def query_all_users():
    users = session.query(
        User).all()
    return users

def query_user_by_name(username):
    name = session.query(
        User).filter_by(username=username).first()
    return name

def add_Post(post_string):
    post_object = Post(post_string=post_string)
    session.add(post_object)
    session.commit()

def query_all_posts():
    posts = session.query(
        Post).all()
    return posts

def query_post_by_id(post_id):
    post = session.query(Post).filter_by(id_table=post_id).first()
    return post

def add_Post(post_string,username):
    post_object = Post(post_string=post_string, username=username)
    session.add(post_object)
    session.commit()

def query_all_posts():
    posts = session.query(
        Post).all()
    return posts

def query_post_by_id(post_id):
    post = session.query(Post).filter_by(id_table=post_id).first()
    return post


    pass
