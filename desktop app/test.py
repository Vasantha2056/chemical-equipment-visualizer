from PyQt5.QtWidgets import QApplication, QLabel
import sys

app = QApplication(sys.argv)
label = QLabel("PyQt5 Desktop App Working 🎉")
label.show()
sys.exit(app.exec_())
