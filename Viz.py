
from crypt import Cryp_Decry
from PyQt5 import QtCore, QtGui, QtWidgets
import time
from crypt import Cryp_Decry
import os


f = open("id_ref.txt", "r")
Id_ = f.read()
Id_ = int(Id_)


class Visual(object):
    def setupUi(self, MainWindow):
        self.decision_var = 0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(806, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color:#101357;")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 60, 541, 471))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 530, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 10, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(570, 90, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(570, 190, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(570, 280, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(570, 380, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label10 = QtWidgets.QLabel(self.centralwidget)
        self.label10.setGeometry(QtCore.QRect(570, 140, 201, 31))
        self.label10.setObjectName("Day")
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(55)
        self.label10.setStyleSheet("color : green")
        self.label10.setFont(font)

        self.label11 = QtWidgets.QLabel(self.centralwidget)
        self.label11.setGeometry(QtCore.QRect(570, 230, 201, 31))
        self.label11.setObjectName("Month")
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(55)
        self.label11.setStyleSheet("color : green")
        self.label11.setFont(font)

        self.label12 = QtWidgets.QLabel(self.centralwidget)
        self.label12.setGeometry(QtCore.QRect(570, 330, 201, 31))
        self.label12.setObjectName("Year")
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(55)
        self.label12.setStyleSheet("color : green")
        self.label12.setFont(font)

        self.label13 = QtWidgets.QLabel(self.centralwidget)
        self.label13.setGeometry(QtCore.QRect(570, 430, 201, 31))
        self.label13.setObjectName("Time")
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(55)
        self.label13.setStyleSheet("color : green")
        self.label13.setFont(font)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 480, 91, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 480, 91, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(660, 10, 101, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton.setStyleSheet("color : #32CD32")
        self.pushButton_2.setStyleSheet("color : #32CD32")
        self.pushButton_3.setStyleSheet("color:#32CD32")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_2.setStyleSheet("color:#ffffff")
        self.label_3.setStyleSheet("color:#ffffff")
        self.label_4.setStyleSheet("color:#ffffff")
        self.label_5.setStyleSheet("color:#ffffff")
        self.label_6.setStyleSheet("color:#ffffff")
        self.label.setStyleSheet("color:#fbaf08")

        self.pushButton.clicked.connect(self.next_btn)
        self.pushButton_2.clicked.connect(self.previous_btn)
        self.pushButton_3.clicked.connect(self.print_fn)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate(
            "MainWindow", "For a safer World , Wear Masks !"))
        self.label_2.setText(_translate(
            "MainWindow", "-------SPOTTED PEOPLE--------"))
        self.label_3.setText(_translate("MainWindow", "DAY :"))
        self.label_4.setText(_translate("MainWindow", "MONTH :"))
        self.label_5.setText(_translate("MainWindow", "YEAR :"))
        self.label_6.setText(_translate("MainWindow", "TIME :"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushButton_2.setText(_translate("MainWindow", "Previous"))
        self.pushButton_3.setText(_translate("MainWindow", "Print Report"))

    def next_btn(self):
        _translate = QtCore.QCoreApplication.translate

        if self.decision_var < Id_-1:

            self.decision_var += 1
            mon_classe = Cryp_Decry()
            mon_classe.data_base_decrypt(
                "/root/Documents/MaskProject/Streaming record/", str(self.decision_var))
           # QtCore.QMetaObject.connectSlotsByName(MainWindow)

            Window_View = QtWidgets.QGraphicsScene()
            f = open("path_img_decrypt.txt", "r")
            a = f.read()
            f.close()

            self.label10.setText(_translate("MainWindow", a[14:16]))  # day
            self.label11.setText(_translate("MainWindow", a[11:13]))  # month
            self.label12.setText(_translate("MainWindow", a[6:10]))  # year
            self.label13.setText(_translate("MainWindow", a[17:24]))  # time
            pixmap = QtGui.QPixmap(a)
            Window_View.addPixmap(pixmap.scaled(
                630, 570, QtCore.Qt.KeepAspectRatio))
            self.graphicsView.setScene(Window_View)
            os.remove(a)
        else:
            print("No photo !")

    def previous_btn(self):
        _translate = QtCore.QCoreApplication.translate

        if self.decision_var > 0:

            self.decision_var -= 1
            mon_classe = Cryp_Decry()
            mon_classe.data_base_decrypt(
                "/root/Documents/MaskProject/Streaming record/", str(self.decision_var))

           # QtCore.QMetaObject.connectSlotsByName(MainWindow)

            Window_View = QtWidgets.QGraphicsScene()
            f = open("path_img_decrypt.txt", "r")
            a = f.read()
            f.close()

            self.label10.setText(_translate("MainWindow", a[14:16]))  # day
            self.label11.setText(_translate("MainWindow", a[11:13]))  # month
            self.label12.setText(_translate("MainWindow", a[6:10]))  # year
            self.label13.setText(_translate("MainWindow", a[17:24]))  # time
            pixmap = QtGui.QPixmap(a)
            Window_View.addPixmap(pixmap.scaled(
                630, 570, QtCore.Qt.KeepAspectRatio))
            self.graphicsView.setScene(Window_View)
            os.remove(a)

        else:
            print("No Photo !")

    def print_fn(self):
        print("print")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Visual()
    ui.setupUi(MainWindow)
    f = open("path_img_decrypt.txt", "w")
    f.write("")
    f.close()
    
    MainWindow.show()
    sys.exit(app.exec_())