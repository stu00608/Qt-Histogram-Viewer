from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import scene
import sys

class Window(QWidget, scene.Ui_Form):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()