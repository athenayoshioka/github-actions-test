"""Module defining the TestWindow class."""
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt


class TestWindow(QMainWindow):
    """A simple test window class.

	Example:
		window = TestWindow()
		window.show()
    """

    def __init__(self) -> None:
        super().__init__()
        self.init_ui()

    def init_ui(self) -> None:
        """Initialize the user interface."""
        self.setWindowTitle("Test Window")
        self.setGeometry(100, 100, 400, 300)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Add a label
        label = QLabel("Welcome to TestWindow!")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
