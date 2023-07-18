from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import QTimer

import time
import numpy as np
from functools import partial
import random

import serial
from df1.models.df1_serial_client import Df1SerialClient

Form, Window = uic.loadUiType("parcing.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
errorWindow = QMessageBox()

client = None
timer = QTimer()
values_array = []

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
            time.sleep(1)
            print("try-----------------------------------------------------------------------------")
            connect_to_plc()
        except KeyboardInterrupt:
            app.quit()  # Exit the application if interrupted by the user

def on_close():
    if client is not None:
        client.close()
        timer.stop()  # Stop the timer
    app.quit()

def on_text_changed():
    global values_array
    try:
        interim = form.textEdit.toPlainText()
        interim_int = int(interim)
        print(interim_int)

        #values_list = [i for i in range(interim_int)]
        values_list = [random.randint(0, 1000) for _ in range(300)]
        # values_list = client.read_integer(file_table=interim_int, start=0, total_int=300)
        values_array = list(map(int, values_list))

        try:
            for i in range(300):
                setValues = "form.label_" + str(i) + ".setText(str(values_array[" + str(i) + "]))"
                eval(setValues)
        except IndexError:
            print('IndexError')
    except ValueError:
        print('ValueError')

def reset_values():
    for i in range(300):
        text = "NO DATA"
        setToNoData = "form.label_" + str(i) + ".setText(text)"
        eval(setToNoData)

        labels_chang = "form.label_" + str(i) + ".setStyleSheet"
        eval(labels_chang)("background-color: white; border: 1px solid black;")

def searching_value():
    from_vl = form.textEdit_2.toPlainText()
    from_vl_int = int(from_vl)
    print(from_vl_int)

    to_vl = form.textEdit_3.toPlainText()
    to_vl_int = int(to_vl)
    print(to_vl_int)

    consecutive_numbers = list(range(from_vl_int, to_vl_int + 1))
    consecutive_numbers_array = np.array(consecutive_numbers)
    print(consecutive_numbers_array)
    print(values_array)

    indices = [i for i, element in enumerate(values_array) if element in consecutive_numbers_array]

    if indices:
        # Display the indexes where elements from array2 are found in array1
        print("Indexes where elements from array2 are found in array1:", indices, type(indices))
        indices_array = np.array(indices)
        print(indices_array, type(indices_array))
        for i in indices_array:
            labels_chang = "form.label_" + str(i) + ".setStyleSheet"
            eval(labels_chang)("background-color: #86f582; border: 1px solid black;")
    else:
        print("No elements in array2 are present in array1")



if __name__ == '__main__':
    app.aboutToQuit.connect(on_close)

    # reconnect_to_plc()  # Start the initial connection process
    # timer.timeout.connect(on_text_changed)

    form.pushButton.clicked.connect(on_text_changed)
    form.pushButton_2.clicked.connect(reset_values)
    form.pushButton_3.clicked.connect(searching_value)

    app.exec()