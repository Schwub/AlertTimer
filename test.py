from PyQt4.QtGui import *
import sys


class MyWidget(QWidget):
    def keyPressEvent(self, event):
        QMessageBox.information(None, "Received Key Press Event!!",
                                "You Pressed: " + event.text())


def main():
    app = QApplication(sys.argv)
    window = MyWidget()

    window.resize(250, 250)
    window.setWindowTitle('Detect Key Press Event')
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()