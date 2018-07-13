from models import *

Session = sessionmaker(bind=engine)
session = Session()

def query_experimentation(session):
    pass

def all_r_and_b_songs():
    return session.query(Genre).filter_by(name='R&B').first().songs

def prince_rock_songs():
    prince_songs = session.query(Artist).filter_by(name='Prince').first().songs
    return [song for song in prince_songs if song.genre.name == 'Classic Rock']



    # import pdb; pdb.set_trace()
