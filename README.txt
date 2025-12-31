# Artworks API

FastAPI backend for managing artworks, creators, and storage places with PostgreSQL, SQLAlchemy, and Alembic.

---

## Project Structure

app/ # Core application logic
├── main.py # Entry point (FastAPI app)
├── models.py # SQLAlchemy models
├── schemas.py # Pydantic schemas
├── crud.py # CRUD operations
├── init_db.sql # Optional SQL script for DB initialization
alembic/ # Alembic migrations
scripts/ # Utility scripts
├── seed_data.py # Script to populate DB with sample data
alembic.ini # Alembic configuration

---

API Endpoints

Creators
POST /creators/ — Create a new creator
GET /creators/ — List all creators

Storage Places
POST /storage_places/ — Create a new storage place
GET /storage_places/ — List all storage places

Artworks
POST /artworks/ — Create a new artwork
GET /artworks/ — List all artworks
GET /artworks/filter/ — Filter artworks by type and year
GET /artworks/join/ — Get artworks with creator and storage info
PUT /artworks/increase_price/ — Increase price of artworks older than a certain year
GET /artworks/group_by_type/ — Count artworks grouped by type
GET /artworks/sorted/ — Get artworks sorted by price
