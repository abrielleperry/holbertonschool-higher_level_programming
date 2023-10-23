-- lists all records of the table without name value, score and name in order, score desc
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;