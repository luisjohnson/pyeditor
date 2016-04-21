import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

class Window(QtGui.QMainWindow):
    def __init__(self, parent = None):
        super(Window, self).__init__()
        self.setWindowTitle("Just Another Text Editor")
        self.initTextEdtor()
        self.showMaximized()

    def  initTextEdtor(self):
        self.TextEditor = QtGui.QTextEdit(self)
        self.setCentralWidget(self.TextEditor)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setFamily("Helvetica")
        self.TextEditor.setFont(font)       
        self.TextEditor.setStyleSheet("QTextEdit { border: 100px solid white}")

#class HighLighter(QtGui.QSyntaxHighlighter):
    

def main():
    app = QtGui.QApplication(sys.argv)
        
    main = Window()

    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":

    main()
