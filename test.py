import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import Qt, QTimer

app = QApplication(sys.argv)

lbl = QLabel('<font color = Green size=12> <b> Test</b> </font>')
lbl.setWindowFlag(Qt.SplashScreen)

lbl.show()

sys.exit(app.exec_())
