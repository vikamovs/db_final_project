from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# Creator table
class Creator(Base):
    __tablename__ = "creators"

    id = Column(Integer, primary_key=True, index=True)
    country = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    years_of_life = Column(String)
    main_direction = Column(String)

    # One creator can have many artworks
    artworks = relationship("Artwork", back_populates="creator")

# Storage place table
class StoragePlace(Base):
    __tablename__ = "storage_places"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    country = Column(String)
    opening_date = Column(Date)
    artworks = relationship("Artwork", back_populates="storage_place")

# Artwork table
class Artwork(Base):
    __tablename__ = "artworks"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Float)
    type = Column(String)
    name = Column(String)
    material = Column(String)
    dimensions = Column(String)

    creator_id = Column(Integer, ForeignKey("creators.id"))
    storage_place_id = Column(Integer, ForeignKey("storage_places.id"))

    creator = relationship("Creator", back_populates="artworks")
    storage_place = relationship("StoragePlace", back_populates="artworks")
