from PyQt5 import QtWidgets
from controller.SheetTableETLController import SheetTableETLController

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = SheetTableETLController()
    window.show()
    sys.exit(app.exec_())
