""" Encounter number and types are generated here. """
# TODO:
# add detail's filepaths to database and monster/animal query results
#
# randomize individual monsters in encounter adn figure out how to display withlink to details
#
# clean up Total Number of Encounters output
#
# look into selecting monsters by type in gui and generator
#
# consider making db tables for adventurers and soldiers or even commoners
# and generating soldiers adventurers and caravans, using soome random name
# generator
#
# also think of a way to mix creature types that are related
# see about making the moster selection process pick monsters closer tothe
# party level



import random
from database import DBHandler


class EncounterGenerator():
    """ Class handles encounter generation. """

    def __init__(self):
        self.db = DBHandler()
        self.terraintype = []
        self.traveltype = []
        self.partysize = 0
        self.partylevel = 0
        # time[0] = months, time[1] = weeks, time[2] = days
        # time[3] = dayflag = 1, time[4] = nightflag = 1
        self.time = [0, 0, 0, 0, 0]
        self.freqadjust = 0
        self.previousgenerationflag = 0
        # traveltype[0] = highway, traveltype[1] = road
        # traveltype[2] = trail, traveltype[3] = wilderness
        self.encounterchances = [{"merchantcaravan": 85, "travellers": 75,
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
        self.nighttimemods = {"merchantcaravan": 0, "travellers": 5,
                              "lonetraveller": 25, "soldiers": 15,
                              "adventurers": 25, "monsters": 125,
                              "animals": 135}

    def generateEncounter(self):
        """ This is the master function that starts the process of displaying a
        new window with the randomly generated encounters. """
        # print("Terrain Types = ", self.terraintype)
        # print("Travel Types = ", self.traveltype)
        # print("Party Size = ", self.partysize)
        # print("Average Party Level = ", self.partylevel)
        # print("time = ", self.time)
        # print("freqadjust = ", self.freqadjust)
        x, y = self._getEncounters()
        print("\nEncounters = ", self.encounters)
        print("Monsters = ", x)
        print("Animals = ", y)
        return self.encounters, x, y

    def _determineEncoutersAndNumbers(self):
        """ This method gneerates the encounters dict that contains ecounter
        type and count.  """
        numberofperiods = ((self.time[0] * 30) + (self.time[1] * 7) + \
                           self.time[2] + self.time[3] + self.time[4])
        print("Number of Periods = ", numberofperiods)
        for period in range(0, numberofperiods):
            for item in self.traveltype:
                translator = {"Highway": self.encounterchances[0],
                              "Road": self.encounterchances[1],
                              "Trail": self.encounterchances[2],
                              "Wilderness": self.encounterchances[3]}
                for key, value in translator[item].items():
                    if self.time[4] == 1:
                        rand = (random.randrange(1, 100) * self.freqadjust * \
                                (self.nighttimemods[key] * .01))
                    else:
                        rand = (random.randrange(1, 100) * (self.freqadjust * .01))
                    if rand <= value:
                        max = int(self.maxencounters[key] * (value * .01))
                        if max < 2:
                            max = 2
                        randnum = random.randrange(1, max)
                        self.encounters[key] += randnum
        return 0

    def _encounterDifficulty(self):
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
                
    def _encounterMaxXP(self):
        """ Used for individual encounters to calculate the max XP for the
        encounter given the randomly decided difficulty. """
        difficulty = self._encounterDifficulty()
        charlvlxpthresh = self.db.getCharacterLevelXPThreshold(difficulty, self.partylevel)
        maxxp = charlvlxpthresh * int(self.partysize)
        return maxxp, difficulty
    
    def _encounterCreatures(self, maxxp, beastflag=None):
        """ Used for individual encounters to find the creatures in the XP
        range. """
        creatures = self.db.getCreaturesData(self.terraintype, maxxp, beastflag)
        if len(creatures) == 0:
            print("\nZero creatures returned from DB\n")
            return -1
        return creatures
        
    def _creatureNumbers(self, maxxp, creaturexp):
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
    
    def _encounter(self, beastflag=None):
        """ This outputs the number of creatures inthe encounter and the basic
        creature data."""
        maxxp, difficulty = self._encounterMaxXP()
        # print("\nDifficulty = ", difficulty)
        # print("Max XP = ", maxxp)
        creaturelist = self._encounterCreatures(maxxp, beastflag)
        # print("Creature List Length= ", len(creaturelist))
        # for item in creaturelist:
            # print(item[0], item[4])
        creature = creaturelist[random.randrange(0,len(creaturelist))]
        # print(creature)
        numberofcreatures = self._creatureNumbers(maxxp, creature[4])
        # print("Number of Creatures = ", numberofcreatures)
        returnarray = [numberofcreatures, creature]
        # print(returnarray)
        return returnarray
        
    def _getEncounters(self):
        """ This returns all encounters for the period of the type monster and
        animal. """
        monsterencounters = []
        beastencounters = []
        self._determineEncoutersAndNumbers()
        for each in range(0, self.encounters["monsters"]):
            x = self._encounter()
            monsterencounters.append(x)
        for each in range(0, self.encounters["animals"]):
            y = self._encounter(1)
            beastencounters.append(y)
        return monsterencounters, beastencounters
        
        
    def reset(self):
        """ Resets all of the attributes of this class """
        self.terraintype = []
        self.traveltype = []
        self.partysize = 0
        self.partylevel = 0
        self.challengerating = 0
        self.time = [0, 0, 0, 0, 0]
        self.freqadjust = 50
        self.encounters = {"merchantcaravan": 0, "travellers": 0,
                           "lonetraveller": 0, "soldiers": 0,
                           "adventurers": 0, "monsters": 0,
                           "animals": 0}
