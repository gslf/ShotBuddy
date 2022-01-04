CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE sessions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_user INTEGER,
    datetime TEXT,
    percentage_target REAL,
    shots TEXT,
    duration INTEGER,
    FOREIGN KEY(id_user) REFERENCES users(id)
)