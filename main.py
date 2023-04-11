from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMessageBox
from selenium.common.exceptions import NoSuchElementException

Form, Window = uic.loadUiType("ui.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
errorWindow = QMessageBox()


window.showFullScreen()
app.exec()