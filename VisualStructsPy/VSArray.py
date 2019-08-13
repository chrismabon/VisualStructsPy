from PyQt5.QtGui import (QColor, QFont)


class VSArray:
    font = {
        'fontSize': 14,
        'fontFamily': 'Monospace'
    }
    data = [
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
    props = {
        'numElems': 0,
        'elemWidth': 0,
        'elemHeight': 0,
        'totalHeight': 0,
        'totalWidth': 0,
        'textMargins': 0,
        'padding': font['fontSize'] / 2
    }

    def __init__(self):
        pass

    def _drawArray(self, qp):
        qp.setFont(QFont(self.font['fontFamily'], self.font['fontSize']))
        elemWidth = self.props['elemWidth']
        elemHeight = self.props['elemHeight']
        txtMargins = self.props['textMargins']

        def _drawArrElem(x, y, w, h, index, data):
            qp.setPen(QColor(0, 0, 0))
            qp.setBrush(QColor(150, 250, 250))
            qp.drawRect(x, y, w, h)
            padding = self.font['fontSize']
            qp.drawText(x + txtMargins, y + txtMargins + (elemHeight / 2), str(index))
            qp.drawLine(x + txtMargins + (padding * 2), y, x + txtMargins + (padding * 2),
                        y + txtMargins + elemHeight)
            qp.drawText(x + txtMargins + padding + (self.font['fontSize'] * 2),
                        y + txtMargins + (elemHeight / 2), str(data))

        i = 0
        while i < self.props['numElems']:
            offset = i * elemHeight
            _drawArrElem(txtMargins, txtMargins + offset, elemWidth, elemHeight, i, self.data[i])
            i += 1

