import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt, QRegExp, QString
from PyQt4.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter, QTextCursor


class Window(QtGui.QMainWindow):
    def __init__(self, parent = None):
        super(Window, self).__init__()
        self.setWindowTitle("Just Another Text Editor")
        self.initTextEdtor()
        self.setupFileMenu()
        self.showMaximized()


    def newFile(self):
        self.TextEditor.clear()

    def openFile(self, path=None):
        if not path:
            path = QtGui.QFileDialog.getOpenFileName(self, "Open File",
                                                     '', "Text Files (*.txt);;Markdown Files (*.md)")

        if path:
            inFile = QtCore.QFile(path)
            if inFile.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
                text = inFile.readAll()

                try:
                    # Python v3.
                    text = str(text, encoding='ascii')
                except TypeError:
                    # Python v2.
                    text = str(text)


                self.TextEditor.setPlainText(text)

    def setupFileMenu(self):
        fileMenu = QtGui.QMenu("&File", self)
        self.menuBar().addMenu(fileMenu)

        fileMenu.addAction("&New...", self.newFile, "Ctrl+N")
        fileMenu.addAction("&Open...", self.openFile, "Ctrl+O")
        fileMenu.addAction("E&xit", QtGui.qApp.quit, "Ctrl+Q")

        

    def  initTextEdtor(self):
        self.TextEditor = QtGui.QTextEdit(self)
        self.setCentralWidget(self.TextEditor)
        self.TextEditor.cursorPositionChanged.connect(self.cursorPosition)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setFamily("Helvetica Neue Light")
        self.TextEditor.setFont(font)       
        #self.TextEditor.setStyleSheet("QTextEdit { border: 300px solid white; }")
        self.TextEditor.setStyleSheet("QTextEdit { border-top: 100px solid white; border-bottom: 20px solid white; border-right: 300px solid white; border-left: 300px solid white;}")
        self.highlighter = Highlighter(self.TextEditor.document())

    def cursorPosition(self):

        cursor = self.TextEditor.textCursor()

        # cursor.select(QTextCursor.WordUnderCursor)

        # c = cursor.selectedText().right(1);
        
        # if c != "h" and  not flag:

        #     cursor.movePosition(QTextCursor.Right)
        #     cursor.insertText(c)
        #     cursor.movePosition(QTextCursor.Left)
        #     global flag
        #     flag = False
            
class Highlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(Highlighter, self).__init__(parent)

        keywordFormat = QtGui.QTextCharFormat()
        keywordFormat.setForeground(QtCore.Qt.blue)
        keywordFormat.setFontWeight(QtGui.QFont.Bold)


        keywordPatterns = [u'TODO', u'NOTE', u'HIGHLIGHT', u'REF']

        self.highlightingRules = [(QtCore.QRegExp(pattern), keywordFormat)
                for pattern in keywordPatterns]
       
        Header1Format = QtGui.QTextCharFormat()
        Header1Format.setFontWeight(QtGui.QFont.Bold)
        Header1Format.setForeground(QColor(28,155,200))
        self.highlightingRules.append((QtCore.QRegExp("^#[^#\n]*"),
                                       Header1Format))
        
        Header2Format = QtGui.QTextCharFormat()
        Header2Format.setFontWeight(QtGui.QFont.Bold)
        Header2Format.setForeground(QColor(255,51,153))
        self.highlightingRules.append((QtCore.QRegExp("^##[^##\n]*"),
                                       Header2Format))

        EmphasizeFormat = QtGui.QTextCharFormat()
        EmphasizeFormat.setFontItalic(True)
        EmphasizeFormat.setForeground(QColor(193,41,130))
        self.highlightingRules.append((QtCore.QRegExp("\*(\S[^\*]+\S|[^\*\s]{1,2})\*(?!\w)"),
                                       EmphasizeFormat))

      
        
        singleLineCommentFormat = QtGui.QTextCharFormat()
        singleLineCommentFormat.setForeground(QtCore.Qt.red)
        self.highlightingRules.append((QtCore.QRegExp("//[^\n]*"),
                singleLineCommentFormat))

        self.multiLineCommentFormat = QtGui.QTextCharFormat()
        self.multiLineCommentFormat.setForeground(QtCore.Qt.red)

        quotationFormat = QtGui.QTextCharFormat()
        quotationFormat.setForeground(QtCore.Qt.darkGreen)
        self.highlightingRules.append((QtCore.QRegExp("\".*\""),
                quotationFormat))

        functionFormat = QtGui.QTextCharFormat()
        functionFormat.setFontItalic(True)
        functionFormat.setForeground(QtCore.Qt.blue)
        self.highlightingRules.append((QtCore.QRegExp("\\b[A-Za-z0-9_]+(?=\\()"),
                functionFormat))

        self.commentStartExpression = QtCore.QRegExp("/\\*")
        self.commentEndExpression = QtCore.QRegExp("\\*/")

    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QtCore.QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        startIndex = 0
        if self.previousBlockState() != 1:
            startIndex = self.commentStartExpression.indexIn(text)

        while startIndex >= 0:
            endIndex = self.commentEndExpression.indexIn(text, startIndex)

            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength = len(text) - startIndex
            else:
                commentLength = endIndex - startIndex + self.commentEndExpression.matchedLength()

            self.setFormat(startIndex, commentLength,
                    self.multiLineCommentFormat)
            startIndex = self.commentStartExpression.indexIn(text,
                    startIndex + commentLength);


            
    

def main():
    app = QtGui.QApplication(sys.argv)
        
    main = Window()

    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":

    main()
