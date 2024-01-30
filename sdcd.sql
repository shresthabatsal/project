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




