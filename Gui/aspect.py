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

from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class Aspect:
    """Trata a estilização da interface"""

    # Recebe o objeto pai
    def __init__(self, parent: object):
        self._parent = parent

    # Remove bordas e background do objeto
    def removeCentralWidget(self):
        self._parent.setWindowFlags(Qt.FramelessWindowHint)
        self._parent.setAttribute(Qt.WA_TranslucentBackground)

    # Define uma sombra ao widget
    def setDropShadow(self, widget: object):
        self._parent.shadow = QGraphicsDropShadowEffect(self._parent)
        self._parent.shadow.setBlurRadius(17)
        self._parent.shadow.setXOffset(0)
        self._parent.shadow.setYOffset(0)
        self._parent.shadow.setColor(QColor(0, 0, 0, 150))
        widget.setGraphicsEffect(self._parent.shadow)

    def setPosition(self, event):
        """Recebe a posição do mouse. Usado para complementar
        a função que movimenta a janela"""

        self._parent.dragPos = event.globalPos()

    # Move a janela
    def moveWindow(self, event):

        # # Restaura o tamanho da janela quando maximizada
        # if MAXIMIZED:
        #     self.maximizeRestore()

        if event.buttons() == Qt.LeftButton:
            self._parent.move(self._parent.pos() + event.globalPos() - self._parent.dragPos)
            self._parent.dragPos = event.globalPos()
            event.accept()