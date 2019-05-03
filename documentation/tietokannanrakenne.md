# Tietokannan rakenne

## Tietokantakaavio
<img src="https://github.com/jooala/keskustelufoorumi/blob/master/documentation/tietokantakaavio.png">

## Create Table - lauseet

### Account -taulu

CREATE TABLE Account (
	id INTEGER,
	name VARCHAR(144) NOT NULL,
	username VARCHAR(144) NOT NULL,
	password VARCHAR(144) NOT NULL,
	rank VARCHAR(144) NOT NULL,
	PRIMARY KEY(id)
);

### Categories -taulu

CREATE TABLE Categories (
	id INTEGER,
	date_created DATETIME,
	date_modified DATETIME,
	name VARCHAR(144) NOT NULL,
	desc VARCHAR(144),
	PRIMARY KEY(id)
);

### Topics -taulu

CREATE TABLE Topics (
	id INTEGER,
	date_created DATETIME,
	date_modified DATETIME,
	name VARCHAR(144) NOT NULL,
	desc VARCHAR(144),
	account_id INTEGER NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(account_id) REFERENCES Account(id)
);

### Posts -taulu

CREATE TABLE Posts (
	id INTEGER,
	date_created DATETIME,
	date_modified DATETIME,
	message TEXT NOT NULL,
	account_id INTEGER NOT NULL,
	topics_id INTEGER NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(account_id) REFERENCES Account(id),
	FOREIGN KEY(topics_id) REFERENCES Topics(id)
);

### TopicsCategories -taulu

CREATE TABLE TopicsCategories (
	id INTEGER,
	topics_id INTEGER,
	categories_id INTEGER,
	PRIMARY KEY(id),
	FOREIGN KEY(topics_id) REFERENCES Topics(id),
	FOREIGN KEY(categories_id) REFERENCES Categories(id)
);