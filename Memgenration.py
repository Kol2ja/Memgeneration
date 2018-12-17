import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLCDNumber, QLineEdit
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton,
                             QSizePolicy, QLabel, QFontDialog, QApplication)


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
        self.label.setText(' ' * 140)
        self.label.move(500, 200)

        self.name_inpu3 = QPushButton('Скачать мем', self)
        self.btn.resize(self.btn.sizeHint())
        self.name_inpu3.move(500, 500)

        self.name_inpu3 = QPushButton('Положение текста', self)
        self.btn.resize(self.btn.sizeHint())
        self.name_inpu3.move(500, 300)

        vbox = QVBoxLayout()

        btn = QPushButton('Выбрать ширифт', self)
        btn.setSizePolicy(QSizePolicy.Fixed,
                          QSizePolicy.Fixed)

        btn.move(500, 200)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialogfile)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

    def hello(self):
        pass

    def showDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)

    def showDialogfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]

        f = open(fname, 'r')

        with f:
            data = f.read()
            self.textEdit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
