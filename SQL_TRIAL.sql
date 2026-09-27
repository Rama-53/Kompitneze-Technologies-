-- data definition
CREATE DATABASE company_db;
USE company_db;
CREATE TABLE employees(
employee_id INT PRIMARY KEY,
emp_name VARCHAR(50),
department VARCHAR(50),
salary INT,
city VARCHAR(50),
age INT
);

INSERT INTO employees VALUES
(1,"Abhay","IT",50000,"Kochi",25),
(2,"Arun","Sales",30000,"Banglore",22),
(3,"Ajay","IT",55000,"Delhi",30),
(4,"Rahul","Marketing",40000, "Trivandrum",28);

SELECT * FROM employees;

CREATE TABLE students (
	student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    course VARCHAR(50)
    );
    
INSERT INTO students VALUES 
(100,'Deepu','pyhton fullstack'),
(101,'Abhay','pyhton fullstack'),
(102,'Jithu','pyhton fullstack'),
(104,'Ram','pyhton fullstack'),
(105,'Muhammmed','pyhton fullstack'),
(106,'Irfan','pyhton fullstack'),
(107,'Alena','pyhton fullstack'),
(108,'Aiswarya','pyhton fullstack'),
(109,'Jobin','pyhton fullstack');

SELECT * FROM students;
SELECT emp_name from employees;
SELECT emp_name, salary FROM employees WHERE SALARY>=20000;
select emp_name,salary from employees where salary>=20000 and department="HR";
select emp_name,salary from employees where salary>=20000 OR department="it";

-- RANGE
SELECT emp_name ,age from employees where age between 20 and 25;

-- not
select emp_name,salary from employees where not age= 22;

--	using NOT
SELECT emp_name, age FROM employees WHERE NOT age =23;
SELECT emp_name, age FROM employees WHERE age != 23;

-- in,not IN
SELECT * from employees WHERE Lepartment NOT IN ( "HR" , "IT" );
SELECT * FROM employees WHERE department IN ( "HR", "IT" );

SELECT salary, salary + 5000 AS new_salary FROM employees;
SELECT salary, salary - 5000 AS new_salary FROM employees;
SELECT salary, salary/5 AS new_salary FROM employees;
SELECT salary, salary*10 AS new_salary FROM employees;
SELECT salary, salary%10 AS new_salary FROM employees;


INSERT INTO employees values
(4,'Deepu','HR',25000,'TVM',26);

SELECT distinct department from employees;
SELECT department FROM employees;



SELECT length(emp_name) from employees;
INSERT INTO employees values
(5,' akshay ',' EC ',28000,'idukki',31),
(7,' Ramnath ' ,'Mech',45000,'muvattupuzha',40)
;

--- OFFSET,LIMIT

select * from employees limit 3;


---	TRIM
select TRIM(emp_name) from employees;
select * from employees;

-- Delecte,truncate,drop
delete from employees where employee_id=1;
truncate table employees;
drop table employees; 


ALTER TABLE studentss ADD joining_date DATE;
ALTER TABLE studentss ADD phone_number BIGINT, ADD address VARCHAR(100);
ALTER TABLE studentss MODIFY phone_number VARCHAR(100);
--- rename column
ALTER TABLE studentss RENAME COLUMN student_name TO full_name;

--- delete a column
ALTER TABLE studentss drop COLUMN address;

SELECT * FROM studentss;


use company_db;


UPDATE studentss SET phone_number = 9586423512 ;
UPDATE studentss SET phone_number = 0012030415 WHERE student_id = 2;
UPDATE stuentss  SET phone_number = 1234567890 WHERE student_id=3;
UPDATE studentss SET phone_number = 0012030415 WHERE student_id = 4;
UPDATE stuentss  SET phone_number = 1234567890 WHERE student_id=5;

create database collage;
use collage;
create table student (
id INT primary key not null,
name varchar(50),
age INT,
marks INT,
city varchar(50)
);

insert into student values 
(1,"Shilpa",20,85,"Chennai"),
(2,"Sruthi",21,90,"Hydrabad"),
(3,"Shilpa",22,75,"Chennai"),
(4,"Rohan",20,60,"Mumbai"),
(5,"Anil",23,90,"Delhi");

-- order by 
select * from student order by marks;
select * from student order by marks desc;

-- aggregate function
-- SELECT student_name ,MIN(marks) as minimum_marks FROM stdunet;

select MAX(marks) from student;
select SUM(marks) from student;
select AVG(marks) from student;
select COUNT(marks) FROM student;


-- sub quiery
select name ,marks FROM student where marks=(select MIN(marks) from student);
select name ,marks FROM student where marks=(select MAX(marks) from student);

-- GROUP BY
-- TO FIND HOW MANY STUDENTS ARE THERE IN EACH CITY
SELECT city ,count(*) as student_count from student group by city;



CREATE TABLE sales (
    sale_id INT,
    product VARCHAR(50),
    category VARCHAR(50),
    quantity INT,
    price INT,
    city VARCHAR(50),
    salesperson VARCHAR(50)
);

INSERT INTO sales VALUES
(1, 'Laptop', 'Electronics', 2, 55000, 'Chennai', 'Arun'),
(2, 'Mobile', 'Electronics', 5, 20000, 'Chennai', 'Meera'),
(3, 'Chair', 'Furniture', 10, 3000, 'Mumbai', 'Rahul'),
(4, 'Laptop', 'Electronics', 1, 55000, 'Delhi', 'Anu'),
(5, 'Table', 'Furniture', 4, 7000, 'Mumbai', 'Rahul'),
(6, 'Mobile', 'Electronics', 3, 20000, 'Hyderabad', 'Meera'),
(7, 'Headphones', 'Accessories', 8, 2500, 'Delhi', 'Anu'),
(8, 'Chair', 'Furniture', 6, 3000, 'Chennai', 'Arun'),
(9, 'Laptop', 'Electronics', 3, 55000, 'Hyderabad', 'Meera'),
(10, 'Keyboard', 'Accessories', 7, 1500, 'Delhi', 'Anu'),
(11, 'Table', 'Furniture', 5, 7000, 'Mumbai', 'Rahul'),
(12, 'Mobile', 'Electronics', 4, 20000, 'Chennai', 'Arun'),
(13, 'Headphones', 'Accessories', 10, 2500, 'Hyderabad', 'Meera'),
(14, 'Chair', 'Furniture', 8, 3000, 'Delhi', 'Anu'),
(15, 'Laptop', 'Electronics', 2, 55000, 'Chennai', 'Arun');





select * FROM sales;
-- find the total quantity sold for each product
SELECT product, SUM(quantity) as total_quantity FROM sales GROUP BY product;
-- find the no of sales for each product
select product ,count(*) AS total_sales FROM sales group by product;

-- find the tiotal qnt sold in each city
select city,sum(quantity) as total_quantity from sales group by city;

-- find the average price for each product category
select category,avg(price) from sales group by category;
select product,avg(price) from sales group by product;

-- find the highest p[roduct oprice in each cat
select category,max(price) from sales group by category;

-- TCL transcation control language
START transaction;
update sales set quantity=10 where sale_id=5;
use collage;
select * from sales;
rollback;
commit;
-- savepoint sp1;
-- update sales set price=5000 where sale_id=4;
-- update sales set quantity=10 where sale_id=6;
-- update sales set city="Adimaly" where sale_id=9;
-- insert into sales values 
-- (16,"phone","Electronics",7,99000,"kerala","jithu"),
-- (17,"camera","Electronics",2,100000,"thrissur","Ram"),
-- (18,"chair","Furniture",8,15000,"Angamaly","Deepu"),
-- (19,"lamp"."Accessories",3,5000,"Kottayam","Abay");
-- rollback to savepoint sp1;
-- commit;

start transaction;
update sales set price=15000 where sale_id=4;
update sales set quantity=8 where sale_id=6;
savepoint sp1;
update sales set city="Mumbai" where sale_id=9;
rollback to sp1;


-- DCL data control language
-- grant select on collage_db.sales to "Arun";
-- grant select ,insert,update on collage_db.sales to "Anu";
-- revoke insert on collage_db.sales from "Anu";

select user();
create user "student1"@"localhost" identified by "1234";
grant select on collage_db.sales to  "student1"@"localhost";
show grants for  "student1"@"localhost";
show databases;
select database();
show tables;
show tables from collage;
show columns from sales;
describe sales;



CREATE DATABASE college;

USE college;

CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    city VARCHAR(50)
);

INSERT INTO students (id, name, age, city) VALUES
(1, 'Rahul', 20, 'Kochi'),
(2, 'Anu', NULL, 'Kochi'),
(3, 'Arun', 22, NULL),
(4, 'Meera', NULL, 'Chennai');

select * from students where age is NULL;
select * from students where age is not NULL;
select * from students where city is not NULL;

--  check wheather a sub query returns atleast 1 row
SELECT EXISTS (
SELECT 1
FROM students
WHERE name = "Rahul"
) AS result;

select salesperson, quantity,
case
when quantity>5 then 'HIGH'
when quantity between 4 and 2 then 'MEDIUM'
else 'LOW'
end as sales_rate from sales;