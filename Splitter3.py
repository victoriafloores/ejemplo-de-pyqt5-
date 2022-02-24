import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
class MyApp(QWidget): 
  def __init__(self,parent=None):
             layout=QHBoxLayout()
             super().__init__()
             self.title = "hola"
             self.top = 400
             self.left = 100
             self.width = 300
             self.height = 200

splitter1 = QSplitter(Qt.Horizontal)
splitter1.setStyleSheet('background color:Turquoise')
lineedit = QLineEdit()
lineedit.setStyleSheet('background-color:pink')
splitter1.addWidget(left)
splitter1.addWidget(lineedit)
splitter1.setSizes([200,200])
spliiter2 = QSplitter(Qt.Vertical)
spliiter2.addWidget(splitter1)
spliiter2.addWidget(bottom)
spliiter2.setStyleSheet('background color:Purple')
hbox.addWidget(spliiter2)
self.setLayout(hbox)
self.setWindowIcon(QtGui.QIcon("icon.png"))
self.setWindowTitle(self.title)
self.setGeometry(self.left, self.top, self.width, self.height)
        
def __init__(self,parent=None):
        super(DockDemo, self).__init__(parent)
        layout=QHBoxLayout()
        bar=self.menuBar()
        file=bar.addMenu('File')
        file.addAction('New')
        file.addAction('Save')
        file.addAction('quit')
self.statusBar = QStatusBar()
self.setStatusBar(self.statusBar)
self.label_hora = QApplication.QLabel()
self.statusBar.addPermanentWidget(self.label_hora, 0)
self.timer = QtCore.QTimer(self)
self.timer.setInterval(1000)
self.timer.timeout.connect(self.mostrar_hora)
self.timer.start()

                                   
self.items=QDockQApplication('animales',self)
self.listQApplication.addItem('raton')
self.listQApplication.addItem('perro')
self.listQApplication.addItem('gato')
self.listQApplication.addItem('leon')
self.lisQApplication.addItem('pez')

if __name__ == '__main__':
  App = QApplication(sys.argv)
window = Window()
p = Principal()
p.show()
demo=DockDemo()
demo.show()
sys.exit(App.exec())