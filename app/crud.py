from sqlalchemy.orm import Session
from . import models, schemas

# Creators
def get_creators(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Creator).offset(skip).limit(limit).all()

def get_creator(db: Session, creator_id: int):
    return db.query(models.Creator).filter(models.Creator.id == creator_id).first()

def create_creator(db: Session, creator: schemas.CreatorCreate):
    db_creator = models.Creator(**creator.dict())
    db.add(db_creator)
    db.commit()
    db.refresh(db_creator)
    return db_creator

# Storage Places
def get_storage_places(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.StoragePlace).offset(skip).limit(limit).all()

def get_storage_place(db: Session, storage_place_id: int):
    return db.query(models.StoragePlace).filter(models.StoragePlace.id == storage_place_id).first()

def create_storage_place(db: Session, storage_place: schemas.StoragePlaceCreate):
    db_storage = models.StoragePlace(**storage_place.dict())
    db.add(db_storage)
    db.commit()
    db.refresh(db_storage)
    return db_storage

# Artworks
def get_artworks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Artwork).offset(skip).limit(limit).all()

def get_artwork(db: Session, artwork_id: int):
    return db.query(models.Artwork).filter(models.Artwork.id == artwork_id).first()

def create_artwork(db: Session, artwork: schemas.ArtworkCreate):
    db_artwork = models.Artwork(**artwork.dict())
    db.add(db_artwork)
    db.commit()
    db.refresh(db_artwork)
    return db_artwork

def get_artworks_by_filters(db: Session, art_type: str | None = None, year_from: int | None = None):
    query = db.query(models.Artwork)
    
    if art_type:
        query = query.filter(models.Artwork.type == art_type)
    if year_from:
        query = query.filter(models.Artwork.created_year >= year_from)
    
    return query.all()

def get_artworks_with_creator_and_storage(db: Session):
    return db.query(
        models.Artwork,
        models.Creator.full_name,
        models.StoragePlace.name.label("storage_name")
    ).join(models.Creator).join(models.StoragePlace).all()

def update_artworks_price_older_than(db: Session, year: int, percent_increase: float):
    artworks = db.query(models.Artwork).filter(models.Artwork.created_year < year).all()
    for artwork in artworks:
        artwork.price *= 1 + percent_increase / 100
    db.commit()
    return artworks

from sqlalchemy import func

def get_artworks_count_by_type(db: Session):
    return db.query(models.Artwork.type, func.count(models.Artwork.id)).group_by(models.Artwork.type).all()

def get_artworks_sorted(db: Session, sort_by_price: str = "asc"):
    query = db.query(models.Artwork)
    if sort_by_price == "asc":
        query = query.order_by(models.Artwork.price.asc())
    else:
        query = query.order_by(models.Artwork.price.desc())
    return query.all()
