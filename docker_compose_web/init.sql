CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	name TEXT
);

INSERT INTO users(name) VALUES 
	('foo'),
	('bar'),
	('John'),
	('Jane');