#!/usr/bin/python3
""" This tool can be used to generate random encounter for
Dungeons and Dragons 5e. """


import sys
from generator import EncounterGenerator
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout,
                             QCheckBox, QApplication,
                             QLabel, QGridLayout,
                             QLineEdit, QGroupBox,
                             QSlider, QComboBox,
                             QMessageBox, QMainWindow,
                             QTabWidget, QAction,
                             qApp, QButtonGroup,
                             QTextEdit, QScrollArea,
                             QPlainTextEdit, QLayout)
from PyQt5.QtCore import (pyqtSlot, Qt, QSize)
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    """ docstring """
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        
        self.setWindowTitle('DnD Random Encounters Generator, 5e')
        self.tabwidget = TabWidget(self)
        self.setCentralWidget(self.tabwidget)

        self.quitbttn = QPushButton("Quit")
        self.quitbttn.clicked.connect(QApplication.instance().quit)
        self.show()
        
    
class TabWidget(QTabWidget):
    """ docstring """
    def __init__(self, parent):
        super(TabWidget, self).__init__()
        self.maintab = GenerateWidget(self)
        self.addTab(self.maintab, "Generate Encounters")
        self.setTabsClosable(True)
        self.show()
        
            
class GenerateWidget(QWidget):
    """ Its rough and needs to be broken down. """
    def __init__(self, parent):
        super(GenerateWidget, self).__init__()
        """ Initializes the window. """
        self.parent = parent
        self.gen = EncounterGenerator()
        self.encountercounter = 0
        
        mainlayout = QGridLayout()
        mainlayout.setAlignment(Qt.AlignTop)
        mainlayout.setColumnMinimumWidth(0, 200)
        mainlayout.setColumnMinimumWidth(1, 200)
        mainlayout.setColumnMinimumWidth(2, 200)
        
        groupleft = QGroupBox("Terrain Type")
        vboxleft = QVBoxLayout()
        buttongroupleft = QButtonGroup(self)
        buttongroupleft.setExclusive(True)
        self.arctic = QCheckBox("Arctic")
        vboxleft.addWidget(self.arctic)
        buttongroupleft.addButton(self.arctic)
        self.desert = QCheckBox("Desert")
        vboxleft.addWidget(self.desert)
        buttongroupleft.addButton(self.desert)
        self.coast = QCheckBox("Coast")
        vboxleft.addWidget(self.coast)
        buttongroupleft.addButton(self.coast)
        self.forest = QCheckBox("Forest")
        vboxleft.addWidget(self.forest)
        buttongroupleft.addButton(self.forest)
        self.grassland = QCheckBox("Grassland")
        vboxleft.addWidget(self.grassland)
        buttongroupleft.addButton(self.grassland)
        self.hill = QCheckBox("Hill")
        vboxleft.addWidget(self.hill)
        buttongroupleft.addButton(self.hill)
        self.mountain = QCheckBox("Mountain")
        vboxleft.addWidget(self.mountain)
        buttongroupleft.addButton(self.mountain)
        self.swamp = QCheckBox("Swamp")
        vboxleft.addWidget(self.swamp)
        buttongroupleft.addButton(self.swamp)
        self.underdark = QCheckBox("Underdark")
        vboxleft.addWidget(self.underdark)
        buttongroupleft.addButton(self.underdark)
        self.underwater = QCheckBox("Underwater")
        vboxleft.addWidget(self.underwater)
        buttongroupleft.addButton(self.underwater)
        self.urban = QCheckBox("Urban")
        vboxleft.addWidget(self.urban)
        groupleft.setLayout(vboxleft)
        
        groupmid = QGroupBox("Travel Type")
        vboxmid = QVBoxLayout()
        buttongroupmid = QButtonGroup(self)
        self.highway = QCheckBox("Highway")
        buttongroupmid.addButton(self.highway)
        vboxmid.addWidget(self.highway)
        self.road = QCheckBox("Road")
        buttongroupmid.addButton(self.road)
        vboxmid.addWidget(self.road)
        self.trail = QCheckBox("Trail")
        buttongroupmid.addButton(self.trail)
        vboxmid.addWidget(self.trail)
        self.wilderness = QCheckBox("Wilderness")
        buttongroupmid.addButton(self.wilderness)
        vboxmid.addWidget(self.wilderness)
        groupmid.setLayout(vboxmid)
        
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
        self.resetbttn.clicked.connect(self.on_reset_click)
        self.generatebttn = QPushButton("Generate")
        self.generatebttn.clicked.connect(self.on_generate_click)
        self.quitbttn = QPushButton("Quit")
        self.quitbttn.clicked.connect(QApplication.instance().quit)

        self.hboxrgq = QHBoxLayout()
        self.hboxrgq.addStretch(1)
        self.hboxrgq.addWidget(self.resetbttn)
        self.hboxrgq.addWidget(self.generatebttn)
        self.hboxrgq.addWidget(self.quitbttn)
        
        mainlayout.addWidget(groupleft, 0, 0)
        mainlayout.addWidget(groupmid, 0, 1)
        mainlayout.addLayout(vboxright, 0, 2)
        mainlayout.addLayout(self.slidervbox, 1, 0)
        mainlayout.addLayout(self.hboxrgq, 1, 2)
        self.setLayout(mainlayout)
        self.show()
        self.on_reset_click()

    @pyqtSlot()
    def on_generate_click(self):
        """ Handles click to pass settings to the generator and create a new
        tab. """
        if self.parseParameters() != 0:
            return -1
        encounters, monsters, animals = self.gen.generateEncounter()
        self.encountercounter += 1
        newencounter = EncounterWidget(self.parent, encounters, monsters, animals)
        title = "Encounters (" + str(self.encountercounter) + ")"
        super(TabWidget, self.parent).addTab(newencounter, title)
        super(TabWidget, self.parent).setCurrentIndex(self.encountercounter)
        return 0

    @pyqtSlot()
    def on_reset_click(self):
        """ Resets all values to default startup values. """
        self.arctic.setChecked(True)
        self.desert.setChecked(False)
        self.coast.setChecked(False)
        self.forest.setChecked(False)
        self.grassland.setChecked(False)
        self.hill.setChecked(False)
        self.mountain.setChecked(False)
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
            self.day.setChecked(False)
            self.night.hide()
            self.night.setChecked(False)
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
            self.monthsdd.setCurrentIndex(0)
            self.weekslbl.hide()
            self.weeksdd.hide()
            self.weeksdd.setCurrentIndex(0)
            self.dayslbl.hide()
            self.daysdd.hide()
            self.daysdd.setCurrentIndex(0)
        return 0

    def _popupMessage(self, title, message):
        """ Wrapper for generating a popup dialog box. """
        QMessageBox.about(self, title, message)
        return 0

    def parseParameters(self):
        """ Loads the values into the generator depending on current
        selections.  """
        self.gen.reset()
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
        if self.hill.isChecked():
            self.gen.terraintype.append("Hill")
        if self.mountain.isChecked():
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


class EncounterWidget(QWidget):
    """ docstring """
    def __init__(self, parent, encounters, monsters, animals):
        super(EncounterWidget, self).__init__()
        self.parent = parent
        self.encounters = encounters
        self.monsters = monsters
        self.animals = animals
        
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
    
        label = QLabel()
        label.setText("Total Numbers of Encounters by Type:")
        # scroll = QScrollArea()
        # scroll.setWidget(textarea)
        self.layout.addWidget(label)
        self.genOutput()
        
        self.closebttn = QPushButton("Close")
        self.closebttn.clicked.connect(self.on_close_click)
        self.layout.addWidget(self.closebttn)

        self.setLayout(self.layout)
        self.show()
        
    def genOutput(self):
        for key, value in self.encounters.items():
            hbox = QHBoxLayout()
            typelbl = QLabel()
            typelbl.setText(key)
            countlbl = QLabel()
            countlbl.setText(str(value))
            hbox.addWidget(typelbl)
            hbox.addWidget(countlbl)
            self.layout.addLayout(hbox)
            
    @pyqtSlot()
    def on_close_click(self):
        super(TabWidget, self.parent).removeTab(super(TabWidget, self.parent).currentIndex())

        
class DetailsWidget(QWidget):
    """ docstring """
    def __init__():
        pass


        
if __name__ == '__main__':
    
    APP = QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(APP.exec_())
