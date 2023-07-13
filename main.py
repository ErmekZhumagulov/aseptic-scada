from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMessageBox

from codes import labels_toggling
from codes import switching_tabs
from codes import switching_btns
from codes import connection

Form, Window = uic.loadUiType("ui.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
errorWindow = QMessageBox()

if __name__ == '__main__':
    client = connection.setup_serial_connection(form)

    switching_tabs.switch_logic(form)
    switching_btns.switch_logic(form)
    labels_toggling.switch_logic(form)

    def on_close():
        client.close()
    app.aboutToQuit.connect(on_close)

window.showFullScreen()
app.exec()