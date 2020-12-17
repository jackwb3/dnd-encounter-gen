""" Docstring """

class GeneratorSetup():
    """ Docstring """

    def __init__(self):
        self.terraintype = []
        self.traveltype = []
        self.partysize = 0
        self.partylevel = 0
        """
            time[0] = months,
            time[1] = weeks,
            time[2] = days
            time[3] = dayflag = 1,
            time[4] = nightflag = 1
        """
        self.time = [0, 0, 0, 0, 0]
        self.freqadjust = 0
        self.previousgenerationflag = 0
