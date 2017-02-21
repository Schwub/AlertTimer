standby_style = """
 QLabel {
   color: green;
   background-color: black;
   font-size: 180pt;
   font-family: "DejaVu Sans Mono";
   font-weight: bold;
}"""

normal_style = """
 QLabel {
   color: black;
   background-color: red;
   font-size: 80pt;
   font-family: "DejaVu Sans Mono";
   font-weight: bold;
}"""

wrong_answer_style = """
 QLabel {
   color: red;
   background-color: Black;
   font-size: 100pt;
   font-family: "DejaVu Sans Mono";
   font-weight: bold;
}"""

wrong_answer_style2 = """
 QLabel {
   color: Black;
   background-color: Black;
   font-size: 100pt;
   font-family: "DejaVu Sans Mono";
   font-weight: bold;
}"""

right_answer_style = """
 QLabel {
   color: white;
   background-color: green;
   font-size: 80pt;
   font-family: "DejaVu Sans Mono";
   font-weight: bold;
}"""

time_out_style = """
 QLabel {
   color: Black;
   background-color: Red;
   font-size: 80pt;
   font-family: "DejaVu Sans Mono";
   font-weight: bold;
}"""

import sys
from PyQt4 import QtCore, QtGui
import time


class ActiveLabel(QtGui.QLabel):
    clicked = QtCore.pyqtSignal(QtGui.QMouseEvent)
    keypress = QtCore.pyqtSignal(QtGui.QKeyEvent)

    def __init__(self, *args):
        super(ActiveLabel, self).__init__(*args)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

    def mouseReleaseEvent(self, ev):
        self.clicked.emit(ev)

    def keyReleaseEvent(self, ev):
        self.keypress.emit(ev)


class Timer:
    def __init__(self, label, totalTime, password=1234):
        self.label = label
        self.totalTime = totalTime
        self.remainingTime = totalTime
        self.password = password
        self.input = "*" * len(str(password))
        self.emptyInput = self.input
        self.currentState = self.standby
        self.currentState()
        self.timer = QtCore.QTimer(interval=10)  # miliseconds
        self.timer.timeout.connect(self.on_every_second)
        self.wrongAnswer = False
        self.wrongCounter = 15

    def on_every_second(self):
        self.remainingTime -= 1/100
        if self.remainingTime <= 0:
            self.currentState = self.timeout()
            self.timer.stop()
        else:
            if self.wrongAnswer == True:
                if self.wrongCounter <= 0:
                    self.wrongCounter = 15
                    self.wrongAnswer = False
                    self.currentState = self.countdown
                elif int(self.wrongCounter) % 2 == 1:
                    self.currentState = self.wrong_answer_negativ
                    self.wrongCounter -= 1 / 20
                else:
                    self.currentState = self.wrong_answer
                    self.wrongCounter -= 1 / 20
            self.currentState()

    # Key-Press-Methods
    def start(self):
        self.remainingTime = self.totalTime
        self.currentState = self.countdown
        self.input = "*" * len(str(self.password))
        self.currentState()
        self.timer.start()

    def updateInput(self, pressedKey):
        if self.input == self.emptyInput:
            self.input = pressedKey
        else:
            self.input = self.input + pressedKey

    def deleteInput(self):
        if self.input != self.emptyInput:
            self.input = self.input[:-1]
        if self.input is "":
            self.input = self.emptyInput


    def checkPassword(self):
        if self.input == str(self.password):
            self.currentState = self.right_answer()
            self.timer.stop()
        else:
            self.wrongAnswer = True
            self.currentState = self.wrong_answer



    # States
    def standby(self):
        self.label.setStyleSheet(standby_style)
        self.label.setText("%02d:%02d" % divmod(abs(self.remainingTime), 60))

    def countdown(self):
        self.label.setStyleSheet(normal_style)
        self.label.setText("%02d:%02d" % divmod(self.remainingTime, 60) +"\n Password:\n" +self.input )

    def wrong_answer(self):
        self.label.setStyleSheet(wrong_answer_style)
        self.label.setText("Wrong password!!!")

    def wrong_answer_negativ(self):
        self.label.setStyleSheet(wrong_answer_style2)
        self.label.setText("Wrong password!!!")

    def right_answer(self):
        self.label.setStyleSheet(right_answer_style)
        self.label.setText("Right password!!!")

    def timeout(self):
        self.label.setStyleSheet(time_out_style)
        self.label.setText("Time is up,\n you lost!!!")


def main(argv):
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    totalTime = 1.5 * 60
    app = QtGui.QApplication(argv)
    mw = QtGui.QMainWindow()
    mw.setWindowTitle('AlterTimer')
    l = ActiveLabel()
    l.setAlignment(QtCore.Qt.AlignCenter)
    alterTimer = Timer(l, totalTime)

    def on_click(ev):
        if ev.button() == QtCore.Qt.LeftButton:
            alterTimer.start()
    def on_key(ev):
        if ev.text() in digits:
            alterTimer.updateInput(ev.text())
        if ev.key() == QtCore.Qt.Key_Backspace:
            alterTimer.deleteInput()
        if ev.key() == QtCore.Qt.Key_Return:
            alterTimer.checkPassword()
        if ev.key() == QtCore.Qt.Key_Enter:
            alterTimer.checkPassword()
        if ev.key() == QtCore.Qt.Key_Escape:
            sys.exit(0)

    l.clicked.connect(on_click)
    l.keypress.connect(on_key)
    mw.setCentralWidget(l)
    mw.showFullScreen()
    return app.exec_()


if __name__ == "__main__":
    sys.exit(main(sys.argv))


#Todo: -Esc Close Porgamm
#      -Blinkendes Wrong Answer
#      -Setup Tool on Start