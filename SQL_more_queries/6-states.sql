-- creates database and table with unique, not null, autoincrment, primary key
CREATE DATABASE hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE states(
  id INT AUTO_INCREMENT NOT NULL,
  PRIMARY KEY (id),
  name VARCHAR(256) NOT NULL
);