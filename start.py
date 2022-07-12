from PyQt5 import QtWidgets
from controller.TableETLController import TableETLController

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = TableETLController()
    window.show()
    sys.exit(app.exec_())
