--SQLite

CREATE TABLE IF NOT EXISTS max_date (
    id TEXT PRIMARY KEY,
    maxDate DATE,
    maxComment TEXT
);

DELETE FROM max_date;

INSERT INTO max_date (id, maxDate, maxComment)
SELECT 
a.id
, a.maxDate
, b.comment as maxComment
from (
select  
id
, max(date) as maxDate
from estates 
WHERE CAST(price AS INTEGER) > 0
GROUP BY id) a 
JOIN estates b 
ON a.id = b.id 
AND a.maxDate = b.date
WHERE CAST(price AS INTEGER) > 0;
