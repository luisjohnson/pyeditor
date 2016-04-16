import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

class Main(QtGui.QMainWindow):

    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)

        self.initUI()

    def  initToolbar(self):

        self.toolbar = self.addToolBar("Option")

        self.addToolBarBreak()

    def initFormatBar(self):

        self.formatbar = self.addToolBar("Format")

    def initMenuBar(self):

        menubar = self.menuBar()

        file = menubar.addMenu("File")
        file.addAction()

        
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("View")

        
    def initUI(self):

        self.text = QtGui.QTextEdit(self)
        self.setCentralWidget(self.text)

        # self.initToolbar()
        # self.initFormatBar()
        
        self.initMenuBar()

        #Initialize a status bar
        self.statusbar = self.statusBar()

        #x and y coordiates on the screen, width, height
        self.setGeometry(100,100,1030,800)

        self.setWindowTitle("pyEditor")

def main():

    app = QtGui.QApplication(sys.argv)

    main = Main()

    main.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
    

