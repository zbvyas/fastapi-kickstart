/**
  Run the following in MySQL (until migrations are setup)
**/

CREATE TABLE pets (
  id INTEGER NOT NULL AUTO_INCREMENT,
  name VARCHAR(255),
  color VARCHAR(255),
  breed VARCHAR(255),
  PRIMARY KEY (id)
)