-- lists the number of records for this score with the label number with the same score in the table second_table
SELECT score score, COUNT(*) number FROM second_table
GROUP BY score
ORDER BY score DESC;