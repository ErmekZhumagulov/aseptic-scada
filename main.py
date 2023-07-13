from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMessageBox
from codes import labels_toggling
from PyQt6.QtCore import QTimer
import random

import serial
from df1.models.df1_serial_client import Df1SerialClient

Form, Window = uic.loadUiType("ui.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
errorWindow = QMessageBox()

#-----------------------------------------------------------------------------------------------------------------------

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

#-----------------------------------------------------------------------------------------------------------------------

# switching buttons logic
def on_pushButton_clicked_7():
    # Custom slot implementation
    form.tabWidget.setCurrentIndex(1)
form.pushButton_7.clicked.connect(on_pushButton_clicked_7)
def on_pushButton_clicked_8():
    # Custom slot implementation
    form.tabWidget.setCurrentIndex(1)
form.pushButton_8.clicked.connect(on_pushButton_clicked_8)
def on_pushButton_clicked_9():
    # Custom slot implementation
    form.tabWidget.setCurrentIndex(1)
form.pushButton_9.clicked.connect(on_pushButton_clicked_9)
def on_pushButton_clicked_10():
    # Custom slot implementation
    form.tabWidget.setCurrentIndex(1)
form.pushButton_10.clicked.connect(on_pushButton_clicked_10)
def on_pushButton_clicked_11():
    # Custom slot implementation
    form.tabWidget.setCurrentIndex(3)
form.pushButton_11.clicked.connect(on_pushButton_clicked_11)
def on_pushButton_clicked_12():
    # Custom slot implementation
    form.tabWidget.setCurrentIndex(4)
form.pushButton_12.clicked.connect(on_pushButton_clicked_12)
def on_pushButton_clicked_13():
    # Custom slot implementation
    form.tabWidget.setCurrentIndex(1)
form.pushButton_13.clicked.connect(on_pushButton_clicked_13)
def on_pushButton_clicked_24():
    # Custom slot implementation
    form.tabWidget.setCurrentIndex(5)
form.pushButton_24.clicked.connect(on_pushButton_clicked_24)
def on_pushButton_clicked_156():
    # Custom slot implementation
    form.tabWidget.setCurrentIndex(6)
form.pushButton_156.clicked.connect(on_pushButton_clicked_156)

#-----------------------------------------------------------------------------------------------------------------------

#set texts to labels
def update_labels(labels):
    for label in labels:
        random_number = random.uniform(0.00, 100.00)
        random_string = "{:.2f}".format(random_number)
        label.setText(random_string)

#-----------------------------------------------------------------------------------------------------------------------

# switch light randomizer
def generate_random_number():
    array = [
        form.pushButton_25, form.pushButton_26, form.pushButton_27, form.pushButton_28, form.pushButton_29,
        form.pushButton_30, form.pushButton_31, form.pushButton_32, form.pushButton_33, form.pushButton_34,
        form.pushButton_35, form.pushButton_36, form.pushButton_37, form.pushButton_38, form.pushButton_39,
        form.pushButton_40, form.pushButton_41, form.pushButton_42, form.pushButton_43, form.pushButton_44,
        form.pushButton_45, form.pushButton_46, form.pushButton_47, form.pushButton_48, form.pushButton_49,
        form.pushButton_50, form.pushButton_51, form.pushButton_52, form.pushButton_53, form.pushButton_54,
        form.pushButton_55, form.pushButton_56
    ]
    for button in array:
        random_number = random.randint(0, 1)
        value = random_number
        button.setProperty("value", value)
        button.style().polish(button)

        # Apply the style sheet to change the background color based on the value
        button.setStyleSheet('''
            QPushButton {
                /* Default background color */
                background-color: red; /* or any other default color */
                border: 1px solid black
            }
            QPushButton[value="0"] {
                /* Background color when value is 0 */
                background-color: #d6d6d6;
                border: 1px solid black
            }
            QPushButton[value="1"] {
                /* Background color when value is 1 */
                background-color: green;
                border: 1px solid black
            }
        ''')

# Create a QTimer to trigger the generation of random numbers every 2 seconds
timer = QTimer()
timer.timeout.connect(generate_random_number)
# Connect the timeout signal of the timer to a lambda function that calls update_labels with the array of labels
timer.timeout.connect(lambda: update_labels([form.label_368,form.label_374, form.label_380, form.label_85, form.label_86, form.label_87, form.label_67, form.label_68, form.label_69, form.label_70, form.label_71, form.label_72]))
timer.start(1000)

#-----------------------------------------------------------------------------------------------------------------------

# labels toggling logic
# need to add label you want to toggle
label_toggler = labels_toggling.LabelToggler([form.label_249, form.label_250, form.label_243, form.label_242, form.label_240, form.label_241, form.label_244, form.label_245, form.label_271, form.label_272, form.label_273, form.label_274, form.label_301, form.label_262, form.label_263, form.label_265, form.label_266, form.label_267, form.label_270, form.label_276, form.label_277, form.label_278, form.label_279, form.label_291, form.label_292, form.label_294, form.label_295, form.label_275, form.label_289, form.label_290, form.label_280, form.label_285, form.label_286, form.label_288, form.label_287, form.label_281, form.label_282, form.label_283, form.label_284, form.label_300, form.label_297, form.label_298, form.label_310, form.label_299, form.label_304, form.label_309, form.label_305, form.label_306, form.label_311, form.label_320, form.label_318, form.label_317, form.label_322, form.label_321, form.label_315, form.label_324, form.label_323, form.label_319])
# Connect the button click event to the toggle_label_visibility slot
form.pushButton.clicked.connect(label_toggler.toggle_label_visibility)

#-----------------------------------------------------------------------------------------------------------------------

client = Df1SerialClient(plc_type='SLC 5/04 CPU', src=0x1, dst=0x3,
                         port='COM12',
                         baudrate=19200, parity=serial.PARITY_NONE,
                         stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS,
                         timeout=5)
client.connect()

def update_label_407():
    form.label_407.setText(str(client.read_integer(start=1, total_int=1)[0]))
    print("run every 1 sec...")
def update_label_408():
    print("run every 1 sec... 2")

timer = QTimer()
timer.timeout.connect(update_label_407)
timer.timeout.connect(update_label_408)
timer.start(1000)

#-----------------------------------------------------------------------------------------------------------------------

def on_close():
    print("Closing the application...")
    client.close()
app.aboutToQuit.connect(on_close)

#-----------------------------------------------------------------------------------------------------------------------

window.showFullScreen()
app.exec()