#!/usr/bin/python3
""" docstring """


import sys
import sqlite3 as sqlite


class DBHandler():
    """ docstring """
    
    def __init__(self):
        self.db = "monsters"
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
            for x in range(len(terraintype)):
                print(x)
                if x == 0:
                    tmpstring += " " + terraintype[x] + " = 'YES'"
                if x > 0:
                    tmpstring += " or " + terraintype[x] + " = 'YES'"
            query = "SELECT * FROM monsters WHERE" + tmpstring + ";"
            print(query)
            cur.execute(query)
            rows = cur.fetchall()
            for row in rows:
                print(row)
        return 0
        
        
# only for testing
if __name__ == '__main__':

    db = DBHandler()
    db.connect()
    ter = ["Arctic", "Urban"]
    db.getRelevantMonsterData(ter)
