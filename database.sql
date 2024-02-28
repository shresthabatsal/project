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

create TABLE Books (
    BookID INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    Genre VARCHAR(100),
    Author VARCHAR(100),
);

CREATE TABLE BorrowedBooks (
    BorrowID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT,
    BookID INT,
    BorrowDate DATE,
    DueDate DATE
);

INSERT into users(first_name,second_name,email,Role,password,confirm_password)
VALUES("Admin","Adminitrator","admin@gmail.com","Admin","admin123","admin123");

show tables;
select *from users;
select *from books;
select *from BorrowedBooks;
