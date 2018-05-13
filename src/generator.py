""" Encounter number and types are generated here. """
# TODO:
# fix function naming conventions and variable names
#
# look into a bottom bound on creatures returned from getCreatureData()
#
# simplify _determineEncountersAndNumbers() and implement frequency slider and nighttime encounter adjustments
#
# make terrain types and travel types exclusive
#
# make single day and single night both checked equal 2 periods



import random
from database import DBHandler


class DndEncGen():
    """ Class handles encounter generation. """

    def __init__(self):
        self.db = DBHandler()
        self.terrains = []
        self.travels = []
        self.partysize = 0
        self.partylevel = 0
        # time[0] = months, time[1] = weeks, time[2] = days
        # time[3] = day or night = 1 or -1
        self.time = [0, 0, 0, 0]
        self.freqadjust = 50
        self.xplvl1 = 25
        # traveltype[0] = highway, traveltype[1] = road
        # traveltype[2] = trail, traveltype[3] = wilderness
        self.traveltype = [{"merchantcaravan": 85, "travellers": 75,
                            "lonetraveller": 65, "soldiers": 45,
                            "adventurers": 35, "monsters":  5,
                            "animals": 3},
                           {"merchantcaravan": 65, "travellers": 50,
                            "lonetraveller": 40, "soldiers": 35,
                            "adventurers": 20, "monsters": 10,
                            "animals": 15},
                           {"merchantcaravan": 0, "travellers": 15,
                            "lonetraveller": 5, "soldiers": 10,
                            "adventurers": 5, "monsters":  35,
                            "animals": 45},
                           {"merchantcaravan": 0, "travellers": 5,
                            "lonetraveller": 0, "soldiers": 20,
                            "adventurers": 5, "monsters":  45,
                            "animals": 65}]
        self.terraintypemod = {"arctic": 80,
                               "coast": 120,
                               "desert": 80,
                               "forest": 120,
                               "Grassland": 100,
                               "hills": 100,
                               "mountains": 75,
                               "swamp": 120,
                               "underdark": 100,
                               "underwater": 100,
                               "urban": 125}
        self.encounters = {"merchantcaravan": 0, "travellers": 0,
                           "lonetraveller": 0, "soldiers": 0,
                           "adventurers": 0, "monsters": 0,
                           "animals": 0}
        self.maxencounters = {"merchantcaravan": 20, "travellers": 15,
                              "lonetraveller": 10, "soldiers": 5,
                              "adventurers": 3, "monsters": 2,
                              "animals": 2}

    def generateEncounter(self):
        """ This is the master function that starts the process of displaying a
        new window with the randomly generated encounters. """
        print("Terrain Types = ", self.terrains)
        print("Travel Types = ", self.travels)
        print("Party Size = ", self.partysize)
        print("Average Party Level = ", self.partylevel)
        print("time = ", self.time)
        print("freqadjust = ", self.freqadjust)
        self._determineEncoutersAndNumbers()
        print("Encounters = ", self.encounters)
        x, y = self.getEncounters()
        print(x)
        print(y)
        
        self.reset()
        return 0

    def _determineEncoutersAndNumbers(self):
        """ This method gneerates the encounters dict that contains ecounter
        type and count.  """
# need to implement encounter frequency adjustment and break this down into multiple methods
        months = 0
        weeks = 0
        days = 0
        daynight = self.time[3]
        numberofperiods = 0
        nightmod = 100
        if self.time[0] != 0:
            months = self.time[0]
        if self.time[1] != 0:
            weeks = self.time[1]
        if self.time[2] != 0:
            days = self.time[2]
        numberofperiods = (months * 30) + (weeks * 7) + (days)
        if daynight == 1 or daynight == -1:
            numberofperiods = 1
        if daynight == -1:
            nightmod = 150
# create dict with nighttime chance mods to modify the standard traveltype chance
        print("Number of Periods = ", numberofperiods)
        for period in range(0, numberofperiods):
            for item in self.travels:
                if item == "Highway":
                    for key, value in self.traveltype[0].items():
                        rand = random.randrange(1, 100)
                        if rand <= value:
                            # need to implement nightmod
                            max = int(self.maxencounters[key] * (value * .01))
                            if max < 2:
                                max = 2
                            randnum = random.randrange(1, max)
                            self.encounters[key] += randnum
                if item == "Road":
                    for key, value in self.traveltype[1].items():
                        rand = random.randrange(1, 100)
                        if rand <= value:
                            # need to implement nightmod
                            max = int(self.maxencounters[key] * (value * .01))
                            if max < 2:
                                max = 2
                            randnum = random.randrange(1, max)
                            self.encounters[key] += randnum
                if item == "Trail":
                    for key, value in self.traveltype[2].items():
                        rand = random.randrange(1, 100)
                        if rand <= value:
                            # need to implement nightmod
                            max = int(self.maxencounters[key] * (value * .01))
                            if max < 2:
                                max = 2
                            randnum = random.randrange(1, max)
                            self.encounters[key] += randnum
                if item == "Wilderness":
                    for key, value in self.traveltype[3].items():
                        rand = random.randrange(1, 100)
                        if rand <= value:
                            # need to implement nightmod
                            max = int(self.maxencounters[key] * (value * .01))
                            if max < 2:
                                max = 2
                            randnum = random.randrange(1, max)
                            self.encounters[key] += randnum
        return 0

    def encounterDifficulty(self):
        """ Used for individual encounters to randomize the encounter
        difficulty. """
        difficulty = random.randrange(1, 16)
        if difficulty == 1:
            difficultyname = "Easy"
        if difficulty > 1 and difficulty < 10:
            difficultyname = "Medium"
        if difficulty >= 10 and difficulty < 16:
            difficultyname = "Hard"
        if difficulty == 16:
            difficultyname = "Deadly"
        return difficultyname
                
    def encounterMaxXP(self):
        """ Used for individual encounters to calculate the max XP for the
        encounter given the randomly decided difficulty. """
        difficulty = self.encounterDifficulty()
        charlvlxpthresh = self.db.getCharacterLevelXPThreshold(difficulty, self.partylevel)
        maxxp = charlvlxpthresh * int(self.partysize)
        return maxxp, difficulty
    
    def encounterCreatures(self, maxxp, beastflag=None):
        """ Used for individual encounters to find the creatures in the XP
        range. """
        creatures = self.db.getCreaturesData(self.terrains, maxxp, beastflag)
        return creatures
        
    def creatureNumbers(self, maxxp, creaturexp):
        """ Used for individual encounters to figure out the different numbers
        of creatures in the possible range of the XP threshold."""
        if maxxp == creaturexp:
            return 1
        for i in range(2, 26):
            tmp = creaturexp * i
            if i == 2:
                tmp = tmp * 1.5
            if i > 2 and i < 7:
                tmp = tmp * 2
            if i > 6 and i < 11:
                tmp = tmp * 2.5
            if i > 10 and i < 15:
                tmp = tmp * 3
            if i > 14:
                tmp = tmp * 4
            if tmp > maxxp:
                return i - 1
            if i == 25:
                return i
    
    def encounter(self, beastflag=None):
        """ This outputs the number of creatures inthe encounter and the basic
        creature data."""
        maxxp, difficulty = self.encounterMaxXP()
        # print("\nDifficulty = ", difficulty)
        # print("Max XP = ", maxxp)
        creaturelist = self.encounterCreatures(maxxp, beastflag)
        # print("Creature List = ")
        # for item in creaturelist:
            # print(item[0], item[4])
        creature = creaturelist[random.randrange(0,len(creaturelist))]
        # print(creature)
        numberofcreatures = self.creatureNumbers(maxxp, creature[4])
        # print("Number of Creatures = ", numberofcreatures)
        returnarray = [numberofcreatures, creature]
        # print(returnarray)
        return returnarray
        
    def getEncounters(self):
        """ This returns all encounters for the period of the type monster and
        animal. """
        monsterencounters = []
        beastencounters = []
        for each in range(0, self.encounters["monsters"]):
            x = self.encounter()
            monsterencounters.append(x)
        for each in range(0, self.encounters["animals"]):
            y = self.encounter(1)
            beastencounters.append(y)
        return monsterencounters, beastencounters
        
        
    def reset(self):
        """ Resets all of the attributes of this class """
        self.terrains = []
        self.travels = []
        self.partysize = 0
        self.partylevel = 0
        self.challengerating = 0
        self.time = [0, 0, 0, 0]
        self.freqadjust = 50
        self.encounters = {"merchantcaravan": 0, "travellers": 0,
                           "lonetraveller": 0, "soldiers": 0,
                           "adventurers": 0, "monsters": 0,
                           "animals": 0}
