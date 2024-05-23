
from PyQt5 import QtCore, QtGui, QtWidgets
import random
from tournament import Tournament
from match import Match
from team import Team

class Ui_eslestirmesonuc(object):
    def setupUi(self, eslestirmesonuc, tournament, isTeam):
       
        eslestirmesonuc.setObjectName("eslestirmesonuc")
        eslestirmesonuc.resize(394, 0)
        self.gridLayout = QtWidgets.QGridLayout(eslestirmesonuc)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(eslestirmesonuc)
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(eslestirmesonuc)
        QtCore.QMetaObject.connectSlotsByName(eslestirmesonuc)


    #Takım sayısının yarısı kadar sonuç alacağımızdan ötürü takımisimleri ikiye böldük
    # random komutu ile rastgele birbiri ile eşleştirdik
    #Daha önceden seçtiğimiz takım isimlerini tekrar seçmemek dahaoncesecilen listesi ve while döngüleri oluşturduk

        matches = tournament.MatchTeams()

        for match in matches:
            
            firstTeam = match.firstTeam
            secondTeam = match.secondTeam

            memberCountIndicator = ' (' + ('1' if not isTeam else str(firstTeam.memberCount)) + ' Kişi)'
            text =  firstTeam.name + (memberCountIndicator if isTeam else '') + ' VS ' + secondTeam.name + (memberCountIndicator if isTeam else '')

            label = QtWidgets.QLabel(eslestirmesonuc)
            label.setText(text)
            self.gridLayout.addWidget(label)



    
    









                
                
                
        




    def retranslateUi(self, eslestirmesonuc):
        _translate = QtCore.QCoreApplication.translate
        eslestirmesonuc.setWindowTitle(_translate("eslestirmesonuc", "Eşleştirme Sonucu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    eslestirmesonuc = QtWidgets.QWidget()
    ui = Ui_eslestirmesonuc()
    ui.setupUi(eslestirmesonuc)
    eslestirmesonuc.show()
    sys.exit(app.exec_())
