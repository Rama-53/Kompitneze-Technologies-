use college;

create table student(
student_id int primary key,
name varchar(50));

create table orders(
order_id int primary key,
student_id int,foreign key(student_id) references student(student_id),
product varchar(50));

insert into student values
(1,'Ajeet'),
(2,'Ratan'),
(3,'Mahesh');

insert into orders values
(101,1,'Book'),
(102,1,'Pen'),
(103,2,'Laptop');

select student.name,orders.product from student inner join orders on student.student_id=orders.student_id;
select student.name,orders.product from student left join orders on student.student_id=orders.student_id;
select student.name,orders.product from student right join orders on student.student_id=orders.student_id;
-- select student.student_name,orders.product from student full outer join orders on student.student_id=orders.student_id;