-- settings.sql
CREATE DATABASE sports;
CREATE USER sportsuser WITH PASSWORD 'sports';
GRANT ALL PRIVILEGES ON DATABASE sports TO sportsuser;