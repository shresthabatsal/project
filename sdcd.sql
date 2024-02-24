create database project;
use project;

create table if not exists users(
USERID int auto_increment Primary key,
first_name varchar(225) NOT NULL,
second_name varchar (225) NOT NULL,
email varchar(225) NOT NULL,
Role varchar(50) NOT NULL,
password varchar(225) NOT NULL,
confirm_password varchar (225) NOT NULL
);
show tables;
select *from users

CREATE TABLE Books (
    BookID INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    Genre VARCHAR(100),
    Author VARCHAR(100),
    Description TEXT
);

show tables;
select *from books;

INSERT into Books(title,Genre,Author)
VALUES("The Great Gatsby","Fiction,Classic Literature","F. Scott Fitzgerald")


ALTER TABLE Books
DROP COLUMN Description;
        
        
        






