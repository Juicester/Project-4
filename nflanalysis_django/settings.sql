-- settings.sql
CREATE DATABASE nflanalysis;
CREATE USER nflanalysisuser
WITH PASSWORD 'nflanalysis';
GRANT ALL PRIVILEGES ON DATABASE nflanalysis TO nflanalysisuser;