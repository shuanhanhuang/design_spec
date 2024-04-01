-- 已經在 mysql 建好了
CREATE DATABASE Class;
use Class;

create table Student(
	id int primary key auto_increment,
    s_id int(10) not null,
    s_name varchar(50) not null,
    s_sex varchar(10) not null,
    s_birthday Date NOT NULL,
    s_score float NOT NULL
);

select * from student;

INSERT INTO Student (s_id, s_name, s_sex, s_birthday, s_score) VALUES
(111018000,"黃曉明","男","2000-01-15",89.2),
(111018010,"陳大通","男","1999-11-21",97.3),
(111018021,"李美華","女","2000-04-04",60.5),
(111018156,"王謙","男","2000-03-10",48.2);
