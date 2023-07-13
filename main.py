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

if __name__ == '__main__':
    switching_tabs.switch_logic(form)
    switching_btns.switch_logic(form)
    labels_toggling.switch_logic(form)
    # client = connection.setup_serial_connection(form)
    try:
        client = Df1SerialClient(plc_type='SLC 5/04 CPU', src=0x1, dst=0x3,
                                 port='COM12',
                                 baudrate=19200, parity=serial.PARITY_NONE,
                                 stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS,
                                 timeout=5)
        client.connect()
    except Exception as e:
        client.reconnect()
        print("reconnecting to plc -/-/-")

    def update_label_407():
        form.label_407.setText(str(client.read_integer(start=1, total_int=1)[0]))

    timer = QTimer()
    timer.timeout.connect(update_label_407)
    timer.start(1000)

    def on_close():
        client.close()
    app.aboutToQuit.connect(on_close)

window.showFullScreen()
app.exec()