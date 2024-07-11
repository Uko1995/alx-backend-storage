-- create table 'users' with the following attributes:
-- id (INT NOT NULL PRIMARY KEY)
-- email - string(255 characters)
-- name - string(255 characters)
-- country - enumeration of (US, CO, TN) with US as default

DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
  id INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255),
  country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
); 
