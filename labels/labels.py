#!/usr/bin/env python3

from collections.abc import Iterator
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm
from reportlab_qrcode import QRCodeImage

_labelInfo = {
    4731: (7, 27, (25.4*mm, 10*mm), (0.25*cm, 0), (0.85*cm, 1.35*cm)),
}

class AveryLabel:
    def __init__(self, label_type):
        data = _labelInfo[label_type]
        self.across, self.down, self.size, gutter, self.margins = data
        self.labelsep = self.size[0] + gutter[0], self.size[1] + gutter[1]
        self.pagesize = A4
        self.position = 0

    def _open(self, filename):
        self.canvas = canvas.Canvas(filename, pagesize=self.pagesize)

    def _topLeft(self):
        x, y = divmod(self.position, self.down)
        return self.margins[0] + x * self.labelsep[0], self.pagesize[1] - self.margins[1] - (y + 1) * self.labelsep[1]

    def _advance(self):
        self.position += 1
        if self.position == self.across * self.down:
            self.canvas.showPage()
            self.position = 0

    def _close(self):
        if self.position:
            self.canvas.showPage()
        self.canvas.save()

    def _render(self, func, iterator):
        for chunk in iterator:
            self.canvas.saveState()
            self.canvas.translate(*self._topLeft())
            func(self.canvas, self.size[0], self.size[1], chunk)
            self.canvas.restoreState()
            self._advance()

    def create_labels(self, startASN=1, num_pages=4):
        def _render(c, x, y, barcode_value):
            qr_size = min(x, y)
            qr = QRCodeImage(barcode_value, size=qr_size)
            qr.drawOn(c, 0, (y - qr_size) / 2)
            c.setFont("Helvetica", 2*mm)
            c.drawString(qr_size, (y - 2*mm * 0.8) / 2, barcode_value)

        self._open("labels.pdf")
        for page in range(num_pages):
            current_start_ASN = startASN + page * 189
            self._render(_render, (f"ASN{i:05d}" for i in range(current_start_ASN, current_start_ASN + 189)))
        self._close()

if __name__ == "__main__":
    label = AveryLabel(4731)
    label.create_labels(startASN=1, num_pages=4)
