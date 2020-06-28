CREATE TABLE Users(
	name VARCHAR(128),
	email VARCHAR(128)
)

INSERT INTO Users (name,email) VALUES ("Kristin","kf@gmail.com")

DELETE FROM Users WHERE email="fred@gmail.com.tw"

UPDATE Users SET name="Charles" WHERE email="csev@umich.edu"

SELECT*FROM

SELECT*FROM Users WHERE email="csev@umich.edu"

SELECT*FROM Users ORDER BY email
SELECT*FROM Users ORDER BY name

###################### HW1 ########################

Then, create a SQLITE database or use an existing database and create a table in the database called "Ages":

CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)
Then make sure the table is empty by deleting any rows that you previously inserted, and insert these rows and only these rows with the following commands:

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Samuel', 16);
INSERT INTO Ages (name, age) VALUES ('Razan', 25);
INSERT INTO Ages (name, age) VALUES ('Karol', 21);
INSERT INTO Ages (name, age) VALUES ('Keirra', 32);
Once the inserts are done, run the following SQL command:
SELECT hex(name || age) AS X FROM Ages ORDER BY X