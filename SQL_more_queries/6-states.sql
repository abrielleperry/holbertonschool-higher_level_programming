-- creates database and table with unique, not null, autoincrment, primary key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
  id INT AUTO_INCREMENT NOT NULL,
  PRIMARY KEY (id),
  name VARCHAR(256) NOT NULL
);