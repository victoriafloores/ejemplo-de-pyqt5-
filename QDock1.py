import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DockDemo(QMainWindow):
    def __init__(self,parent=None):
        super(DockDemo, self).__init__(parent)
        layout=QHBoxLayout()
        bar=self.menuBar()
        file=bar.addMenu('File')
        file.addAction('New')
        file.addAction('Save')
        file.addAction('quit')

        self.items=QDockWidget('animales',self)

        self.listWidget=QListWidget()
        self.listWidget.addItem('perro')
        self.listWidget.addItem('gato')
        self.listWidget.addItem('leon')
        self.listWidget.addItem('pez')

        self.items.setWidget(self.listWidget)
        self.items.setFloating(False)
        self.setCentralWidget(QTextEdit())
        self.addDockWidget(Qt.RightDockWidgetArea,self.items)

        self.setLayout(layout)
        self.setWindowTitle('Dock')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=DockDemo()
    demo.show()
    sys.exit(app.exec_())
