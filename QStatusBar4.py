import sys
from PyQt5 import QtCore, QtWidgets

class Principal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setCentralWidget(QtWidgets.QWidget())

        self.statusBar = QtWidgets.QStatusBar()
        self.setStatusBar(self.statusBar)
        self.label_hora = QtWidgets.QLabel()
        self.statusBar.addPermanentWidget(self.label_hora, 0)

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.mostrar_hora)
        self.timer.start()

    def mostrar_hora(self):
        self.label_hora.setText(QtCore.QDateTime.currentDateTime()
                                                .toString("hh:mm:ss AP")
                                   )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    p = Principal()
    p.show()
    sys.exit(app.exec_())