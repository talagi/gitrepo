DROP TABLE IF EXISTS miasta;
DROP TABLE IF EXISTS mieszkancy;
DROP TABLE IF EXISTS powierzchnie;


CREATE TABLE miasta (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nazwa_miasta TEXT(30),
	wojewodztwo TEXT(35)
);

CREATE TABLE mieszkancy (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	liczba_mieszkancow INTEGER,
	liczba_kobiet INTEGER,
  grupa_wiekowa TEXT(20),
  data_aktualizacji DATE,
  id_miasta INTEGER
);

CREATE TABLE powierzchnie (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	powierzchnia DECIMAL,
	powierzgcnie_zielone INTEGER,
	data_aktualizacji DATE,
	id_miasta INTEGER
);