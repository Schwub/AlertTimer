
normal_style = """
 QLabel {
   color: white;
   background-color: black;
   font-size: 180pt;
   font-family: "DejaVu Sans Mono";
   font-weight: bold;
}"""

warning_style = """
 QLabel {
   color: red;
   background-color: black;
   font-size: 180pt;
   font-family: "DejaVu Sans Mono";
   font-weight: bold;
}"""

negative_style = """
 QLabel {
   color: black;
   background-color: red;
   font-size: 180pt;
   font-family: "DejaVu Sans Mono";
   font-weight: bold;
}"""

standby_style = """
 QLabel {
   color: green;
   background-color: black;
   font-size: 100pt;
   font-family: "DejaVu Sans Mono";
   font-weight: bold;
}"""

import sys
from PyQt4 import QtCore, QtGui


class ActiveLabel(QtGui.QLabel):
    clicked = QtCore.pyqtSignal(QtGui.QMouseEvent)
    keypress= QtCore.pyqtSignal(QtGui.QKeyEvent)

    def __init__(self, *args):
        super(ActiveLabel, self).__init__(*args)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

    def mouseReleaseEvent(self, ev):
        self.clicked.emit(ev)

    def keyReleaseEvent(self, ev):
        self.keypress.emit(ev)


class FSM(object):
    def __init__(self, label, totalTime):
        self.label = label
        self.totalTime = totalTime
        self.remainingTime = totalTime
        self.current_state = self.standingby
        self.current_state()
        self.timer = QtCore.QTimer(interval=1000) # miliseconds
        self.timer.timeout.connect(self.on_every_second)

    # Event methods:
    def on_every_second(self):
        self.remainingTime -= 1
        self.current_state()

    # Methods:
    def start(self):
        if self.current_state not in [self.standingby, self.stopped]:
            return
        self.remainingTime = self.totalTime
        self.current_state = self.countdown
        self.current_state()
        self.timer.start()

    def stop(self):
        if self.current_state in [self.standingby, self.stopped]:
            return
        self.timer.stop()
        self.current_state = self.stopped
        self.current_state()

    def standby(self):
        self.timer.stop()
        self.current_state = self.standingby
        self.current_state()


    # States:
    def standingby(self):
        self.label.setStyleSheet(standby_style)
        self.label.setText("TEDxSkopje")

    def stopped(self):
        self.label.setStyleSheet(normal_style)
        self.label.setText("00:00")

    def countdown(self):
        if self.remainingTime < 0:
            self.label.setStyleSheet(negative_style)
            self.label.setText("%02d:%02d" % divmod(abs(self.remainingTime), 60))
        elif self.remainingTime < 60:
            self.label.setStyleSheet(warning_style)
            self.label.setText("%02d:%02d" % divmod(self.remainingTime, 60))
            self.label.setText("lol")
        else:
            self.label.setStyleSheet(normal_style)
            self.label.setText("%02d:%02d" % divmod(self.remainingTime, 60))


def main(argv):
    try:
        totalTime = int(argv[1]) * 60
    except IndexError:
        totalTime = 1 * 60

    app = QtGui.QApplication(argv)
    mw = QtGui.QMainWindow()
    mw.setWindowTitle('Одбројување за TEDxSkopje')
    l = ActiveLabel()
    l.setAlignment(QtCore.Qt.AlignCenter)
    fsm = FSM(l, totalTime)
    def on_click(ev):
        if ev.button() == QtCore.Qt.LeftButton:
            fsm.start()
        elif ev.button() == QtCore.Qt.RightButton:
            fsm.stop()
    def on_key(ev):
        if ev.key() == QtCore.Qt.Key_Escape:
            fsm.standby()
    l.clicked.connect(on_click)
    l.keypress.connect(on_key)
    mw.setCentralWidget(l)
    mw.showFullScreen()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main(sys.argv))

# TODO:
#  - configurable totalTime
#


