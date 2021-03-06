# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources\ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(314, 454)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_buildPlot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_buildPlot.setMinimumSize(QtCore.QSize(0, 23))
        self.pushButton_buildPlot.setMaximumSize(QtCore.QSize(16777215, 23))
        self.pushButton_buildPlot.setObjectName("pushButton_buildPlot")
        self.gridLayout.addWidget(self.pushButton_buildPlot, 4, 3, 1, 2)
        self.widget_plot = PlotWidget(self.centralwidget)
        self.widget_plot.setMinimumSize(QtCore.QSize(0, 300))
        self.widget_plot.setObjectName("widget_plot")
        self.gridLayout.addWidget(self.widget_plot, 0, 0, 1, 5)
        self.lineEdit_formula = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_formula.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_formula.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lineEdit_formula.setObjectName("lineEdit_formula")
        self.gridLayout.addWidget(self.lineEdit_formula, 4, 0, 1, 3)
        self.lineEdit_s2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_s2.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_s2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lineEdit_s2.setObjectName("lineEdit_s2")
        self.gridLayout.addWidget(self.lineEdit_s2, 3, 4, 1, 1)
        self.lineEdit_xmin = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_xmin.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_xmin.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lineEdit_xmin.setObjectName("lineEdit_xmin")
        self.gridLayout.addWidget(self.lineEdit_xmin, 3, 0, 1, 1)
        self.lineEdit_xstep = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_xstep.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_xstep.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lineEdit_xstep.setObjectName("lineEdit_xstep")
        self.gridLayout.addWidget(self.lineEdit_xstep, 3, 2, 1, 1)
        self.label_maxDifference = QtWidgets.QLabel(self.centralwidget)
        self.label_maxDifference.setMinimumSize(QtCore.QSize(0, 13))
        self.label_maxDifference.setMaximumSize(QtCore.QSize(16777215, 13))
        self.label_maxDifference.setObjectName("label_maxDifference")
        self.gridLayout.addWidget(self.label_maxDifference, 1, 0, 1, 5)
        self.lineEdit_xmax = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_xmax.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_xmax.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lineEdit_xmax.setObjectName("lineEdit_xmax")
        self.gridLayout.addWidget(self.lineEdit_xmax, 3, 1, 1, 1)
        self.lineEdit_s1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_s1.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_s1.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lineEdit_s1.setObjectName("lineEdit_s1")
        self.gridLayout.addWidget(self.lineEdit_s1, 3, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 13))
        self.label.setMaximumSize(QtCore.QSize(16777215, 13))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 13))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 13))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 13))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 13))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 13))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 13))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(0, 13))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 13))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 4, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 314, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_buildPlot.setText(_translate("MainWindow", "build"))
        self.lineEdit_formula.setText(_translate("MainWindow", "x*sin(x)"))
        self.lineEdit_formula.setPlaceholderText(_translate("MainWindow", "f(x)"))
        self.lineEdit_s2.setText(_translate("MainWindow", "0"))
        self.lineEdit_s2.setPlaceholderText(_translate("MainWindow", "right derivative"))
        self.lineEdit_xmin.setText(_translate("MainWindow", "-20"))
        self.lineEdit_xmin.setPlaceholderText(_translate("MainWindow", "x min"))
        self.lineEdit_xstep.setText(_translate("MainWindow", "4"))
        self.lineEdit_xstep.setPlaceholderText(_translate("MainWindow", "x dpi"))
        self.label_maxDifference.setText(_translate("MainWindow", "max difference: "))
        self.lineEdit_xmax.setText(_translate("MainWindow", "20"))
        self.lineEdit_xmax.setPlaceholderText(_translate("MainWindow", "x max"))
        self.lineEdit_s1.setText(_translate("MainWindow", "0"))
        self.lineEdit_s1.setPlaceholderText(_translate("MainWindow", "left derivative"))
        self.label.setText(_translate("MainWindow", "x min"))
        self.label_2.setText(_translate("MainWindow", "x max"))
        self.label_3.setText(_translate("MainWindow", "x step"))
        self.label_4.setText(_translate("MainWindow", "f \'(X0)"))
        self.label_5.setText(_translate("MainWindow", "f \'(Xn)"))
from .plotwidget import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
