import sys
import random
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QLabel,
    QHBoxLayout,
    QSpacerItem,
    QSizePolicy
)
from PyQt5.QtGui import QFont, QColor, QPalette, QPainter, QBrush
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QRegion


def generate_realistic_username():
    prefixes = [
        "Dark", "Epic", "Shadow", "Silent", "Golden", "Silver", "Mystic", "Cyber", "Frost", "Iron",
        "Storm", "Flame", "Night", "Crimson", "Royal", "Omega", "Phantom", "Void", "Neon", "Savage",
        "Solar", "Lunar", "Infinity", "Steel", "Turbo", "Venom", "Atomic", "Blazing", "Chaos", "Nova"
    ]
    nouns = [
        "Wolf", "Tiger", "Dragon", "Knight", "Hunter", "Falcon", "Wizard", "Ninja", "Reaper",
        "Phoenix", "Viper", "Raven", "Hawk", "Ghost", "Samurai", "Pirate", "Sniper", "Rider",
        "Predator", "Warrior", "Beast", "Fox", "Serpent", "Gladiator", "Shark", "Lion", "Demon",
        "Wraith", "Blaze", "Spider", "Scorpion", "Eagle", "Panther", "Cobra", "Slayer", "Rogue"
    ]
    suffixes = [
        "X", "99", "Pro", "360", "_YT", "_01", "_Gamer", "_Dev", "77", "King", "Master", "_Elite",
        "TheGreat", "Xx", "4Life", "5000", "_Legend", "God", "_Boss", "_OG", "V2", "Z", "88",
        "_Prime", "Alpha", "Omega", "Shadow", "Lord", "_Ace", "_Legendary", "999", "01X", "Hunter"
    ]

    # Construct a username
    username = f"{random.choice(prefixes)}{random.choice(nouns)}{random.choice(suffixes)}"
    return username


class UsernameGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Username Generator")
        self.setFixedSize(300, 166)  # Smaller window size

        # Enable rounded corners and custom shape
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Set dark grey and purple color scheme with rounded corners
        self.setStyleSheet(
            """
            QMainWindow {
                background-color: transparent;
                border-radius: 15px;
            }
            QWidget {
                background-color: #1a1a1a;
                border: none;
            }
            QLabel {
                color: white;
                font-size: 20px;
                font-weight: bold;
            }
            QPushButton {
                background-color: #6e488a;
                color: white;
                border-radius: 10px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #8a5ca3;
            }
            QPushButton#closeButton {
                background-color: #6e488a;
                color: white;
                border-radius: 10px;
                width: 30px;
                height: 30px;
                padding: 0;
                font-size: 12px;
                font-weight: bold;
            }
            QPushButton#closeButton:hover {
                background-color: #8a5ca3;
            }
            QLineEdit {
                background-color: #333333;
                color: white;
                border: 1px solid #6e488a;
                border-radius: 8px;
                padding: 10px;
                font-size: 16px;
            }
            QLineEdit:focus {
                border: 1px solid #8a5ca3;
            }
            """
        )

        # Track if window is being dragged
        self.is_dragging = False
        self.drag_position = QPoint()

        # Main layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        main_widget = QWidget(self)
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        # Close button in top right corner
        self.close_button = QPushButton("X")
        self.close_button.setObjectName("closeButton")
        self.close_button.clicked.connect(self.close)
        
        # Create a horizontal layout for the close button
        close_layout = QHBoxLayout()
        close_layout.addStretch()
        close_layout.addWidget(self.close_button)
        close_layout.setContentsMargins(10, 10, 10, 0)
        
        # Add close button layout to main layout
        layout.addLayout(close_layout)

        # Title with "K" and "M" in the same color as the buttons
        self.title = QLabel()
        self.title.setText('<span style="color:#6e488a;">K</span>ing<span style="color:#6e488a;">M</span>ethod')
        self.title.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title)

        # Spacer to push the generator section down
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Username display
        self.username_box = QLineEdit()
        self.username_box.setReadOnly(True)
        self.username_box.setFont(QFont("Arial", 14))
        layout.addWidget(self.username_box)

        # Generate and Copy buttons layout
        button_layout = QHBoxLayout()
        generate_button = QPushButton("Generate Username")
        generate_button.clicked.connect(self.generate_username)
        button_layout.addWidget(generate_button)

        copy_button = QPushButton("Copy to Clipboard")
        copy_button.clicked.connect(self.copy_to_clipboard)
        button_layout.addWidget(copy_button)

        layout.addLayout(button_layout)

        # Make the entire window draggable
        self.setMouseTracking(True)

    def paintEvent(self, event):
        """ Create rounded corners for the window """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(Qt.white))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(self.rect(), 15, 15)

    def mousePressEvent(self, event):
        """ Handle mouse press event to initiate dragging """
        if event.button() == Qt.LeftButton:
            self.is_dragging = True
            self.drag_position = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        """ Handle mouse move event to drag the window """
        if self.is_dragging:
            self.move(event.globalPos() - self.drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        """ Handle mouse release event to stop dragging """
        self.is_dragging = False
        event.accept()

    def generate_username(self):
        # Generate a realistic username
        username = generate_realistic_username()
        self.username_box.setText(username)

    def copy_to_clipboard(self):
        # Copy the username to the clipboard
        clipboard = QApplication.clipboard()
        clipboard.setText(self.username_box.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UsernameGenerator()
    window.show()
    sys.exit(app.exec_())