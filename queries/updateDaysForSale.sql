--SQLite
UPDATE estates
SET daysForSale = (
    SELECT b.daysForSale
    FROM estates_new b
    WHERE estates.id = b.id
)
WHERE EXISTS (
    SELECT 1
    FROM estates_new b
    WHERE estates.id = b.id
    AND estates.comment in ('New','Price changed')
);