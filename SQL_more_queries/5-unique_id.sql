-- create table with unique id
CREATE TABLE unique_id(
  id INT DEFAULT 1,
  UNIQUE (id),
  name VARCHAR(256)
);