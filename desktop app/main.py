import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QTableWidget,
    QTableWidgetItem, QPushButton
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class EquipmentApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chemical Equipment Visualizer – Desktop App")
        self.setGeometry(200, 100, 800, 600)

        layout = QVBoxLayout()

        title = QLabel("Chemical Equipment Data (Desktop)")
        title.setStyleSheet("font-size:18px; font-weight:bold;")
        layout.addWidget(title)

        self.table = QTableWidget()
        layout.addWidget(self.table)

        self.button = QPushButton("Load Data from API")
        self.button.clicked.connect(self.load_data)
        layout.addWidget(self.button)

        self.figure = Figure(figsize=(5, 3))
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

    def load_data(self):
        url = "http://127.0.0.1:8000/api/equipment/"
        response = requests.get(url)
        data = response.json()

        self.table.setRowCount(len(data))
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Name", "Type"])

        type_count = {}

        for row, item in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(item["name"]))
            self.table.setItem(row, 1, QTableWidgetItem(item["type"]))

            type_count[item["type"]] = type_count.get(item["type"], 0) + 1

        self.draw_chart(type_count)

    def draw_chart(self, type_count):
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        types = list(type_count.keys())
        counts = list(type_count.values())

        ax.bar(types, counts)
        ax.set_title("Equipment Type Distribution")
        ax.set_xlabel("Type")
        ax.set_ylabel("Count")

        self.canvas.draw()


app = QApplication(sys.argv)
window = EquipmentApp()
window.show()
sys.exit(app.exec_())
