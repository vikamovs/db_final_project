-- Create user
CREATE USER art_user WITH PASSWORD 'art_password';

-- Create database
CREATE DATABASE art_db
    WITH
    OWNER = art_user
    ENCODING = 'UTF8';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE art_db TO art_user;
