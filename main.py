########################################################################
## Copyright © 2021, Ailson Araujo
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##     http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
##
## Versão: 1.0
## Data: 27/10/2021
##
## Projeto feito com Qt Designer, PyQt5.
########################################################################

import os
import sys
import Gui.resource_rc

from Gui.aspect import Aspect
from Gui.GuiMain import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

# Para problema de alto DPI e escala acima de 100%
os.environ["QT_FONT_DPI"] = "96"


class WinMain(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kargs):
        super(WinMain, self).__init__(*args, **kargs)
        self.setupUi(self)

        aspect = Aspect(self)
        aspect.removeCentralWidget()
        aspect.setDropShadow(self.frame_main)

        self.frame_move.mouseMoveEvent = aspect.moveWindow

        self.btn_close.clicked.connect(lambda: self.close())

    
    def mousePressEvent(self, event):
        self.frame_move.setCursor(QCursor(Qt.ClosedHandCursor))
        aspect = Aspect(self)
        aspect.setPosition(event)

    def mouseReleaseEvent(self, event):
        self.frame_move.setCursor(QCursor(Qt.OpenHandCursor))
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinMain()
    win.show()
    sys.exit(app.exec())