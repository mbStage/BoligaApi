-- SQlite
ALTER TABLE estates ADD COLUMN date DATE;
-- Add an integer column named 'count'
ALTER TABLE estates ADD COLUMN count INTEGER;
-- Add a text column named 'comment'
ALTER TABLE estates ADD COLUMN comment TEXT;

