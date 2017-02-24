import sys
from PyQt4 import QtCore, QtGui, uic
from alertTimer import *
from webbrowser import open

class timerSetup(QtGui.QDialog):
    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)
        QtGui.QDialog.__init__(self)
        self.ui = uic.loadUi('qtTimerSetup.ui')
        self.ui.show()
        #Buttons
        self.connect(self.ui.pushButtonStart, QtCore.SIGNAL("clicked()"), self.start)
        self.connect(self.ui.pushButtonReadMe, QtCore.SIGNAL("clicked()"), self.readme)
        sys.exit(self.app.exec_())

    def readme(self):
        open("readme.html")

    def start(self):
        totaltime = self.ui.timeEdit2.time().hour() * 3600
        totaltime = totaltime + self.ui.timeEdit2.time().minute() * 60
        totaltime = totaltime + self.ui.timeEdit2.time().second()
        if totaltime <= 0:
            QtGui.QMessageBox.critical(self, "Time Error", "Totaltime must be greater than zero!", QtGui.QMessageBox.Ok)
            return None


        timePunishment = self.ui.timeEdit.time().hour() * 3600
        timePunishment = timePunishment + self.ui.timeEdit.time().minute() * 60
        timePunishment = timePunishment + self.ui.timeEdit.time().second()


        password = self.ui.lineEdit.text()
        if len(password) > 17:
            QtGui.QMessageBox.critical(self, "Password Lenght Error", "Password lenght may only be 17 digits!", QtGui.QMessageBox.Ok)
            return None
        try:
            password = int(password)
        except ValueError:
            QtGui.QMessageBox.critical(self, "Format Error", "Password may only contain digits \nand must at least have one digit!", QtGui.QMessageBox.Ok)
            return None

        if timePunishment > totaltime:
            choice = QtGui.QMessageBox.warning(self, "Warning", "Timepunishment is greater than Totaltime.\nProceed?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if choice == QtGui.QMessageBox.No:
                return None

        self.ui.close()
        self.startTimer(totaltime, timePunishment, password)

    def startTimer(self, totalTime, timePunishment, password):
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        #app = QtGui.QApplication(sys.argv)
        self.ui = QtGui.QMainWindow()
        self.ui.setWindowTitle('AlertTimer')
        l = ActiveLabel()
        l.setAlignment(QtCore.Qt.AlignCenter)
        alterTimer = Timer(l, totalTime, timePunishment, password)

        def on_click(ev):
            if ev.button() == QtCore.Qt.LeftButton:
                alterTimer.start()

        def on_key(ev):
            if ev.text() in digits:
                alterTimer.updateInput(ev.text())
            if ev.key() == QtCore.Qt.Key_Backspace:
                alterTimer.deleteInput()
            if ev.text() == "-":
                alterTimer.deleteInput()
            if ev.key() == QtCore.Qt.Key_Return:
                alterTimer.checkPassword()
            if ev.key() == QtCore.Qt.Key_Enter:
                alterTimer.checkPassword()
            if ev.key() == QtCore.Qt.Key_Escape:
                sys.exit(0)
            if ev.key() == QtCore.Qt.Key_Space:
                alterTimer.start()

        l.clicked.connect(on_click)
        l.keypress.connect(on_key)
        self.ui.setCentralWidget(l)
        self.ui.showFullScreen()

if __name__ == "__main__":
    timerSetup = timerSetup()






