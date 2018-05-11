""" docstring shit """


import random


class DndEncGen():
    """ may not need to set a challenge rating """

    def __init__(self):
        self.terrains = []
        self.travels = []
        self.partysize = 0
        self.partylevel = 0
        # self.challengerating = 0
        # time[0] = months, time[1] = weeks, time[2] = days
        # time[3] = day or night = 1 or -1
        self.time = [0, 0, 0, 0]
        self.freqadjust = 50
        self.xpforencouner = 0
        self.xplvl1 = 25
        # traveltype[0] = highway, traveltype[1] = road
        # traveltype[2] = trail, traveltype[3] = wilderness
        self.traveltype = [{"merchantcaravan": 95, "travellers": 85,
                            "lonetravellers": 65, "soldiers": 45,
                            "adventurers": 35, "monsters":  5,
                            "animals": 3},
                           {"merchantcaravan": 65, "travellers": 50,
                            "lonetraveller": 40, "soldiers": 35,
                            "adventurers": 20, "monsters": 10,
                            "animals": 15},
                           {"merchantcaravan": 0, "travellers": 15,
                            "lonetravellers": 5, "soldiers": 10,
                            "adventurers": 5, "monsters":  35,
                            "animals": 45},
                           {"merchantcaravan": 0, "travellers": 5,
                            "lonetravellers": 0, "soldiers": 20,
                            "adventurers": 5, "monsters":  45,
                            "animals": 65}]
        self.terraintypemod = {"arctic": 90,
                               "coast": 110,
                               "desert": 90,
                               "forest": 110,
                               "grasslands": 100,
                               "hills": 100,
                               "mountains": 95,
                               "swamp": 110,
                               "underdark": 100,
                               "underwater": 100,
                               "urban": 105}
        self.encounters = {"merchantcaravan": 0, "travellers": 0,
                           "lonetraveler": 0, "soldiers": 0,
                           "adventurers": 0, "monsters": 0,
                           "animals": 0}

    def generateEncounter(self):
        """ This is the master function that starts the process of displaying a
        new window with the randomly generated encounters. """
        print(self.terrains)
        print(self.travels)
        print(self.partysize)
        print(self.partylevel)
        print(self.challengerating)
        print(self.time)
        print(self.freqadjust)
        self._determineEncoutersAndNumbers()
        print(self.encounters)
        self._calculateDifficultyInXP()
        print(self.xpforencouner)

        self.reset()

    def _determineEncoutersAndNumbers(self):
        """ This method gneerates the encounters dict that contains ecounter
        type and count.  """
        months = 0
        weeks = 0
        days = 0
        daynight = 0
        numberofperiods = 0
        nightmod = 100
        if self.time[3] == 1:
            daynight = self.time[0]
        if self.time[0] != 0:
            months = self.time[0]
        if self.time[1] != 0:
            weeks = self.time[1]
        if self.time[2] != 0:
            days = self.time[2]
        if daynight == 0:
            numberofperiods = (months * 30) + (weeks * 7) + (days)
        elif daynight != 0:
            numberofperiods = 1
        if daynight == -1:
            nightmod = 150

        for item in self.travels:
            if item == "Highway":
                for key, value in self.traveltype[0].items():
                    rand = random.randrange(1, 100)
                    if rand <= value:
                        # need to implement range calc and terrainmod/nightmod
                        # randnum = random.randrange(1, 19)
                        self.encounters[key] += 1
            if item == "Road":
                for key, value in self.traveltype[1].items():
                    rand = random.randrange(1, 100)
                    if rand <= value:
                        # need to implement range calc and terrainmod/nightmod
                        # randnum = random.randrange(1, 19)
                        self.encounters[key] += 1
            if item == "Trail":
                for key, value in self.traveltype[2].items():
                    rand = random.randrange(1, 100)
                    if rand <= value:
                        # need to implement range calc and terrainmod/nightmod
                        # randnum = random.randrange(1, 19)
                        self.encounters[key] += 1
            if item == "Wilderness":
                for key, value in self.traveltype[3].items():
                    rand = random.randrange(1, 100)
                    if rand <= value:
                        # need to implement range calc and terrainmod/nightmod
                        # randnum = random.randrange(1, 19)
                        self.encounters[key] += 1

    def _calculateDifficultyInXP(self):
        """ this calculates total xp available for the encounter and
        has a set likelihood of different encounter difficulties. This
        difficulty range might need to be made dynamic."""
        difficulty = random.randrange(1, 16)
        # easy
        if difficulty == 1:
            self.xpforencouner = (self.xplvl1 * int(self.partylevel) *
                                  int(self.partysize))
        # medium
        if difficulty > 1 and difficulty < 10:
            self.xpforencouner = (self.xplvl1 * int(self.partylevel) *
                                  int(self.partysize) * 2)
        # hard
        if difficulty >= 10 and difficulty < 16:
            self.xpforencouner = (self.xplvl1 * int(self.partylevel) *
                                  int(self.partysize) * 3)
        # deadly
        if difficulty == 16:
            self.xpforencouner = (self.xplvl1 * int(self.partylevel) *
                                  int(self.partysize) * 4)

    def reset(self):
        self.terrains = []
        self.travels = []
        self.partysize = 0
        self.partylevel = 0
        self.challengerating = 0
        self.time = [0, 0, 0, 0]
        self.freqadjust = 50

    def createNewWindow(self):
        """ bs """
        pass
