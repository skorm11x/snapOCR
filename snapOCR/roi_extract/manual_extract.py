""" Creates a PYQT application that allows the user to select a region to send to the OCR engine.
"""

import os
import tempfile
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter


class SelectionWindow(QMainWindow):
    """

    Args:
        QMainWindow (QMainWindow): class inherits QMainWIndow
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manual ROI Selection")

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.showFullScreen()

        screen = QApplication.primaryScreen()
        self._background_pixmap = screen.grabWindow(0)
        self.setFixedSize(self._background_pixmap.size())

        self.overlay = QWidget(self)
        self.overlay.setGeometry(self.rect())
        self.overlay.setStyleSheet("background-color: rgba(0, 0, 0, 0.2);")

        self.instructions_label = QLabel(
            "Click and drag to select the area.", self.overlay
        )
        self.instructions_label.setStyleSheet("color: white; font-size: 20px;")
        self.instructions_label.adjustSize()
        self.instructions_label.move(
            (self.overlay.width() - self.instructions_label.width()) // 2,
            (self.overlay.height() - self.instructions_label.height()) // 2,
        )
        self.overlay.show()

        self._start_point = None
        self._end_point = None
        self.filename = None

    def mousePressEvent(self, event):  # pylint: disable=invalid-name
        """QMainWindow event listener code for mouse left button press

        Args:
            event (QEvent): left mouse press
        """
        if event.button() == Qt.LeftButton:
            self._start_point = event.pos()
            self.update()

    def mouseMoveEvent(self, event):  # pylint: disable=invalid-name
        """QMainWindow event listener code for mouse movement

        Args:
            event (QEvent): mouse movement
        """
        if self._start_point:
            self._end_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):  # pylint: disable=invalid-name
        """QMainWindow event lisener code for mouse left button press release

        Args:
            event (QEvent): left mouse release from press
        """
        if event.button() == Qt.LeftButton:
            self._end_point = event.pos()
            self._save_selection()
            self.close()

    def _save_selection(self):
        """Save the pixelmap located in the rectangle bounding region to a temporary PNG file."""
        if not self._start_point or not self._end_point:
            return

        rect = QRect(self._start_point, self._end_point).normalized()

        temp_dir = tempfile.mkdtemp()
        self.filename = os.path.join(temp_dir, "ROI.png")
        selected_pixmap = self._background_pixmap.copy(rect)
        selected_pixmap.save(self.filename, "PNG")

    def paintEvent(self, event):  # pylint: disable=invalid-name
        """Paints the empty pixel map with the pixels specified in the recntangle bounding region

        Args:
            event (QEvent): driven by completion of the PyQT rect
        """
        super().paintEvent(event)
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self._background_pixmap)

        if self._start_point and self._end_point:
            painter.setPen(Qt.red)
            painter.setBrush(Qt.NoBrush)
            rect = QRect(self._start_point, self._end_point).normalized()
            painter.drawRect(rect)


def get_manual_roi(app):
    """Driver function exposed to run manual ROI acquisiton

    Returns:
        str, QApplication: filename path of temporary file, QApplication
    """
    # app = QApplication(sys.argv)
    window = SelectionWindow()
    window.show()
    app.exec_()
    # return window.filename, app
    return window.filename
