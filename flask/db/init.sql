CREATE DATABASE test_db;
use test_db;

CREATE TABLE MyUsers (
  firstname VARCHAR(30) NOT NULL,
  lastname VARCHAR(30) NOT NULL
);

INSERT INTO MyUsers
  (firstname, lastname)
VALUES
  ('Anurag', 'Guda'),
  ('Madhavi', 'Mummadireddy');
