CREATE TABLE cities(
	cid INT AUTO_INCREMENT, 
	name VARCHAR(100) NOT NULL,
	PRIMARY KEY(cid)
);

INSERT INTO 
	cities(cid, name)
VALUES
	(1,"mumbai"),
	(2,"pune"),
	(3,"patna"),
	(4,"delhi");

SELECT * FROM cities;

CREATE TABLE students(
  id INT not null unique AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100)  not null unique,
  city_id INT null ,
  PRIMARY KEY(id),
  foreign key(city_id) references cities(cid)
);

INSERT INTO students(name,email,city_id)
VALUES
("a","a@gmail.com",1),
("b","b@gmail.com",2),
("d","d@gmail.com",4);
INSERT INTO students(name,email)
VALUES
("f","f@gmail.com");

SELECT * FROM students;

SELECT *FROM students 
INNER JOIN cities
ON students.city_id=cities.cid;



