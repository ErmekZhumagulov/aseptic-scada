from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMessageBox, QMainWindow, QLabel, QPushButton
from PyQt6.QtCore import Qt
from PyQt5.QtGui import QTransform
import labels_toggling

Form, Window = uic.loadUiType("ui.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
errorWindow = QMessageBox()

# switching tabs logic
def on_pushButton_clicked_2():
    # Custom slot implementation
    form.tabWidget.setCurrentIndex(2)
form.pushButton_2.clicked.connect(on_pushButton_clicked_2)
def on_pushButton_clicked_3():
    # Custom slot implementation
    form.tabWidget.setCurrentIndex(3)
form.pushButton_3.clicked.connect(on_pushButton_clicked_3)
def on_pushButton_clicked_4():
    # Custom slot implementation
    form.tabWidget.setCurrentIndex(4)
form.pushButton_4.clicked.connect(on_pushButton_clicked_4)

# labels toggling logic
# need to add label you want to toggle
label_toggler = labels_toggling.LabelToggler([form.label_249, form.label_250, form.label_243, form.label_242, form.label_240, form.label_241, form.label_244, form.label_245, form.label_271, form.label_272, form.label_273, form.label_274, form.label_301, form.label_262, form.label_263, form.label_265, form.label_266, form.label_267, form.label_270, form.label_276, form.label_277, form.label_278, form.label_279, form.label_291, form.label_292, form.label_294, form.label_295, form.label_275, form.label_289, form.label_290, form.label_280, form.label_285, form.label_286, form.label_288, form.label_287, form.label_281, form.label_282, form.label_283, form.label_284, form.label_300, form.label_297, form.label_298, form.label_310, form.label_299, form.label_304, form.label_309, form.label_305, form.label_306, form.label_311, form.label_320, form.label_318, form.label_317, form.label_322, form.label_321, form.label_315, form.label_324, form.label_323, form.label_319])
# Connect the button click event to the toggle_label_visibility slot
form.pushButton.clicked.connect(label_toggler.toggle_label_visibility)

window.showFullScreen()
app.exec()