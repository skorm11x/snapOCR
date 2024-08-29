import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QRubberBand
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import QRect, Qt, QPoint
from PyQt5.QtGui import QImage
from PIL import ImageGrab

class ScreenCapture(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowTransparentForInput)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(0, 0, QApplication.primaryScreen().size().width(), QApplication.primaryScreen().size().height())
        self.rubber_band = QRubberBand(QRubberBand.Rectangle, self)
        self.start_point = QPoint()

        self.showFullScreen()
        self.setMouseTracking(True)
        self.setWindowOpacity(0.3)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_point = event.pos()
            self.rubber_band.setGeometry(QRect(self.start_point, QSize()))
            self.rubber_band.show()

    def mouseMoveEvent(self, event):
        if self.rubber_band.isVisible():
            self.rubber_band.setGeometry(QRect(self.start_point, event.pos()).normalized())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.rubber_band.hide()
            rect = self.rubber_band.geometry()
            x1, y1, x2, y2 = rect.left(), rect.top(), rect.right(), rect.bottom()
            self.capture_screen(x1, y1, x2, y2)
            self.close()

    def capture_screen(self, x1, y1, x2, y2):
        screen = QApplication.primaryScreen()
        screenshot = screen.grabWindow(0, x1, y1, x2-x1, y2-y1)
        screenshot.save("screenshot.png", "png")
        print("Screenshot saved as 'screenshot.png'.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScreenCapture()
    sys.exit(app.exec_())