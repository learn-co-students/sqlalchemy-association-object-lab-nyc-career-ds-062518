from models import *
from sqlalchemy import create_engine
engine = create_engine('sqlite:///music.db')
Session = sessionmaker(bind=engine)
session = Session()

def query_experimentation(session):
    pass 
