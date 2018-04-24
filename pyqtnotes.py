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
        lcd.display(50)
        grid.addWidget(lcd, 2, 1, 1, 2)

        slider = QSlider(Qt.Horizontal, self)
        slider.setValue(50)
        grid.addWidget(slider, 3, 1, 1, 2)

        combobox = QComboBox(self)
        grid.addWidget(combobox, 4, 1, 1, 1)
        combobox.addItems(["Beck", "Nathan", "Olivia"])

        checkbox = QCheckBox(self)
        grid.addWidget(checkbox, 4, 2, 1, 1)

        textline = QLineEdit(self)
        grid.addWidget(textline, 5, 1, 1, 1)

        multiline = QTextEdit(self)
        grid.addWidget(multiline, 5, 2, 1, 1)

        calender = QCalendarWidget(self)
        grid.addWidget(calender, 6, 1, 1, 1)

        # set up signals and slots
        button1.clicked.connect(lambda: label1.setText("Clicked!"))
        slider.valueChanged.connect(lcd.display)
        checkbox.stateChanged.connect(self.box_checked)
        multiline.textChanged.connect(lambda: print("Changed"))
        combobox.currentTextChanged.connect(lambda: print(combobox.currentText()))
        
    def box_checked(self):
        print("Box checked!")

        # draw the app
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Window() # create an instance of the window class
    sys.exit(app.exec_())