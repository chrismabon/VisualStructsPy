import sys

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

        self.arrayData = [
            'Donec non justo auctor, efficitur augue sit amet, semper dolor.',
            'Maecenas in fermentum dolor. Vestibulum porttitor volutpat odio, aliquam suscipit erat volutpat vel. ',
            'Nulla ac tellus lacus.',
            'Morbi euismod mi lorem, non placerat tellus iaculis et.',
            'Ut in feugiat nisl, in fringilla leo.',
            'In hendrerit blandit velit vitae ullamcorper.',
            'Mauris varius quam vitae odio sodales, non faucibus arcu mattis.',
            'Nullam a pretium ex, in hendrerit nulla.',
            'Donec fermentum purus eget magna fermentum blandit.',
            'Vestibulum mollis tortor consectetur diam commodo, sagittis gravida diam laoreet.',
            'Nulla id neque vel diam vestibulum convallis id a felis.',
            'Quisque ac eros at magna mollis suscipit in vitae turpis.',
            'Duis sodales mattis scelerisque.',
            'Phasellus lectus mi, blandit eu feugiat vitae, viverra vel orci.'
        ]
        self.arrayProps = {
            'numElems': 0,
            'elemWidth': 0,
            'elemHeight': 0,
            'totalHeight': 0,
            'totalWidth': 0,
            'textMargins': 0,
            'fontSize': 20,
            'fontFamily': 'Monospace'
        }

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

        self.setGeometry(self.guiX, self.guiY, self.arrayProps['totalWidth'], self.arrayProps['totalHeight'])
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
        self.arrayProps['numElems'] = self.arrayData.__len__()
        self.arrayProps['textMargins'] = int(self.arrayProps['fontSize'] * 0.4)
        self.arrayProps['elemWidth'] = (((self.arrayProps['fontSize'] * 0.85) * self._longestStr(self.arrayData))
                                        + (self.arrayProps['textMargins'] * 10))
        self.arrayProps['elemHeight'] = self.arrayProps['fontSize'] * 2
        self.arrayProps['totalHeight'] = (self.guiMargins * 2) + (self.arrayProps['elemHeight']
                                                                  * self.arrayProps['numElems'])
        self.arrayProps['totalWidth'] = (self.guiMargins * 2) + self.arrayProps['elemWidth']

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self._drawArray(qp)
        qp.end()

    def _drawArray(self, qp):
        qp.setFont(QFont(self.arrayProps['fontFamily'], self.arrayProps['fontSize']))
        elemWidth = self.arrayProps['elemWidth']
        elemHeight = self.arrayProps['elemHeight']
        margins = self.guiMargins

        def _drawArrElem(x, y, w, h, index, data, col=QColor(0, 0, 0)):
            col.setNamedColor('#000000')
            qp.setPen(col)
            qp.setBrush(QColor(150, 250, 250))
            qp.drawRect(x, y, w, h)
            margins = self.arrayProps['textMargins']
            padding = self.arrayProps['fontSize']
            qp.drawText(x + margins, y + margins + (elemHeight / 2), str(index))
            qp.drawLine(x + margins + (padding * 2), y, x + margins + (padding * 2),
                        y + margins + elemHeight)
            qp.drawText(x + margins + padding + (self.arrayProps['fontSize'] * 2),
                        y + margins + (elemHeight / 2), str(data))

        i = 0
        while i < self.arrayProps['numElems']:
            offset = i * elemHeight
            _drawArrElem(margins, margins + offset, elemWidth, elemHeight, i, self.arrayData[i])
            i += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Gui()
    sys.exit(app.exec_())
