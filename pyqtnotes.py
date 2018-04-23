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
        grid.addWidget(label1, 1, 1, 1, 1) # row, col, row_span, col_span

        button1 = QPushButton("button1", self)
        grid.addWidget(button1, 1, 2, 1, 1)

        lcd = QLCDNumber(self)
        grid.addWidget(lcd, 2, 1, 1, 2)

        slider = QSlider(Qt.Horizontal, self)
        slider.setValue(50)
        grid.addWidget(slider, 3, 1, 1, 2)

        # set up signals and slots
        button1.clicked.connect(lambda: label1.setText("Clicked!"))

        # draw the app
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Window() # create an instance of the window class
    sys.exit(app.exec_())