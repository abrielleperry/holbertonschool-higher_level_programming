-- creates table called second_table in current database hbtn_0c_0 with rows and columns
CREATE TABLE second_table(
  id INT,
  name VARCHAR(256),
  score INT
);
INSERT INTO second_table (id, name, score) VALUES (1, "John", 10);
INSERT INTO second_table (id, name, score) VALUES (2, "Alex", 3);
INSERT INTO second_table (id, name, score) VALUES (3, "Bob", 14);
INSERT INTO second_table (id, name, score) VALUES (4, "George", 8);
