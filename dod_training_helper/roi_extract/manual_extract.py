from PyQt5.QtWidgets import QApplication, QMainWindow
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
        self.background_pixmap = screen.grabWindow(0)
        self.setFixedSize(self.background_pixmap.size())

        self.start_point = None
        self.end_point = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_point = event.pos()
            self.update()

    def mouseMoveEvent(self, event):
        if self.start_point:
            self.end_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.end_point = event.pos()
            self.save_selection()
            self.close()

    def save_selection(self):
        if not self.start_point or not self.end_point:
            return

        rect = QRect(self.start_point, self.end_point).normalized()

        temp_dir = tempfile.mkdtemp()
        filename = os.path.join(temp_dir, 'ROI.png')
        selected_pixmap = self.background_pixmap.copy(rect)
        selected_pixmap.save(filename, 'PNG')

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.background_pixmap)

        if self.start_point and self.end_point:
            painter.setPen(Qt.red)
            painter.setBrush(Qt.NoBrush)
            rect = QRect(self.start_point, self.end_point).normalized()
            painter.drawRect(rect)

def main():
    app = QApplication(sys.argv)
    window = SelectionWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
