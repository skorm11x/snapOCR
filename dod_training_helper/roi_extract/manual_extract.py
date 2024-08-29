from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QPainter, QPixmap
import sys
import os
import tempfile

class SelectionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Manual ROI Selection')
        
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.showFullScreen()

        screen = QApplication.primaryScreen()
        self._background_pixmap = screen.grabWindow(0)
        self.setFixedSize(self._background_pixmap.size())

        self.overlay = QWidget(self)
        self.overlay.setGeometry(self.rect())
        self.overlay.setStyleSheet("background-color: rgba(0, 0, 0, 0.2);")
        
        self.instructions_label = QLabel("Click and drag to select the area.", self.overlay)
        self.instructions_label.setStyleSheet("color: white; font-size: 20px;")
        self.instructions_label.adjustSize()
        self.instructions_label.move(
            (self.overlay.width() - self.instructions_label.width()) // 2,
            (self.overlay.height() - self.instructions_label.height()) // 2
        )
        self.overlay.show()

        self._start_point = None
        self._end_point = None
        self.filename = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._start_point = event.pos()
            self.update()

    def mouseMoveEvent(self, event):
        if self._start_point:
            self._end_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._end_point = event.pos()
            self._save_selection()
            self.close()

    def _save_selection(self):
        if not self._start_point or not self._end_point:
            return

        rect = QRect(self._start_point, self._end_point).normalized()

        temp_dir = tempfile.mkdtemp()
        self.filename = os.path.join(temp_dir, 'ROI.png')
        selected_pixmap = self._background_pixmap.copy(rect)
        selected_pixmap.save(self.filename, 'PNG')

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self._background_pixmap)

        if self._start_point and self._end_point:
            painter.setPen(Qt.red)
            painter.setBrush(Qt.NoBrush)
            rect = QRect(self._start_point, self._end_point).normalized()
            painter.drawRect(rect)

def getManualRoi():
    app = QApplication(sys.argv)
    window = SelectionWindow()
    window.show()
    app.exec_()
    return window.filename, app

if __name__ == "__main__":
    getManualRoi()
