from PyQt6.QtCore import QTimer
import serial
from df1.models.df1_serial_client import Df1SerialClient


def setup_serial_connection(form):
    try:
        client = Df1SerialClient(plc_type='SLC 5/04 CPU', src=0x1, dst=0x3,
                                 port='COM12',
                                 baudrate=19200, parity=serial.PARITY_NONE,
                                 stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS,
                                 timeout=5)
        client.connect()
    except Exception as e:
        client.reconnect()

    def update_label_407():
        form.label_407.setText(str(client.read_integer(start=1, total_int=1)[0]))
        print("run every 1 sec...")

    def update_label_408():
        print("run every 1 sec... 2")

    timer = QTimer()
    timer.timeout.connect(update_label_407)
    timer.timeout.connect(update_label_408)
    timer.start(1000)
