#!/usr/bin/python3
""" docstring """


import sys
import sqlite3 as sqlite


class DBHandler():
    """ docstring """
    
    def __init__(self):
        self.db = "monsters.db"
        self.con = self.connect()
        
    def connect(self):
        """ docstring """
        conn = sqlite.connect(self.db)
        return conn
        
    def getRelevantMonsterData(self, terraintype, cr):
        """ docstring """
        with self.con:
            cur = self.con.cursor()
            tmpstring = ""
            returnlist = []
            cr = "'" + cr + "'"
            for x in range(len(terraintype)):
                if x == 0:
                    tmpstring += " (" + terraintype[x] + " = 'YES'"
                if x > 0:
                    tmpstring += " or " + terraintype[x] + " = 'YES'"
            query = "SELECT Name, Type, ALIGNMENT, Size, CR, AC, HP, \
                    Attack1dmg, Attack2dmg, Spellcasting FROM monsters WHERE" \
                    + tmpstring + ") and Type != 'Beast' and CR <= " + cr + ";"
            cur.execute(query)
            rows = cur.fetchall()
            for row in rows:
                returnlist.append(row)
        return returnlist
        
    def getRelevantBeastData(self, terraintype, cr):
        """ docstring """
        with self.con:
            cur = self.con.cursor()
            tmpstring = ""
            returnlist = []
            cr = "'" + cr + "'"
            for x in range(len(terraintype)):
                if x == 0:
                    tmpstring += " (" + terraintype[x] + " = 'YES'"
                if x > 0:
                    tmpstring += " or " + terraintype[x] + " = 'YES'"
            query = "SELECT Name, Type, ALIGNMENT, Size, CR, AC, HP, \
                    Attack1dmg, Attack2dmg, Spellcasting FROM monsters WHERE" \
                    + tmpstring + ") and Type = 'Beast' and CR <= " + cr + ";"
            cur.execute(query)
            rows = cur.fetchall()
            for row in rows:
                returnlist.append(row)
        return returnlist
        
        
# only for testing
if __name__ == '__main__':

    db = DBHandler()
    db.connect()
    ter = ["Arctic", "Urban"]
    db.getRelevantMonsterData(ter)
