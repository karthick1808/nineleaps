CREATE DATABASE hive_metastore;
CREATE USER 'hive_user'@'localhost' IDENTIFIED BY 'hive_password';
GRANT ALL PRIVILEGES ON hive_metastore.* TO 'hive_user'@'localhost';
FLUSH PRIVILEGES;
