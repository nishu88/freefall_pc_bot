import sys
import tkinter as tk
from ctypes import *
##from ctypes.wintypes import *


from PIL import Image, ImageGrab
from PyQt5 import QtCore, QtGui, QtWidgets
##l=[]

class Snippy(QtWidgets.QWidget):
    def __init__(self):
        
        super().__init__()
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.setGeometry(0, 0, screen_width, screen_height)
        self.setWindowTitle(' ')
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.setWindowOpacity(0.3)
        QtWidgets.QApplication.setOverrideCursor(
            QtGui.QCursor(QtCore.Qt.CrossCursor)
        )
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.show()

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor('blue'), 1))
        qp.setBrush(QtGui.QColor(128, 128, 255, 128))
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.close()

        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())

        image = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        print(x1,y1,x2,y2)
        f = open("bbox_values.txt", "w")
        f.write(str(x1)+" "+str(y1)+" "+str(x2)+" "+str(y2))
##        l.append(x1)
##        l.append(y1)
##        l.append(x2)
##        l.append(y2)
##        print(l)
        return


        #CloseClipboard()
##        sys.exit(app.exec_())
        
def main():
    
        app = QtWidgets.QApplication(sys.argv)
        window = Snippy()
        window.show()
        app.aboutToQuit.connect(app.deleteLater)
        sys.exit(app.exec_())
        
if __name__ == '__main__':
    main()
        

    
    
