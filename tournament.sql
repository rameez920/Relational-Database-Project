-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--


CREATE TABLE players (id SERIAL PRIMARY KEY,
						name TEXT,
						wins INTEGER,
						matchesPlayed INTEGER);



CREATE TABLE matches (winner SERIAL REFERENCES players,
						loser SERIAL REFERENCES players,
						matchID SERIAL PRIMARY KEY);



CREATE TABLE swissPairings(player1 SERIAL REFERENCES players,
							player1Name TEXT REFERENCES players,
							player2 SERIAL REFERENCES players,
							player2Name TEXT REFERENCES players);