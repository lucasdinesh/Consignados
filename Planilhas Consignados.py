import sys
from designeconsignados import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
import getpass
from main2 import executa
from threading import Thread
from contador import Informacoes


class Consignado(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnenviarnumero.clicked.connect(self.receber_id)
        self.selectbutton.clicked.connect(self.seleciona_arquivo)
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.id = ''
        self.nome_arquivo = ''
        self.caminho_arquivo = ''

    def receber_id(self):
        try:
            self.id = self.inputAbrirArquivo.text()
            self.nome_arquivo = self.getnomearquivo.text()
            print(self.id, self.nome_arquivo)
            Thread(target=executa, args=(self.id, self.nome_arquivo, self.caminho_arquivo, self.checkBox.isChecked())).start()
        except Exception as error:
            print("Erro ao receber o id:", error)

    def seleciona_arquivo(self):
        try:
            self.caminho_arquivo, _ = QFileDialog.getOpenFileName(
                self.centralwidget,
                "Selecionar",
                r'/Users/' + getpass.getuser() + f'/Desktop/',
                options=QFileDialog.DontUseNativeDialog
            )
            self.labelarquivosexistente.setText(self.caminho_arquivo)
            informacoes = Informacoes()
            self.inputAbrirArquivo.setText(informacoes.get_id(self.caminho_arquivo))
            self.getnomearquivo.setText((informacoes.get_nomearquivo(self.caminho_arquivo)))
        except Exception as error:
            print("Erro ao selecionar arquivo", error)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Consignado()
    novo.show()
    qt.exec_()