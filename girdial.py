
from PyQt5 import QtCore, QtGui, QtWidgets
from eslestirmesonuc import Ui_eslestirmesonuc
from tournament import Tournament
from team import Team, Person
from match import Match
from PyQt5.QtWidgets import QMessageBox

class Ui_Form(object):

    memberCount = 0
    isTeam = False

    def setupUi(self, Form, takimsayisi, memberCount, isTeam):

        self.memberCount = memberCount
        self.isTeam = isTeam
        
        Form.setObjectName("Form")
        Form.resize(300, 200)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
    #Takım isimlerini Depolayıp Sonucu Alacağımız Forma Aktarabileceğimiz Bir takımisim adlı liste değişkeni oluşturduk
        self.takimisim = []
    #For döngüsü ile önceki Formdan Aldıgımız takımsayisi kadar textbox ve label olusturduk
        for i in range(takimsayisi):
            label = QtWidgets.QLabel(Form)
            label.setText(f"Takım {i + 1}:")
            self.verticalLayout.addWidget(label)
            takimisim = QtWidgets.QLineEdit(Form)
            takimisim.setObjectName(f"takimisim_{i}")
            self.verticalLayout.addWidget(takimisim)
            self.takimisim.append(takimisim)

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.yeniformac)


    #Önceki Formdaki button islevine benzer olarak bir yeniformac fonksiyonu oluşturduk
    def yeniformac(self):
        
        tournament = Tournament(None)
        tournament.teams = []
       
        for textbox in self.takimisim:

            team = Team(textbox.text(), self.memberCount) if self.isTeam else Person(textbox.text())
            tournament.AddTeam(team)

        self.window = QtWidgets.QWidget()
        self.ui = Ui_eslestirmesonuc()
        self.ui.setupUi(self.window, tournament, self.isTeam)
        self.window.show()
        
        
           

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Takım İsimlerini Giriniz"))
        self.pushButton.setText(_translate("Form", "Takımları Eşleştir"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())