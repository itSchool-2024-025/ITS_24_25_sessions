from gui import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
import sys

class Custom_MainWindow(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.number7.clicked.connect(self.method_for_button_no_7)
        self.Sum.clicked.connect(self.method_for_button_sum)
        self.delete_button.clicked.connect(self.method_for_button_delete)

    def method_for_button_no_7(self):
        # Get the text value from the Digital Output (QLineEdit)
        text_number = str(self.lineEdit.text())
        if text_number == "0":
            text_number = "7"
        else:
            text_number += "7"
        self.lineEdit.setText(text_number)

    def method_for_button_sum(self):
        print("Sum")

    def method_for_button_delete(self):
        self.lineEdit.setText("0")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Custom_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
