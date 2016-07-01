#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("DELETE FROM matches")
    cursor.execute("UPDATE players SET wins = 0, matchesPlayed = 0")
    DB.commit()
    DB.close()

def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("DELETE FROM players")
    DB.commit()
    DB.close()

def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("SELECT count(*) FROM players")
    playerCount = cursor.fetchall()
    DB.close
    return playerCount[0][0]

def registerPlayer(name):
   DB = connect()
   cursor = DB.cursor()
   cursor.execute("INSERT INTO players (name, wins, matchesPlayed) Values (%s, 0, 0)", (name,))
   DB.commit()
   DB.close()


def playerStandings():
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("SELECT * FROM players ORDER BY wins")
    standings = cursor.fetchall()
    DB.close()
    return standings


def reportMatch(winner, loser):
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("INSERT INTO matches VALUES (%s, %s)", (winner, loser))
    #loser query
    cursor.execute("UPDATE players SET matchesPlayed = matchesPlayed + 1 WHERE id = %s", (loser,))
    #winner query
    cursor.execute("UPDATE players SET wins = wins + 1, matchesPlayed = matchesPlayed + 1 WHERE id = %s", (winner,))
    DB.commit()
    DB.close()
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """


