import sys
import src.vsArray as Array

from PyQt5.QtWidgets import (QWidget, QLabel, QComboBox, QGridLayout, QFrame, QSplitter, QMainWindow,
                             QApplication, QVBoxLayout, QHBoxLayout, QGraphicsScene, QGraphicsView, QAction,
                             qApp)
from PyQt5.QtGui import (QPainter, QColor, QFont, QIcon)
from PyQt5.QtCore import (Qt, QPoint, QRect)


class Gui(QMainWindow):
    def __init__(self):
        super().__init__()

        self.guiX = 100
        self.guiY = 100
        self.guiWidth = 1000
        self.guiHeight = 600
        self.guiMargins = 50

        self._initUI()

    def _initUI(self):
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self._setArrProps()

        self.setGeometry(self.guiX, self.guiY, Array.VSArray.props['totalWidth'], Array.VSArray.props['totalHeight'])
        self.setWindowTitle('Visual Structs')
        self.show()

    def _longestStr(self, data):
        i = 0
        longest = 0
        while i < data.__len__():
            if longest < data[i].__len__():
                longest = data[i].__len__()
            i += 1

        return longest

    def _setArrProps(self):
        Array.VSArray.props['numElems'] = len(Array.VSArray.data)
        Array.VSArray.props['textMargins'] = int(Array.VSArray.props['fontSize'] * 0.5)
        Array.VSArray.props['elemWidth'] = (((Array.VSArray.props['fontSize'] * 0.85)
                                             * self._longestStr(Array.VSArray.data))
                                            + (Array.VSArray.props['textMargins'] * 10))
        Array.VSArray.props['elemHeight'] = Array.VSArray.props['fontSize'] * 2
        Array.VSArray.props['totalHeight'] = (self.guiMargins * 2) + (Array.VSArray.props['elemHeight']
                                                                      * Array.VSArray.props['numElems'])
        Array.VSArray.props['totalWidth'] = (self.guiMargins * 2) + Array.VSArray.props['elemWidth']

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self._drawArray(qp)
        qp.end()

    def _drawArray(self, qp):
        qp.setFont(QFont(Array.VSArray.props['fontFamily'], Array.VSArray.props['fontSize']))
        elemWidth = Array.VSArray.props['elemWidth']
        elemHeight = Array.VSArray.props['elemHeight']
        margins = self.guiMargins

        def _drawArrElem(x, y, w, h, index, data):
            qp.setPen(QColor(0, 0, 0))
            qp.setBrush(QColor(150, 250, 250))
            qp.drawRect(x, y, w, h)
            margins = Array.VSArray.props['textMargins']
            padding = Array.VSArray.props['fontSize']
            qp.drawText(x + margins, y + margins + (elemHeight / 2), str(index))
            qp.drawLine(x + margins + (padding * 2), y, x + margins + (padding * 2),
                        y + margins + elemHeight)
            qp.drawText(x + margins + padding + (Array.VSArray.props['fontSize'] * 2),
                        y + margins + (elemHeight / 2), str(data))

        i = 0
        while i < Array.VSArray.props['numElems']:
            offset = i * elemHeight
            _drawArrElem(margins, margins + offset, elemWidth, elemHeight, i, Array.VSArray.data[i])
            i += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Gui()
    sys.exit(app.exec_())
