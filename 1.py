import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import  QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLCDNumber, QLineEdit
from PyQt5.QtWidgets import  QVBoxLayout, QSizePolicy, QFontDialog
from PyQt5.QtWidgets import   qApp
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
    QLabel, QApplication)
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(1, 30, 1260, 720)
        self.setWindowTitle('Генератор мемов')

        self.btn = QPushButton('Загрузить', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(500, 100)
        self.btn.clicked.connect(self.hello)

        self.btn = QPushButton('Сделать мем', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(500, 400)
        self.btn.clicked.connect(self.hello)

        self.label = QLabel(self)
        self.label.setText(' ')
        self.label.move(500, 200)

        self.name_inpu3 = QPushButton('Скачать мем', self)
        self.btn.resize(self.btn.sizeHint())
        self.name_inpu3.move(500, 400)

        self.name_inpu3 = QPushButton('Положение текста', self)
        self.btn.resize(self.btn.sizeHint())
        self.name_inpu3.move(500, 300)

        btn = QPushButton('Выбрать ширифт', self)
        btn.setSizePolicy(QSizePolicy.Fixed,
                          QSizePolicy.Fixed)

        btn.move(0, 0)

        btn.clicked.connect(self.showDialog)

        self.lbl = QLabel('Пример текста', self)

        self.lbl.move(0, 600)

        
        pixmap = QPixmap("13028.jpg")

        lbl = QLabel(self)
        lbl.resize(500, 500)
        lbl.move(0, 30)        
        lbl.setPixmap(pixmap)



        #openFile = QAction(QIcon('open.png'), 'Open', self)
        #openFile.setShortcut('Ctrl+O')
        #openFile.setStatusTip('Open new File')
        #openFile.triggered.connect(self.showDialogfile)
        
        #self.statusBar()
                
        #menubar = self.menuBar()
        #fileMenu = menubar.addMenu('&File')
        #fileMenu.addAction(openFile)

    def hello(self):
        pass

    def showDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)        
            self.lbl.adjustSize()
            print(font)

    def showDialogfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]

        f = open(fname, 'r')

        with f:
            data = f.read()
            self.textEdit.setText(data)
            print(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())