import subprocess
import sys
import os
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication,  QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import *
# probando subida github
class Consulta_apagado(QMainWindow):
    def __init__(self):
        super().__init__()
        # NUMERO 1/2
        nombre_archivo=self.resolver_ruta("apagadocom.ui")
        uic.loadUi(nombre_archivo, self)
        #uic.loadUi("C:/Users/Paul/Desktop/PROYECTOS INFORMATICOS/APAGADO COMP/apagadocom.ui", self)
        self.pushButton_iniciar.clicked.connect(self.turnoff)
        
    def turnoff(self):

        t=int(self.lineEdit_minutos.text())*60
        if t>1:
            subprocess.call("shutdown -s -t %d" %t)
            s= QMessageBox.question(self, "Mensaje", "¿Seguro quiere apagar la computadora?", QMessageBox.Yes, QMessageBox.No)
            if s == QMessageBox.No:
                subprocess.call("shutdown -a")
                QMessageBox.about(self, "INFORMACION","Apagado cancelado.") 
                self.lineEdit_minutos.setText("")
            else:
                QMessageBox.about(self, "INFORMACION","Apagado programado.") 
                self.close()

    # NUMERO 2/2

    def resolver_ruta(self,ruta_relativa):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, ruta_relativa)
        return os.path.join(os.path.abspath('.'), ruta_relativa)

if __name__ == "__main__":
    app=QApplication(sys.argv)
    QApplication.setAttribute(Qt.AA_DisableWindowContextHelpButton)  
    GUIde=Consulta_apagado()
    GUIde.show()
    sys.exit(app.exec_())