""" Encounter number and types are generated here. """


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
        self.xptocr = dict([(10, '0'), (25, '1/8'), (50, '1/4'), (100, '1/2'), (200, '1'),
                            (450, '2'), (700, '3'), (1100,
                                                     '4'), (1800, '5'), (2300, '6'),
                            (2900, '7'), (3900, '8'), (5000,
                                                       '9'), (5900, '10'), (7200, '11'),
                            (8400, '12'), (10000, '13'), (11500, '14'), (13000, '15'),
                            (15000, '16'), (18000,
                                            '17'), (20000, '18'), (22000, '19'),
                            (25000, '20'), (33000,
                                            '21'), (41000, '22'), (50000, '23'),
                            (62000, '24'), (75000, '25'), (90000,
                                                           '26'), (105000, '27'),
                            (120000, '28'), (135000, '29'), (155000, '30')])

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
        self._genMonsterAndAnimalEncounters()
        # self._calculateDifficultyInXP()
        # print(self.xpforencouner)

        self.reset()
        return 0

    def _determineEncoutersAndNumbers(self):
        """ This method gneerates the encounters dict that contains ecounter
        type and count.  """
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

    def _calculateDifficultyInXP(self):
        """ this calculates total xp available for the encounter and
        has a set likelihood of different encounter difficulties. This
        difficulty range might need to be made dynamic."""
        difficulty = random.randrange(1, 16)
        # easy
        if difficulty == 1:
            difficultyname = "easy"
            xpforencouner = (self.xplvl1 * int(self.partylevel) *
                             int(self.partysize))
        # medium
        if difficulty > 1 and difficulty < 10:
            difficultyname = "medium"
            xpforencouner = (self.xplvl1 * int(self.partylevel) *
                             int(self.partysize) * 2)
        # hard
        if difficulty >= 10 and difficulty < 16:
            difficultyname = "hard"
            xpforencouner = (self.xplvl1 * int(self.partylevel) *
                             int(self.partysize) * 3)
        # deadly
        if difficulty == 16:
            difficultyname = "deadly"
            xpforencouner = (self.xplvl1 * int(self.partylevel) *
                             int(self.partysize) * 4)
        return xpforencouner, difficultyname

    def _genMonsterAndAnimalEncounters(self):
        """ docstring """
        for each in range(0, self.encounters["monsters"]):
            xp, diff = self._calculateDifficultyInXP()
            print("xp = ", xp)
            cr = 0
            previouskey = 0
            for key, value in self.xptocr.items():
                if xp <= key and xp >= previouskey:
                    cr = value
                    print("cr = ", cr)
                previouskey = key
            potentialmonsters = self.db.getRelevantMonsterData(
                self.terrains, cr)
            print("difficulty = ", diff)
            # for item in potentialbeasts:
            #     print(item)
        for each in range(0, self.encounters["animals"]):
            xp, diff = self._calculateDifficultyInXP()
            print("xp = ", xp)
            cr = 0
            previouskey = 0
            for key, value in self.xptocr.items():
                if xp <= key and xp >= previouskey:
                    cr = value
                    print("cr = ", cr)
                previouskey = key
            potentialbeasts = self.db.getRelevantBeastData(self.terrains, cr)
            print("difficulty = ", diff)
            # for item in potentialbeasts:
            #     print(item)
            # parse the selection of beasts to find a number of beast whos crs equal the cr value
        return

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
