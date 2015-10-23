#!/usr/bin/env python3
# coding: utf-8

import sys
import requests
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from sandpit_ui import *


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        response = requests.get(
            "http://icons.wxug.com/i/c/k/nt_partlycloudy.gif", # The image link we got earlier
            proxies={"http": "10.1.8.90:8080"},
            stream=True
        )

        data = response.raw.read()
        pixmap = QPixmap().fromImage(QImage().fromData(data))
        self.ui.lblImage.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
