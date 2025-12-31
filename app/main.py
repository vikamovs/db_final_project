from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List
from . import models, schemas, crud
from .database import SessionLocal, engine

app = FastAPI(title="Artworks API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Creators
@app.post("/creators/", response_model=schemas.CreatorResponse)
def create_creator(creator: schemas.CreatorCreate, db: Session = Depends(get_db)):
    return crud.create_creator(db=db, creator=creator)

@app.get("/creators/", response_model=List[schemas.CreatorResponse])
def read_creators(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_creators(db=db, skip=skip, limit=limit)

# Storage Places
@app.post("/storage_places/", response_model=schemas.StoragePlaceResponse)
def create_storage_place(storage_place: schemas.StoragePlaceCreate, db: Session = Depends(get_db)):
    return crud.create_storage_place(db=db, storage_place=storage_place)

@app.get("/storage_places/", response_model=List[schemas.StoragePlaceResponse])
def read_storage_places(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_storage_places(db=db, skip=skip, limit=limit)

# Artworks
@app.post("/artworks/", response_model=schemas.ArtworkResponse)
def create_artwork(artwork: schemas.ArtworkCreate, db: Session = Depends(get_db)):
    return crud.create_artwork(db=db, artwork=artwork)

@app.get("/artworks/", response_model=List[schemas.ArtworkResponse])
def read_artworks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_artworks(db=db, skip=skip, limit=limit)

# Additional endpoints
@app.get("/artworks/filter/", response_model=List[schemas.ArtworkResponse])
def filter_artworks(
    art_type: Optional[str] = Query(None, alias="art_type"),
    year_from: Optional[int] = Query(None, alias="year_from"),
    db: Session = Depends(get_db)
):
    return crud.get_artworks_by_filters(db, art_type, year_from)

@app.get("/artworks/join/")
def artworks_with_creator_and_storage(db: Session = Depends(get_db)):
    results = crud.get_artworks_with_creator_and_storage(db)
    return [
        {
            "artwork_id": art.Artwork.id,
            "artwork_name": art.Artwork.name,
            "creator_name": art.full_name,
            "storage_name": art.storage_name
        }
        for art in results
    ]

@app.put("/artworks/increase_price/")
def increase_price(year: int, percent: float, db: Session = Depends(get_db)):
    updated = crud.update_artworks_price_older_than(db, year, percent)
    return {"updated_count": len(updated)}

@app.get("/artworks/group_by_type/")
def artworks_count_by_type(db: Session = Depends(get_db)):
    results = crud.get_artworks_count_by_type(db)
    return [{"type": type_, "count": count} for type_, count in results]

@app.get("/artworks/sorted/", response_model=List[schemas.ArtworkResponse])
def artworks_sorted(sort: str = "asc", db: Session = Depends(get_db)):
    return crud.get_artworks_sorted(db, sort_by_price=sort)
