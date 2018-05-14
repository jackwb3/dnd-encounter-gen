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
                             QSlider, QComboBox,
                             QMessageBox)
from PyQt5.QtCore import (pyqtSlot, Qt)


class DndEncGenGUI(QWidget):
    """ This clas is used to construct the GUI. """

    def __init__(self):
        super().__init__()
        self.initUI()

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
        self.on_click_reset()

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
        self.grassland = QCheckBox("Grassland")
        vbox.addWidget(self.grassland)
        self.hills = QCheckBox("Hill")
        vbox.addWidget(self.hills)
        self.mountains = QCheckBox("Mountain")
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
        self.numplayers = QComboBox()
        count = 1
        for num in range(1, 11):
            self.numplayers.addItem(str(count))
            count = count + 1
        hbox1.addWidget(numplayerslbl)
        hbox1.addWidget(self.numplayers)
        hbox2 = QHBoxLayout()
        avglvllbl = QLabel("Average Level of Players")
        self.avglvl = QComboBox()
        count = 1
        for num in range(1, 21):
            self.avglvl.addItem(str(count))
            count = count + 1
        hbox2.addWidget(avglvllbl)
        hbox2.addWidget(self.avglvl)
        vboxtop.addLayout(hbox1)
        vboxtop.addLayout(hbox2)
        gboxtop.setLayout(vboxtop)

        gboxbottom = QGroupBox("Time Parameters")
        vboxbottom = QVBoxLayout()
        self.day = QCheckBox("Single Day (daylight hours)")
        self.night = QCheckBox("Single Night (nitghtime hours)")
        self.custom = QCheckBox("Custom Time Range")
        self.custom.stateChanged.connect(self._toggleTimeInput)

        hboxcustomtime = QHBoxLayout()
        vbox1 = QVBoxLayout()
        self.monthslbl = QLabel()
        self.monthslbl.setText("Months")
        self.monthsdd = QComboBox()
        count = 0
        for num in range(0, 13):
            self.monthsdd.addItem(str(count))
            count = count + 1
        vbox1.addWidget(self.monthslbl)
        vbox1.addWidget(self.monthsdd)
        vbox2 = QVBoxLayout()
        self.weekslbl = QLabel()
        self.weekslbl.setText("Weeks")
        self.weeksdd = QComboBox()
        count = 0
        for num in range(0, 4):
            self.weeksdd.addItem(str(count))
            count = count + 1
        vbox2.addWidget(self.weekslbl)
        vbox2.addWidget(self.weeksdd)
        vbox3 = QVBoxLayout()
        self.dayslbl = QLabel()
        self.dayslbl.setText("Days")
        self.daysdd = QComboBox()
        count = 0
        for num in range(0, 7):
            self.daysdd.addItem(str(count))
            count = count + 1
        vbox3.addWidget(self.dayslbl)
        vbox3.addWidget(self.daysdd)
        hboxcustomtime.addLayout(vbox1)
        hboxcustomtime.addLayout(vbox2)
        hboxcustomtime.addLayout(vbox3)
        self.monthslbl.hide()
        self.monthsdd.hide()
        self.weekslbl.hide()
        self.weeksdd.hide()
        self.dayslbl.hide()
        self.daysdd.hide()

        vboxbottom.addWidget(self.day)
        vboxbottom.addWidget(self.night)
        vboxbottom.addWidget(self.custom)
        vboxbottom.addLayout(hboxcustomtime)
        gboxbottom.setLayout(vboxbottom)

        vboxright.addWidget(gboxtop)
        vboxright.addWidget(gboxbottom)
        return vboxright

    def _createBottomRow(self):
        """ This generated the bottom row of options and buttons. """
        self.slidervbox = QVBoxLayout()
        sliderlbl = QLabel()
        sliderlbl.setText("Encounter Frequency Adjustment")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(1)
        self.slider.setMaximum(199)
        self.slider.setValue(100)
        self.slidervbox.addWidget(sliderlbl)
        self.slidervbox.addWidget(self.slider)

        self.resetbttn = QPushButton("Reset")
        self.resetbttn.clicked.connect(self.on_click_reset)
        self.generatebttn = QPushButton("Generate")
        self.generatebttn.clicked.connect(self.on_click)
        self.quitbttn = QPushButton("Quit")
        self.quitbttn.clicked.connect(QApplication.instance().quit)

        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.resetbttn)
        self.hbox.addWidget(self.generatebttn)
        self.hbox.addWidget(self.quitbttn)

    @pyqtSlot()
    def on_click(self):
        """ Handles click to pass settings to the generator. """
        if self.parseParameters() != 0:
            return -1
        self.gen.generateEncounter()
        return 0

    @pyqtSlot()
    def on_click_reset(self):
        """ Resets all values to default startup values. """
        self.arctic.setChecked(True)
        self.desert.setChecked(False)
        self.coast.setChecked(False)
        self.forest.setChecked(False)
        self.grassland.setChecked(False)
        self.hills.setChecked(False)
        self.mountains.setChecked(False)
        self.swamp.setChecked(False)
        self.underdark.setChecked(False)
        self.underwater.setChecked(False)
        self.urban.setChecked(False)
        self.highway.setChecked(True)
        self.road.setChecked(False)
        self.trail.setChecked(False)
        self.wilderness.setChecked(False)
        self.day.setChecked(True)
        self.night.setChecked(False)
        self.custom.setChecked(False)
        self.slider.setValue(100)
        return 0

    def _toggleTimeInput(self):
        """ Handles dynamic display of alternate time inputs. """
        if self.custom.isChecked():
            self.day.hide()
            self.night.hide()
            self.monthslbl.show()
            self.monthsdd.show()
            self.weekslbl.show()
            self.weeksdd.show()
            self.dayslbl.show()
            self.daysdd.show()
        elif not self.custom.isChecked():
            self.day.show()
            self.night.show()
            self.monthslbl.hide()
            self.monthsdd.hide()
            self.weekslbl.hide()
            self.weeksdd.hide()
            self.dayslbl.hide()
            self.daysdd.hide()
        return 0

    def _popupMessage(self, title, message):
        """ Wrapper for generating a popup dialog box. """
        QMessageBox.about(self, title, message)
        return 0

    def parseParameters(self):
        """ Loads the values into the generator depending on current
        selections.  """
        if self.arctic.isChecked():
            self.gen.terraintype.append("Arctic")
        if self.coast.isChecked():
            self.gen.terraintype.append("Coast")
        if self.desert.isChecked():
            self.gen.terraintype.append("Desert")
        if self.forest.isChecked():
            self.gen.terraintype.append("Forest")
        if self.grassland.isChecked():
            self.gen.terraintype.append("Grassland")
        if self.hills.isChecked():
            self.gen.terraintype.append("Hill")
        if self.mountains.isChecked():
            self.gen.terraintype.append("Mountain")
        if self.swamp.isChecked():
            self.gen.terraintype.append("Swamp")
        if self.underdark.isChecked():
            self.gen.terraintype.append("Underdark")
        if self.underwater.isChecked():
            self.gen.terraintype.append("Underwater")
        if self.urban.isChecked():
            self.gen.terraintype.append("Urban")

        if self.highway.isChecked():
            self.gen.traveltype.append("Highway")
        if self.road.isChecked():
            self.gen.traveltype.append("Road")
        if self.trail.isChecked():
            self.gen.traveltype.append("Trail")
        if self.wilderness.isChecked():
            self.gen.traveltype.append("Wilderness")
        # if self.river.isChecked():
        #     self.gen.traveltype.append("River")
        # if self.sea.isChecked():
        #     self.gen.traveltype.append("Sea")

        if self.numplayers.currentText() != "":
            self.gen.partysize = self.numplayers.currentText()
        if self.avglvl.currentText() != "":
            self.gen.partylevel = self.avglvl.currentText()

        if self.day.isChecked():
            self.gen.time[3] = 1
        if self.night.isChecked():
            self.gen.time[4] = 1
        if self.custom.isChecked():
            self.gen.time[0] = int(self.monthsdd.currentText())
            self.gen.time[1] = int(self.weeksdd.currentText())
            self.gen.time[2] = int(self.daysdd.currentText())
            count = self.gen.time[0] + self.gen.time[1] + self.gen.time[2]
            if count < 1:
                self._popupMessage("Custom Time Error",
                                   "A custom time must be greater than zero.")
                return -1
                
        self.gen.freqadjust = self.slider.value()
        return 0


if __name__ == '__main__':

    APP = QApplication(sys.argv)
    ex = DndEncGenGUI()
    sys.exit(APP.exec_())
