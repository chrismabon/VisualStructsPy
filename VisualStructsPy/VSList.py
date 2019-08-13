from VisualStructsPy.VSNode import VSNode

from PyQt5.QtGui import (QColor, QFont, QTransform)


class VSList:
    def __init__(self):
        self.font = {
            'fontSize': 20,
            'fontFamily': 'Monospace'
        }
        self.data = [
            'Nulla ac tellus lacus.',
            'Morbi euismod mi lorem, non placerat tellus iaculis et.',
            'Ut in feugiat nisl, in fringilla leo.',
            'In hendrerit blandit velit vitae ullamcorper.',
            'Nullam a pretium ex, in hendrerit nulla.',
            'Donec fermentum purus eget magna fermentum blandit.',
            'Nulla id neque vel diam vestibulum convallis id a felis.',
            'Quisque ac eros at magna mollis suscipit in vitae turpis.',
            'Duis sodales mattis scelerisque.'
        ]
        self.props = {
            'numElems': 0,
            'elemWidth': 0,
            'elemHeight': 0,
            'elemMargin': 0,
            'totalHeight': 0,
            'totalWidth': 0,
            'textMargins': 0,
            'padding': self.font['fontSize'] / 2
        }

    def drawList(self, qp):
        elemWidth = self.props['elemWidth']
        elemHeight = self.props['elemHeight']
        padding = self.props['padding']
        txtMargins = self.props['textMargins']
        qp.setFont(QFont(self.font['fontFamily'], self.font['fontSize']))
        qp.setPen(QColor(0, 0, 0))

        def _drawListElem(x, y, w, h, data):
            qp.setBrush(QColor(150, 250, 250))
            qp.setFont(QFont(self.font['fontFamily'], self.font['fontSize'] - 6))
            qp.drawEllipse(x + txtMargins + (elemWidth / 2) + padding, y + padding, w, h)
            qp.drawText(x + (txtMargins * 2) + padding + (elemWidth / 2), y + txtMargins + padding
                        + (elemHeight / 2.5), str(data))

        def _drawListHead(count):
            qp.setBrush(QColor(250, 0, 0))
            x = self.props['elemMargin']
            y = self.props['elemMargin']
            w = (self.props['totalWidth'] / 2.5) - (self.props['elemMargin'])
            h = (self.props['totalHeight'] / 2) - (self.props['elemMargin'] * 2)
            qp.drawRect(x, y, w, h)
            qp.drawText(x + txtMargins, y - txtMargins, 'Count:' + str(count))
        _drawListHead(self.data.__len__())

        i = 0

        while i < self.props['numElems']:
            transform = QTransform.translate(QTransform(1, 0, 0, 1, i * 5.0, 20.0), 1.0, 1.0)
            qp.setTransform(transform)
            offset = int(i * elemWidth + (elemWidth / 2))
            _drawListElem(txtMargins + offset + (padding * i * 2), txtMargins + elemHeight, elemWidth, elemHeight,
                          self.data[i][0:4])
            i += 1
