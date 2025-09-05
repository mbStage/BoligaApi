--SQLite
INSERT INTO estates
SELECT 
a.id	
, a.priceChangePercentTotal	
, a.energyClass	
, a.price	
, a.buildYear	
, a.street
, a.zipCode
, a.agentDisplayName
, a.isActive
, a.propertyType
, a.squaremeterPrice
, a.daysForSale
, a.images
, CURRENT_DATE AS date
, 1 AS count
, 'New' AS comment
, a.latitude
, a.longitude
FROM estates_new a
LEFT JOIN estates b ON a.id = b.id
WHERE b.id IS NULL;


INSERT INTO estates
SELECT
a.id	
, a.priceChangePercentTotal	
, a.energyClass	
, a.price	
, a.buildYear	
, a.street
, a.zipCode
, a.agentDisplayName
, a.isActive
, a.propertyType
, a.squaremeterPrice
, a.daysForSale
, a.images
, CURRENT_DATE AS date
, -1 AS count
, 'Not for sale' AS comment
, a.latitude
, a.longitude
FROM estates a
LEFT JOIN estates_new b ON a.id = b.id
LEFT JOIN max_date c ON a.id = c.id AND c.maxDate = a.date AND c.maxComment != 'Not for sale'
WHERE b.id IS NULL AND c.id IS NOT NULL;

INSERT INTO estates
SELECT 
a.id	
, a.priceChangePercentTotal	
, a.energyClass	
, a.price	
, a.buildYear	
, a.street
, a.zipCode
, a.agentDisplayName
, a.isActive
, a.propertyType
, a.squaremeterPrice
, a.daysForSale
, a.images
, CURRENT_DATE AS date
, 0 AS count
, 'Price changed' AS comment
, a.latitude
, a.longitude
FROM estates_new a
JOIN ( 

    SELECT 
    a.id 
    , a.price
    , a.date
    FROM estates a
    JOIN max_date c ON a.id = c.id 
    AND c.maxDate = a.date
    WHERE CAST(a.price AS INTEGER) > 0

 ) b 
ON a.id = b.id
WHERE a.price != b.price;

INSERT INTO estates
SELECT 
b.id	
, b.priceChangePercentTotal	
, b.energyClass	
, '-' || b.price	
, b.buildYear	
, b.street
, b.zipCode
, b.agentDisplayName
, b.isActive
, b.propertyType
, b.squaremeterPrice
, a.daysForSale
, a.images
, CURRENT_DATE AS date
, 0 AS count
, 'Price changed' AS comment
, a.latitude
, a.longitude
FROM estates_new a
JOIN ( 

    SELECT 
    *
    FROM estates a
    JOIN max_date c ON a.id = c.id 
    AND c.maxDate = a.date
    WHERE CAST(a.price AS INTEGER) > 0

 ) b 
ON a.id = b.id
WHERE a.price != b.price;
