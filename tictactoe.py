from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        MainWindow.setMinimumSize(QtCore.QSize(400, 500))
        MainWindow.setMaximumSize(QtCore.QSize(400, 500))

        font = QtGui.QFont()
        font.setFamily("OpenSymbol")
        font.setPointSize(36)
        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = QtWidgets.QPushButton(self.gridLayoutWidget)
                button.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
                button.setMinimumSize(QtCore.QSize(100, 100))
                button.setText("")
                button.setObjectName(f"pushButton_{i*3+j+1}")
                self.gridLayout_2.addWidget(button, i, j, 1, 1)
                button.clicked.connect(lambda _, b=button: self.clicker(b))
                row.append(button)
            self.buttons.append(row)

        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(0, 350, 411, 31))
        font.setPointSize(17)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.reset_game)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 310, 391, 31))
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 64))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.current_player = "X"
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def clicker(self, button):
        button.setText(self.current_player)
        button.setEnabled(False)
        if self.check_winner():
            self.label.setText(f"{self.current_player} Wins!")
            self.disable_all_buttons()
        elif self.is_draw():
            self.label.setText("It's a Draw!")
        else:
            self.current_player = "O" if self.current_player == "X" else "X"
            self.label.setText(f"{self.current_player}'s Turn")

    def disable_all_buttons(self):
        for row in self.buttons:
            for button in row:
                button.setEnabled(False)

    def reset_game(self):
        for row in self.buttons:
            for button in row:
                button.setText("")
                button.setEnabled(True)
        self.current_player = "X"
        self.label.setText("X Goes First!")

    def check_winner(self):
        for row in self.buttons:
            if row[0].text() == row[1].text() == row[2].text() and row[0].text() != "":
                return True
        for col in range(3):
            if self.buttons[0][col].text() == self.buttons[1][col].text() == self.buttons[2][col].text() and self.buttons[0][col].text() != "":
                return True
        if self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text() and self.buttons[0][0].text() != "":
            return True
        if self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text() and self.buttons[0][2].text() != "":
            return True
        return False

    def is_draw(self):
        for row in self.buttons:
            for button in row:
                if button.text() == "":
                    return False
        return True

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tic-Tac-Toe"))
        self.pushButton_10.setText(_translate("MainWindow", "Start Over"))
        self.label.setText(_translate("MainWindow", "X Goes First!"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())