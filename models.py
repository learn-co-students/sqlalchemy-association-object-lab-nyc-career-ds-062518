from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Artist(Base):
    __tablename__ = 'artists'
    id = Column( Integer, primary_key = True)
    name = Column(Text)
    genres= relationship('Genre',secondary = 'songs', back_populates = 'artists')
    #songs= relationship( 'Song', back_populates= 'artist')


class Genre(Base):
    __tablename__ = 'genres'
    id=Column( Integer, primary_key = True)
    name = Column(Text)
    artists= relationship('Artist', secondary= 'songs', back_populates= 'genres')
    #songs= relationship('Song', back_populates= 'genre')


class Song(Base):
    __tablename__ = 'songs'
    id= Column(Integer, primary_key= True)
    name = Column(Text)
    artist_id=Column(Integer, ForeignKey('artists.id'))
    genre_id=Column(Integer, ForeignKey('genres.id'))
    artist = relationship('Artist', backref=backref("songs", cascade="all, delete-orphan"))
    genre = relationship( 'Genre', backref=backref("songs", cascade="all, delete-orphan"))



# Write your classes below






engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
