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
VALUES("To Kill a Mockingbird", "Fiction,Classic Literature", "Harper Lee");
	
    


ALTER TABLE Books
DROP COLUMN Description;

CREATE TABLE BorrowedBooks (
    BorrowID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT,
    BookID INT,
    BookName Varchar(225),
    BorrowDate DATE,
    DueDate DATE
);
    
select *from borrowedbooks

Delete FROM Books
WHERE BookID = '2';

SET SQL_SAFE_UPDATES = 0;
select *from Books

INSERT Into borrowedbooks(BorrowID,UserID,BookID )
VALUES("2345","33","4");
        
        
        






