from PyQt6.QtCore import Qt, QObject, QEvent
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

class KeyPressHandler(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.KeyPress:
            print(f"Key Pressed: {event.key()}")
            if event.key() == Qt.Key.Key_A:
                print("The 'A' key was pressed!")
            return True  # Indicate the event was handled
        return super().eventFilter(obj, event)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Key Press Example")
        self.setGeometry(100, 100, 300, 200)

        # Add some widgets
        layout = QVBoxLayout()
        label = QLabel("Press any key...")
        layout.addWidget(label)
        self.setLayout(layout)

        # Install the event filter
        self.keyPressHandler = KeyPressHandler(self)
        QApplication.instance().installEventFilter(self.keyPressHandler)

if __name__ == "__main__":
    app = QApplication([])  # Create the QApplication instance
    window = MainWindow()
    window.show()
    app.exec()
