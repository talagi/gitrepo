DROP TABLE IF EXISTS pracownicy;
DROP TABLE IF EXISTS place;
DROP TABLE IF EXISTS kontakty;
DROP TABLE IF EXISTS stanowiska;

CREATE TABLE pracownicy (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	imie VARCHAR(15),
	nazwisko VARCHAR(20),
	kod VARCHAR(20),
	miasto_z VARCHAR(25),
	data_u DATE,
	ulica VARCHAR(35),
	miasto_u VARCHAR(25)
);

CREATE TABLE place (
	id_p INTEGER,
	id_s INTEGER,
	placa INTEGER,
	data_z DATE,
	FOREIGN KEY (id_p) REFERENCES pracownicy(id)
	FOREIGN KEY (id_S) REFERENCES stanowiska(id)
);

CREATE TABLE kontakty (
	id_pracownika INTEGER,
	typ_k BOOLEAN,
	kontakt VARCHAR,
	uwagi TEXT,
	FOREIGN KEY (id_pracownika) REFERENCES pracownicy(id)
);

CREATE TABLE stanowiska (
id_stanowiska INTEGER PRIMARY KEY AUTOINCREMENT,
stanowisko VARCHAR,
);