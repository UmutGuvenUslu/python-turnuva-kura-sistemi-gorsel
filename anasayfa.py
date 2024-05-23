from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from girdial import Ui_Form

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(387, 239)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(387, 239))
        MainWindow.setStatusTip("")
        self.anasayfa = QtWidgets.QWidget(MainWindow)
        self.anasayfa.setMinimumSize(QtCore.QSize(387, 219))
        self.anasayfa.setMaximumSize(QtCore.QSize(387, 219))
        self.anasayfa.setFocusPolicy(QtCore.Qt.NoFocus)
        self.anasayfa.setObjectName("anasayfa")
        self.turnuvakurasistem = QtWidgets.QLabel(self.anasayfa)
        self.turnuvakurasistem.setGeometry(QtCore.QRect(50, 10, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.turnuvakurasistem.setFont(font)
        self.turnuvakurasistem.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.turnuvakurasistem.setTextFormat(QtCore.Qt.AutoText)
        self.turnuvakurasistem.setAlignment(QtCore.Qt.AlignCenter)
        self.turnuvakurasistem.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.turnuvakurasistem.setObjectName("turnuvakurasistem")
        self.label = QtWidgets.QLabel(self.anasayfa)
        self.label.setGeometry(QtCore.QRect(125, 70, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.takimsayi_spinbox = QtWidgets.QSpinBox(self.anasayfa)
        self.takimsayi_spinbox.setGeometry(QtCore.QRect(170, 100, 61, 41))
        self.takimsayi_spinbox.setAutoFillBackground(False)
        self.takimsayi_spinbox.setObjectName("takimsayi_spinbox")
        #SpinBoxun Başlangıç Değerini Gireriz
        self.takimsayi_spinbox.setValue(4)
        self.takmbelirle_button = QtWidgets.QPushButton(self.anasayfa)
        self.takmbelirle_button.setGeometry(QtCore.QRect(150, 160, 91, 31))
        self.takmbelirle_button.setObjectName("takmbelirle_button")
        MainWindow.setCentralWidget(self.anasayfa)
        self.actiontak_mgiris = QtWidgets.QAction(MainWindow)
        self.actiontak_mgiris.setObjectName("actiontak_mgiris")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # "Takımları Belirle" butonuna tıklayınca yapılacak fonksiyon
        self.takmbelirle_button.clicked.connect(self.yeniformac)
        #Formdaki Text Ayarları
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Ana Sayfa", "Ana Sayfa"))
        self.turnuvakurasistem.setText(_translate("Ana Sayfa", "Turnuva Kura Sistemi"))
        self.label.setText(_translate("Ana Sayfa", "Takım Sayısını Giriniz"))
        self.takmbelirle_button.setText(_translate("Ana Sayfa", "Takımları Belirle"))
        self.actiontak_mgiris.setText(_translate("Ana Sayfa", "takımgiris"))
#Burada Takımları Belirle Butonuna Bastığımızda Açılacak Yeni Formu Ve Takım Sayısının Hangi Kurallara Göre Belirleneceğini Belirtiyoruz
    def yeniformac(self):
        takimsayisi = self.takimsayi_spinbox.value()
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Hata")
           
        if takimsayisi < 4:
            msg.setText('Takım Sayısı 4 veya daha fazla olmalıdır!!')
            msg.exec_()
            return
        
        if takimsayisi > 16 :
            msg.setText('Takım sayısı 16 veya daha az olmalıdır!')
            msg.exec_()
            return

        if takimsayisi % 2 != 0:
            msg.setText('Takım sayısı çift olmalıdır!!')
            msg.exec_()
            return
        
        
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window,takimsayisi)
        self.window.show()
        MainWindow.hide()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

