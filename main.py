import sys
import hashlib

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDesktopWidget
from forms.entrance_student import Entrance_Student
from forms.registration_Student import Registration_Student

import platform
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDesktopWidget
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *


def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    import traceback
    text += ''.join(traceback.format_tb(tb))

    print(text)
    QMessageBox.critical(None, 'Error', text)
    quit()


sys.excepthook = log_uncaught_exceptions

from ui_splash_screen import Ui_SplashScreen    # pyuic5 splash_screen.ui -o ui_splash_screen.py

from ui_main import Ui_MainWindow

counter = 0


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)



        self.show()

    def progress(self):

        global counter

        self.ui.progressBar.setValue(counter)

        if counter > 100:
            self.timer.stop()

            self.main = apposition()
            self.main.show()

            self.close()

        counter += 1


class apposition(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data/Enter_or_regist.ui', self)
        self.initUI()

    def initUI(self):
        self.center()
        self.btn_enter.clicked.connect(self.Entrance)
        self.btn_regist.clicked.connect(self.Regist)

    def Entrance(self):
        self.ch = Entrance_Student()
        self.ch.show()

    def Regist(self):
        self.ch = Registration_Student()
        self.ch.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())

