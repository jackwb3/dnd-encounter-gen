#!/usr/bin/python3
""" This module handles database interactions. """


import sys
import sqlite3 as sqlite


class DBHandler():
    """ docstring """
    
    def __init__(self):
        self.db = "monsters.db"
        self.con = self._connect()
        
    def _connect(self):
        """ docstring """
        conn = sqlite.connect(self.db)
        return conn
        
    def getCharacterLevelXPThreshold(self, difficulty, level):
        with self.con:
            cur = self.con.cursor()
            query = "SELECT " + difficulty + " FROM characterlvlencounter WHERE CharacterLevel = " + level  + ";"
            # print(query)
            cur.execute(query)
            x = cur.fetchone()
        return int(x[0])
        
    def getCreaturesData(self, terraintype, maxxp, beast=None):
        with self.con:
            cur = self.con.cursor()
            minxp = str(maxxp * 0.25)
            maxxp = str(maxxp)
            tmpstring = ""
            returnlist = []
            for x in range(len(terraintype)):
                if x == 0:
                    tmpstring += " (" + terraintype[x] + " = 'YES'"
                if x > 0:
                    tmpstring += " or " + terraintype[x] + " = 'YES'"
            if beast == None:
                query = "SELECT Name, Type, ALIGNMENT, Size, XP, AC, HP, Attack1dmg, Attack2dmg, Spellcasting FROM monsters WHERE" + tmpstring + ") and Type != 'Beast' and XP <= " + maxxp + ";"
            if beast == 1:
                query = "SELECT Name, Type, ALIGNMENT, Size, XP, AC, HP, Attack1dmg, Attack2dmg, Spellcasting FROM monsters WHERE" + tmpstring + ") and Type = 'Beast' and XP <= " + maxxp + ";"
            # print(query)
            cur.execute(query)
            rows = cur.fetchall()
            for row in rows:
                returnlist.append(row)
                #print(row)
        return returnlist
        
        
# only for testing
if __name__ == '__main__':

    db = DBHandler()
    db.connect()
    ter = ["Arctic", "Urban"]
    db.getRelevantMonsterData(ter)
