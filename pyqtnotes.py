import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # ser my layout
        grid = QGridLayout()
        self.setLayout(grid)
        self.setGeometry(10, 10, 300, 300) # top left x, top left y, width, height

        # make our widgets
        label1 = QLabel("label1", self) # text to display, widget to display to

        # set up signals and slots

        # draw the app
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Window() # create an instance of the window class
    sys.exit(app.exec_())