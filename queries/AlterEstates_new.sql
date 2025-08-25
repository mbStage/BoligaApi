--SQLite
/*
ALTER TABLE estates
ADD COLUMN longitude TEXT;
*/


UPDATE estates
SET latitude = (SELECT latitude FROM estates_new WHERE estates.id = estates_new.id),
    longitude = (SELECT longitude FROM estates_new WHERE estates.id = estates_new.id);


