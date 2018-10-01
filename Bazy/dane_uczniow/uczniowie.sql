DROP TABLE IF EXISTS Nazwiska;
DROP TABLE IF EXISTS Dane;
DROP TABLE IF EXISTS Oceny;

CREATE TABLE Nazwiska
(
  id INTEGER PRIMARY KEY,
  nazwisko TEXT(20),
  pierwsze_imie TEXT,
  drugie_imie TEXT
);

CREATE TABLE Dane (
  id_Nazwiska INTEGER,
  dzien_urodzenia INTEGER,
  miesiąc_urodzenia INTEGER,
  rok_urodzenia INTEGER,
  miejsce_urodzenia TEXT,
  wojewodztwo TEXT,
  FOREIGN KEY (id_Nazwiska) REFERENCES Nazwiska(id)
);

CREATE TABLE Oceny (
  id_Nazwiska INTEGER,
  zachowanie TEXT(15),
  rel_ety INTEGER DEFAULT "",
  jpol INTEGER DEFAULT "",
  jang INTEGER DEFAULT "",
  jniem INTEGER DEFAULT "",
  mat INTEGER DEFAULT "",
  hist INTEGER DEFAULT "",
  grog INTEGER DEFAULT "",
  biol INTEGER DEFAULT "",
  fiz INTEGER DEFAULT "",
  che INTEGER DEFAULT "",
  tech INTEGER DEFAULT "",
  info INTEGER DEFAULT "",
  plas INTEGER DEFAULT "",
  po INTEGER DEFAULT "",
  wf INTEGER DEFAULT "",
  FOREIGN KEY (id_Nazwiska) REFERENCES Nazwiska(id)
);
