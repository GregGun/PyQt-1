import sys
from PyQt6 import QtWidgets, uic, QtWidgets

class MyDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("design-1.ui", self)

        self.__pushbutton1 = self.findChild(QtWidgets.QPushButton, "Fullscreen")
        self.__pushbutton1.clicked.connect(self.meinKlick)

    def meinKlick(self):
        print("Button geklickt!" * 1000000)


app = QtWidgets.QApplication(sys.argv)
md = MyDialog()
md.show()
sys.exit(app.exec())