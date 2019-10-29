CREATE TABLE uczniowie (
	id_ucznia CHAR(8) PRIMARY KEY,
	imie VARCHAR(30) NOT NULL,
	nazwisko VARCHAR(30) NOT NULL,
    klasa CHAR(4) DEFAULT ''
    
);

CREATE TABLE oceny(
	id_oceny INTEGER(8) PRIMARY KEY AUTO_INCREMENT,
	data DATE,
	id_ucznia CHAR(8) NOT NULL ,
	id_przed INTEGER NOT NULL,
	ocena DECIMAL(3,2)
	FOREIGN KEY(id_ucznia) REFERENCES (id_ucznia)
    ON DELETE CASCADE
);

CREATE TABLE przedmioty(
	id_przed INTEGER PRIMARY KEY AUTO_INCREMENT,
	przedmiot VARCHAR(30)
);
