#
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

class Main(QtGui.QMainWindow):

    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)

        self.filename = ""
        
        self.initUI()

    def  initToolbar(self):

        self.toolbar = self.addToolBar("Option")

        self.addToolBarBreak()

    def initFormatBar(self):

        self.formatbar = self.addToolBar("Format")

    def initMenuBar(self):

        menubar = self.menuBar()

        self.newAction = QtGui.QAction("New", self)
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.triggered.connect(self.new)
         
        self.openAction = QtGui.QAction("Open", self)
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.open)
              
        self.saveAction = QtGui.QAction("Save", self)
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self.save)


        file = menubar.addMenu("File")

        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAction)
        

        
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

        
    def new(self):

        spawn = Main(self)
        spawn.show()

    def open(self):

        self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', ".", "(*.writer)")

        if self.filename:
            with open(self.filename, "rt") as file:
                self.text.setText(file.read())

    def save(self):

        if not self.filename:
            self.filename = QtGui.QFileDialog.getSaveFileName(self, "Save File")

        if not self.filename.endswith(".writer"):
            self.filename += ".writer"

        with open(self.filename, "wt") as file:
            file.write(self.text.toHtml())
                
            
        

def main():

    app = QtGui.QApplication(sys.argv)

    main = Main()

    main.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
