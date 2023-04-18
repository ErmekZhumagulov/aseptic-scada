from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMessageBox, QMainWindow, QLabel, QPushButton
from PyQt6.QtCore import Qt
import labels_toggling

Form, Window = uic.loadUiType("ui.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
errorWindow = QMessageBox()



# labels toggling logic
# need to add label you want to toggle
label_toggler = labels_toggling.LabelToggler([form.label_249, form.label_250])
# Connect the button click event to the toggle_label_visibility slot
form.pushButton.clicked.connect(label_toggler.toggle_label_visibility)

window.showFullScreen()
app.exec()