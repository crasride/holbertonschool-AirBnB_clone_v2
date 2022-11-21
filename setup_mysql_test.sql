-- script that prepares a MySQL server for the project AirBnb clone
-- create new database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create new user and grant privileges
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- SELECT privileges
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
