"""@package VisualStructsPy
Graphically displays data structures such as arrays, lists, and trees.

Users simply pass a list of data elements to the appropriate constructor function to instantiate and
populate a structure with that data. Note that trees have additional arguments to determine the manner
in which nodes are added.
"""

import sys
import VisualStructsPy.VSArray as VSArray
import VisualStructsPy.VSList as VSList
import VisualStructsPy.VSTree as VSTree

from PyQt5.QtWidgets import (QMainWindow, QApplication, QAction, qApp)
from PyQt5.QtGui import (QPainter, QColor, QFont, QIcon)


class Canvas(QMainWindow):
    def __init__(self):
        super().__init__()

        self.vsArray = VSArray.VSArray()
        self.vsList = VSList.VSList()
        self.vsTree = VSTree.VSTree()

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

        # self._setArrProps()
        self._setListProps()

        self.setGeometry(self.guiX, self.guiY,self.guiWidth, self.guiHeight)
        self.setWindowTitle('Visual Structs')
        self.show()

    def setGuiWidth(self, width):
        self.guiWidth = width

    def setGuiHeight(self, height):
        self.guiHeight = height

    def _longestStr(self, data):
        i = 0
        longest = 0
        while i < data.__len__():
            if longest < data[i].__len__():
                longest = data[i].__len__()
            i += 1

        return longest

    def _setArrProps(self):
        self.vsArray.props['numElems'] = len(self.vsArray.data)
        self.vsArray.props['textMargins'] = int(self.vsArray.font['fontSize'] * 0.5)
        self.vsArray.props['elemWidth'] = (((self.vsArray.font['fontSize'] * 0.85)
                                            * self._longestStr(self.vsArray.data))
                                           + (self.vsArray.props['textMargins'] * 10))
        self.vsArray.props['elemHeight'] = self.vsArray.font['fontSize'] * 2
        self.vsArray.props['totalHeight'] = (self.guiMargins * 4) + (self.vsArray.props['elemHeight']
                                                                        * self.vsArray.props['numElems'])
        self.vsArray.props['totalWidth'] = (self.guiMargins * 4) + self.vsArray.props['elemWidth']
        self.guiWidth = self.vsArray.props['totalWidth']
        self.guiHeight = self.vsArray.props['totalHeight']

    def _setListProps(self):
        self.vsList.props['numElems'] = len(self.vsList.data)
        self.vsList.props['textMargins'] = int(self.vsList.font['fontSize'] * 0.5)
        self.vsList.props['elemWidth'] = (self.vsList.font['fontSize'] * 4) + (self.vsList.props['textMargins'] * 0.5)
        self.vsList.props['elemHeight'] = self.vsList.font['fontSize'] * 4
        self.vsList.props['totalHeight'] = (self.guiMargins * 2) + ((self.vsList.props['elemHeight'] * 2)
                                                                      + self.vsList.props['elemMargin'])
        self.vsList.props['totalWidth'] = (self.guiMargins * 2) + ((self.vsList.props['elemWidth']
                                                                      + (self.vsList.props['elemMargin'] * 2)
                                                                    + (self.vsList.props['padding'] * 2))
                                                                     * self.vsList.props['numElems'])
        self.guiWidth = self.vsList.props['totalWidth']
        self.guiHeight = self.vsList.props['totalHeight']
        self.vsList.props['elemMargin'] = self.guiWidth / self.vsList.props['numElems']

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        # self._drawArray(qp)
        self.vsList.drawList(qp)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Canvas()
    sys.exit(app.exec_())
