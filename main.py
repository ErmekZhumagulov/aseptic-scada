from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import QTimer

from codes import labels_toggling
from codes import switching_tabs
from codes import switching_btns
from codes import connection

import serial
from df1.models.df1_serial_client import Df1SerialClient

Form, Window = uic.loadUiType("ui.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
errorWindow = QMessageBox()

client = None
timer = QTimer()

def connect_to_plc():
    global client
    try:
        client = Df1SerialClient(plc_type='SLC 5/04 CPU', src=0x1, dst=0x3,
                                 port='COM12',
                                 baudrate=19200, parity=serial.PARITY_NONE,
                                 stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS,
                                 timeout=5)
        client.connect()
        timer.start(1000)  # Start the timer for updating label_407
    except Exception as e:
        print("Error connecting to PLC:", str(e))
        client = None
        timer.stop()  # Stop the timer
        reconnect_to_plc()  # Attempt to reconnect

def reconnect_to_plc():
    global client
    while client is None:  # Keep attempting to reconnect until successful
        try:
            connect_to_plc()
        except KeyboardInterrupt:
            app.quit()  # Exit the application if interrupted by the user

def update_label_407():
    form.label_407.setText(str(client.read_integer(start=1, total_int=1)[0]))

def on_close():
    if client is not None:
        client.close()
        timer.stop()  # Stop the timer
    app.quit()

if __name__ == '__main__':
    window.showFullScreen()
    app.aboutToQuit.connect(on_close)

    switching_tabs.switch_logic(form)
    switching_btns.switch_logic(form)
    labels_toggling.switch_logic(form)

    # reconnect_to_plc()  # Start the initial connection process

    timer.timeout.connect(update_label_407)  # Connect the timer to the update_label_407 function

    app.exec()