

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from mysql.connector import Error
from Stream import Ui_MainWindow

class Authentification(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(339, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:#101357;")
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(70, 60, 200, 116))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.graphicsView.setBackgroundBrush(brush)
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 240, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 310, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label.setStyleSheet("color:   #2BB0C8")
        self.label_2.setStyleSheet("color: #2BB0C8")

        self.nameTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.nameTextbox.setGeometry(QtCore.QRect(30, 260, 271, 31))
        self.nameTextbox.setPlaceholderText("Enter Your ID ")
        self.nameTextbox.setObjectName("Personal ID")
        self.passTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.passTextbox.setGeometry(QtCore.QRect(30, 340, 271, 31))
        self.passTextbox.setPlaceholderText("Enter Your Password ")
        self.passTextbox.setObjectName("Personal pass")
        self.passTextbox.setEchoMode(QtWidgets.QLineEdit.Password)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Lao UI")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 410, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.label_3.setStyleSheet("color:#DE1414")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        Window_View = QtWidgets.QGraphicsScene()
        pixmap = QtGui.QPixmap("/root/Documents/MaskProject/Assests/rsz_proof-of-identification-1.png")
        Window_View.addPixmap(pixmap.scaled(
            198, 170, QtCore.Qt.KeepAspectRatio))

        self.graphicsView.setScene(Window_View)
        self.pushButton.setStyleSheet("color:#7FFF00")

        self.pushButton.clicked.connect(self.get_msg)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Authentification"))
        self.label.setText(_translate("MainWindow", "Personal ID Number"))
        self.label_2.setText(_translate("MainWindow", "Personal Password"))
        self.label_3.setText(_translate(
            "MainWindow", "Authorized Personnel Only"))
        self.pushButton.setText(_translate("MainWindow", "Login"))

    def Data_Base_Verif(self, host, Db_Name, user, Password, id, password):
        try:
            connection = mysql.connector.connect(host=host,
                                                 database=Db_Name,
                                                 user=user,
                                                 password=Password)
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute(
                    "select Password from Information where Id like "+id+";")

                result = cursor.fetchone()
                try : 
                    if result[0] == password:
                        
                        self.next_win()
                        cursor.close()
                        connection.close()
                    else:
                        print("No Authorized !")
                        cursor.close()
                        connection.close()
                except :
                    print("No Authorised attempt ! ")
                

        except Error as e:
            print("Error while connecting to MySQL", e)

    def get_msg(self):
        Name = self.nameTextbox.text()
        Pass = self.passTextbox.text()
        if (len(Name) == 0 or len(Pass) == 0):
            print("Enter Your Name & Pass !")
        else:
            self.Data_Base_Verif('localhost',
                                 'Authority',
                                 'root',
                                 'covid19', Name, Pass)

    def next_win(self):
        self.window=QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Authentification()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
