from pydantic import BaseModel, ConfigDict
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

class ArtworkSimple(BaseModel):
    id: int
    name: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

class CreatorResponse(CreatorBase):
    id: int
    artworks: List[ArtworkSimple] = []

    model_config = ConfigDict(from_attributes=True)

# StoragePlace schemas 
class StoragePlaceBase(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    country: Optional[str] = None
    opening_date: Optional[date] = None

class StoragePlaceCreate(StoragePlaceBase):
    pass

class StoragePlaceResponse(StoragePlaceBase):
    id: int
    artworks: List[ArtworkSimple] = []

    model_config = ConfigDict(from_attributes=True)

# Artwork schemas
class ArtworkBase(BaseModel):
    price: Optional[float] = None
    type: Optional[str] = None
    name: Optional[str] = None
    material: Optional[str] = None
    dimensions: Optional[str] = None
    created_year: Optional[int] = None

class ArtworkCreate(ArtworkBase):
    creator_id: int
    storage_place_id: int

class ArtworkResponse(ArtworkBase):
    id: int
    creator: Optional[CreatorBase] = None
    storage_place: Optional[StoragePlaceBase] = None

    model_config = ConfigDict(from_attributes=True)
