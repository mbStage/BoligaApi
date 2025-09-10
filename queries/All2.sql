-- SQLite
/*
select a.* From estates a 
where CAST(a.price AS INTEGER) > 4000000 
AND CAST(a.price AS INTEGER) < 5600000
ORDER BY a.squaremeterPrice;

select * From estates a
where id = '2172879';

*/


SELECT *

FROM estates 
--WHERE id = '2243280';
WHERE date = '2025-09-10';

--SELECT * FROM estates
DELETE FROM estates
WHERE id = '2181338'
AND price = '-6495000'
AND comment = 'Not for sale';


/*

SELECT * from estates
WHERE street = 'Højeloft Vænge 258';

SELECT * from estates
WHERE street like 'Højeloft%';

*/

/*
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

*/

