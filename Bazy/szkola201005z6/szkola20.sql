DROP TABLE IF EXISTS Uczniowie;
DROP TABLE IF EXISTS Przedmioty;
DROP TABLE IF EXISTS Oceny;

CREATE TABLE Uczniowie
(
  id_ucznia INTEGER PRIMARY KEY,
  nazwisko TEXT(20),
  imie TEXT,
  ulica TEXT,
  dom INTEGER,
  klasa_id TEXT
);

CREATE TABLE Przedmioty
(
  id_przedmiotu INTEGER PRIMARY KEY,
  przedmiot TEXT,
  nau_naz TEXT,
  nau_imie TEXT
);

CREATE TABLE Oceny
(
  id_ucznia INTEGER,
  ocena INTEGER,
  data DATE,
  id_przedmiotu INTEGER,
  FOREIGN KEY (id_przedmiotu) REFERENCES Przedmioty(id_przedmiotu)
  FOREIGN KEY (id_ucznia) REFERENCES Uczniowie(id_ucznia)
);
