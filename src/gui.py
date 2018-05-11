#!/usr/bin/python3
""" This tool can be used to generate random encounter for
Dungeons and Dragons 5e. """


import sys
from generator import DndEncGen
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout,
                             QCheckBox, QApplication,
                             QLabel, QGridLayout,
                             QLineEdit, QGroupBox,
                             QSlider, QComboBox)
from PyQt5.QtCore import (pyqtSlot, Qt)


class DndEncGenGUI(QWidget):
    """ This clas is used to construct the GUI. """

    def __init__(self):
        super().__init__()
        self.initUI()

    def _createLeftGroupBox(self):
        """ Creates the terrain options. """
        group = QGroupBox("Terrain Type")
        vbox = QVBoxLayout()
        self.arctic = QCheckBox("Arctic")
        vbox.addWidget(self.arctic)
        self.desert = QCheckBox("Desert")
        vbox.addWidget(self.desert)
        self.coast = QCheckBox("Coast")
        vbox.addWidget(self.coast)
        self.forest = QCheckBox("Forest")
        vbox.addWidget(self.forest)
        self.grasslands = QCheckBox("Grasslands")
        vbox.addWidget(self.grasslands)
        self.hills = QCheckBox("Hills")
        vbox.addWidget(self.hills)
        self.mountains = QCheckBox("Mountains")
        vbox.addWidget(self.mountains)
        self.swamp = QCheckBox("Swamp")
        vbox.addWidget(self.swamp)
        self.underdark = QCheckBox("Underdark")
        vbox.addWidget(self.underdark)
        self.underwater = QCheckBox("Underwater")
        vbox.addWidget(self.underwater)
        self.urban = QCheckBox("Urban")
        vbox.addWidget(self.urban)
        group.setLayout(vbox)
        return group

    def _createMiddleGroupBox(self):
        """ Creates the travel type options. """
        group = QGroupBox("Travel Type")
        vbox = QVBoxLayout()
        self.highway = QCheckBox("Highway")
        vbox.addWidget(self.highway)
        self.road = QCheckBox("Road")
        vbox.addWidget(self.road)
        self.trail = QCheckBox("Trail")
        vbox.addWidget(self.trail)
        self.wilderness = QCheckBox("Wilderness")
        vbox.addWidget(self.wilderness)
        # self.river = QCheckBox("River")
        # vbox.addWidget(self.river)
        # self.sea = QCheckBox("Sea")
        # vbox.addWidget(self.sea)
        group.setLayout(vbox)
        return group

    def _createRightGroupBoxes(self):
        """ Creates the party and time options. """
        vboxright = QVBoxLayout()
        gboxtop = QGroupBox("Party Parameters")
        vboxtop = QVBoxLayout()
        hbox1 = QHBoxLayout()
        numplayerslbl = QLabel("Number of Players")
        self.numplayers = QLineEdit()
        hbox1.addWidget(numplayerslbl)
        hbox1.addWidget(self.numplayers)
        hbox2 = QHBoxLayout()
        avglvllbl = QLabel("Average Level of Players")
        self.avglvl = QLineEdit()
        hbox2.addWidget(avglvllbl)
        hbox2.addWidget(self.avglvl)
        # hbox3 = QHBoxLayout()
        # crlbl = QLabel("Challenge Rating")
        # self.cr = QLineEdit()
        # hbox3.addWidget(crlbl)
        # hbox3.addWidget(self.cr)
        vboxtop.addLayout(hbox1)
        vboxtop.addLayout(hbox2)
        # vboxtop.addLayout(hbox3)
        gboxtop.setLayout(vboxtop)

        gboxbottom = QGroupBox("Time Parameters")
        vboxbottom = QVBoxLayout()
        self.day = QCheckBox("Single Day (daylight hours)")
        self.night = QCheckBox("Single Night (nitghtime hours)")
        self.custom = QCheckBox("Custom Time Range")
        self.custom.stateChanged.connect(self._toggleTimeInput)
        self.customlbl = QLabel()
        self.customlbl.setText("Example: 1m2w3d")
        self.customlbl.hide()
        self.customqle = QLineEdit()
        self.customqle.hide()

        vboxbottom.addWidget(self.day)
        vboxbottom.addWidget(self.night)
        vboxbottom.addWidget(self.custom)
        vboxbottom.addWidget(self.customlbl)
        vboxbottom.addWidget(self.customqle)
        gboxbottom.setLayout(vboxbottom)

        vboxright.addWidget(gboxtop)
        vboxright.addWidget(gboxbottom)
        return vboxright

    def initUI(self):
        """ Initializes the window. """
        self.gen = DndEncGen()

        leftbox = self._createLeftGroupBox()
        middlebox = self._createMiddleGroupBox()
        rightbox = self._createRightGroupBoxes()
        self._createBottomRow()
        mainlayout = QGridLayout()
        mainlayout.setAlignment(Qt.AlignTop)
        mainlayout.setColumnMinimumWidth(0, 200)
        mainlayout.setColumnMinimumWidth(1, 200)
        mainlayout.setColumnMinimumWidth(2, 200)
        mainlayout.addWidget(leftbox, 0, 0)
        mainlayout.addWidget(middlebox, 0, 1)
        mainlayout.addLayout(rightbox, 0, 2)
        mainlayout.addLayout(self.slidervbox, 1, 0)
        mainlayout.addLayout(self.hbox, 1, 2)

        self.setLayout(mainlayout)
        self.setWindowTitle('DnD 5e Encounter Generator')
        self.show()

    def _createBottomRow(self):
        """ maybe add a reset button to clear current settings """
        self.slidervbox = QVBoxLayout()
        sliderlbl = QLabel()
        sliderlbl.setText("Encounter Frequency Adjustment")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(1)
        self.slider.setMaximum(17)
        self.slider.setValue(9)
        self.slidervbox.addWidget(sliderlbl)
        self.slidervbox.addWidget(self.slider)

        self.generatebttn = QPushButton("Generate")
        self.generatebttn.clicked.connect(self.on_click)
        self.quitbttn = QPushButton("Quit")
        self.quitbttn.clicked.connect(QApplication.instance().quit)

        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.generatebttn)
        self.hbox.addWidget(self.quitbttn)

    @pyqtSlot()
    def on_click(self):
        """ Handles click to pass settings to the generator. """
        self.parseParameters()
        self.gen.generateEncounter()

    def _toggleTimeInput(self):
        """ Handles dynamic display of alternate time inputs. """
        if self.custom.isChecked():
            self.day.hide()
            self.night.hide()
            self.customlbl.show()
            self.customqle.show()
        elif not self.custom.isChecked():
            self.day.show()
            self.night.show()
            self.customlbl.hide()
            self.customqle.hide()

    def parseParameters(self):
        """ Loads the values into the generator depending on current
        selections.  """
        if self.arctic.isChecked():
            self.gen.terrains.append("Arctic")
        if self.coast.isChecked():
            self.gen.terrains.append("Coast")
        if self.desert.isChecked():
            self.gen.terrains.append("Desert")
        if self.forest.isChecked():
            self.gen.terrains.append("Forest")
        if self.grasslands.isChecked():
            self.gen.terrains.append("Grasslands")
        if self.hills.isChecked():
            self.gen.terrains.append("Hills")
        if self.mountains.isChecked():
            self.gen.terrains.append("Mountains")
        if self.swamp.isChecked():
            self.gen.terrains.append("Swamp")
        if self.underdark.isChecked():
            self.gen.terrains.append("Underdark")
        if self.underwater.isChecked():
            self.gen.terrains.append("Underwater")
        if self.urban.isChecked():
            self.gen.terrains.append("Urban")

        if self.highway.isChecked():
            self.gen.travels.append("Highway")
        if self.road.isChecked():
            self.gen.travels.append("Road")
        if self.trail.isChecked():
            self.gen.travels.append("Trail")
        if self.wilderness.isChecked():
            self.gen.travels.append("Wilderness")
        # if self.river.isChecked():
        #     self.gen.travels.append("River")
        # if self.sea.isChecked():
        #     self.gen.travels.append("Sea")

        if self.numplayers.text() != "":
            self.gen.partysize = self.numplayers.text()
        if self.avglvl.text() != "":
            self.gen.partylevel = self.avglvl.text()
        # if self.cr.text() != "":
        #     self.gen.challengerating = self.cr.text()

        if self.day.isChecked():
            self.gen.time[3] = 1
        if self.night.isChecked():
            self.gen.time[3] = -1
        if self.custom.isChecked():
            pass

        self.gen.freqadjust = self.slider.value()


if __name__ == '__main__':

    APP = QApplication(sys.argv)
    ex = DndEncGenGUI()
    sys.exit(APP.exec_())
