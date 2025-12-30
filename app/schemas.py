from pydantic import BaseModel
from typing import List, Optional
from datetime import date

# Creator schemas
class CreatorBase(BaseModel):
    country: str
    full_name: str
    years_of_life: Optional[str] = None
    main_direction: Optional[str] = None

class CreatorCreate(CreatorBase):
    pass

class Creator(CreatorBase):
    id: int
    artworks: List["Artwork"] = []

    class Config:
        orm_mode = True

# StoragePlace schemas
class StoragePlaceBase(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    country: Optional[str] = None
    opening_date: Optional[date] = None

class StoragePlaceCreate(StoragePlaceBase):
    pass

class StoragePlace(StoragePlaceBase):
    id: int
    artworks: List["Artwork"] = []

    class Config:
        orm_mode = True

# Artwork schemas
class ArtworkBase(BaseModel):
    price: Optional[float] = None
    type: Optional[str] = None
    name: Optional[str] = None
    material: Optional[str] = None
    dimensions: Optional[str] = None

class ArtworkCreate(ArtworkBase):
    creator_id: int
    storage_place_id: int

class Artwork(ArtworkBase):
    id: int
    creator: Optional[Creator] = None
    storage_place: Optional[StoragePlace] = None

    class Config:
        orm_mode = True
