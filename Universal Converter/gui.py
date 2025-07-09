from PyQt5 import Qt
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout,    QComboBox, QTextEdit, QMessageBox
)
from PyQt5.QtGui import QFont
import sys

# Import your conversion logic
from main import convert


class ConverterGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🧠 Universal Converter")
        self.setGeometry(100, 100, 600, 400)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()


        #Universal Converter
        title = QLabel("UNIVERSAL CONVERTER")  # Capitalized
        title.setFont(QFont("Arial", 22, QFont.Bold))  # Bigger + bold
        title.setStyleSheet("""
            color: #333;
            margin-bottom: 15px;
            padding: 10px;
            text-align: center;
        """)
        title.setAlignment(Qt.AlignCenter)  # 👈 Center align
        layout.addWidget(title)

        # Dropdowns
        dropdown_layout = QHBoxLayout()

        self.from_combo = QComboBox()
        self.from_combo.addItems(["text", "binary", "decimal", "hex"])

        self.to_combo = QComboBox()
        self.to_combo.addItems(["text", "binary", "decimal", "hex"])

        dropdown_layout.addWidget(QLabel("From:"))
        dropdown_layout.addWidget(self.from_combo)
        dropdown_layout.addWidget(QLabel("To:"))
        dropdown_layout.addWidget(self.to_combo)

        layout.addLayout(dropdown_layout)

        # Input Text
        self.input_box = QTextEdit()
        self.input_box.setPlaceholderText("Enter your value here...")
        layout.addWidget(QLabel("Input:"))
        layout.addWidget(self.input_box)

        # Convert Button
        self.convert_button = QPushButton("Convert")
        self.convert_button.clicked.connect(self.handle_conversion)
        self.convert_button.setStyleSheet("background-color: #4CAF50; color: white;")
        layout.addWidget(self.convert_button)

        # Output Text
        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)
        layout.addWidget(QLabel("Result:"))
        layout.addWidget(self.output_box)

        self.setLayout(layout)

    def handle_conversion(self):
        source_type = self.from_combo.currentText()
        target_type = self.to_combo.currentText()
        input_data = self.input_box.toPlainText()

        if not input_data.strip():
            QMessageBox.warning(self, "Input Error", "Please enter some data.")
            return

        result = convert(input_data, source_type, target_type)
        self.output_box.setText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConverterGUI()
    window.show()
    try:
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        print("Exited by user.")

