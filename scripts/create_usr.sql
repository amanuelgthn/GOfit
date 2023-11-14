-- create mysql user for fitapp
CREATE USER IF NOT EXISTS 'fit_usr'@'localhost' IDENTIFIED BY 'fit_usr_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'fit_usr'@'localhost';
FLUSH PRIVILEGES;