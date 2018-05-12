#!/usr/bin/python3
""" docstring """


import sys
import sqlite3 as sqlite


class DBHandler():
    """ docstring """
    
    def __init__(self):
        self.db = "monsters.db"
        self.con = ""
        
    def connect(self):
        """ docstring """
        self.con = sqlite.connect(self.db)
        return 0
        
    def getRelevantMonsterData(self, terraintype):
        """ docstring """
        with self.con:
            cur = self.con.cursor()
            tmpstring = ""
            returnlist = []
            for x in range(len(terraintype)):
                print(x)
                if x == 0:
                    tmpstring += " (" + terraintype[x] + " = 'YES'"
                if x > 0:
                    tmpstring += " or " + terraintype[x] + " = 'YES'"
            query = "SELECT Name, Type, ALIGNMENT, Size, CR, AC, HP, \
                    Attack1dmg, Attack2dmg, Spellcasting FROM monsters WHERE" \
                    + tmpstring + ") and Type != 'Beast';"
            print(query)
            cur.execute(query)
            rows = cur.fetchall()
            for row in rows:
                # print(row)
                returnlist.append(row)
        return returnlist
        
    def getRelevantBeastData(self, terraintype):
        """ docstring """
        with self.con:
            cur = self.con.cursor()
            tmpstring = ""
            returnlist = []
            for x in range(len(terraintype)):
                print(x)
                if x == 0:
                    tmpstring += " (" + terraintype[x] + " = 'YES'"
                if x > 0:
                    tmpstring += " or " + terraintype[x] + " = 'YES'"
            query = "SELECT Name, Type, ALIGNMENT, Size, CR, AC, HP, \
                    Attack1dmg, Attack2dmg, Spellcasting FROM monsters WHERE" \
                    + tmpstring + ") and Type = 'Beast';"
            print(query)
            cur.execute(query)
            rows = cur.fetchall()
            for row in rows:
                # print(row)
                returnlist.append(row)
        return returnlist
        
        
# only for testing
if __name__ == '__main__':

    db = DBHandler()
    db.connect()
    ter = ["Arctic", "Urban"]
    db.getRelevantMonsterData(ter)
