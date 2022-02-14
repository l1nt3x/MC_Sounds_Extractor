import json
import os
import shutil
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

from MCSE_UI import Ui_MCSE


class MCSE(QMainWindow, Ui_MCSE):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1080, 180)
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        self.mc_dir = 'NODIR'
        self.out_dir = 'NODIR'
        self.versions = []
        self.mc_dir_lineEdit.setReadOnly(True)
        self.out_dir_lineEdit.setReadOnly(True)

        self.mc_dir_pushButton.clicked.connect(self.browse_mc_dir)
        self.out_dir_pushButton.clicked.connect(self.browse_out_dir)
        self.extract_pushButton.clicked.connect(self.extract)

        self.ver_comboBox.addItem('No version')

    def browse_mc_dir(self):
        self.mc_dir = QFileDialog.getExistingDirectory(self, 'Browse Minecraft directory', '')
        self.mc_dir_lineEdit.setText(self.mc_dir)
        try:
            self.versions = os.listdir(f'{self.mc_dir}/assets/indexes')
        except Exception as e:
            self.statusBar.showMessage('Please browse your Minecraft directory!')
            self.statusBar.setStyleSheet("background-color : pink")
            return False
        for i in range(len(self.versions)):
            self.versions[i] = self.versions[i][:-5]
        self.ver_comboBox.addItems(self.versions)
        self.mc_dir = 'NODIR'

    def browse_out_dir(self):
        self.out_dir = QFileDialog.getExistingDirectory(self, 'Browse output directory', '')
        self.out_dir_lineEdit.setText(self.out_dir)

    def check(self):
        if self.mc_dir == 'NODIR':
            self.statusBar.showMessage('Please browse your Minecraft directory!')
            self.statusBar.setStyleSheet("background-color : pink")
            return False
        if not os.path.exists(self.mc_dir):
            self.statusBar.showMessage('Please browse your Minecraft directory!')
            self.statusBar.setStyleSheet("background-color : pink")
            return False
        if self.out_dir == 'NODIR':
            self.statusBar.showMessage('Please browse your output directory!')
            self.statusBar.setStyleSheet("background-color : pink")
            return False
        if self.ver_comboBox.currentText() == 'No version':
            self.statusBar.showMessage('Please choose Minecraft version!')
            self.statusBar.setStyleSheet("background-color : pink")
            return False
        if not os.path.isfile(f"{self.mc_dir}/assets/indexes/{self.ver_comboBox.currentText() + '.json'}"):
            self.statusBar.showMessage('Please choose Minecraft version!')
            self.statusBar.setStyleSheet("background-color : pink")
            return False
        return True

    def extract(self):
        if self.check():
            mc_assets = f'{self.mc_dir}/assets'
            mc_version = self.ver_comboBox.currentText() + '.json'
            out_path = self.out_dir
            mc_object_index = f"{mc_assets}/indexes/{mc_version}"
            mc_object_path = f"{mc_assets}/objects"
            with open(mc_object_index, "r") as read_file:
                data = json.load(read_file)
                sounds = {k: v["hash"] for (k, v) in data["objects"].items() if k[-3:] == 'ogg'}
                for fpath, fhash in sounds.items():
                    src_fpath = os.path.normpath(f"{mc_object_path}/{fhash[:2]}/{fhash}")
                    dest_fpath = os.path.normpath(f"{out_path}/sounds/{fpath}").replace('\sounds\minecraft\sounds', '')
                    os.makedirs(os.path.dirname(dest_fpath), exist_ok=True)
                    shutil.copyfile(src_fpath, dest_fpath)
            self.statusBar.showMessage('Done!')
            self.statusBar.setStyleSheet("background-color : green")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MCSE()
    ex.show()
    sys.exit(app.exec_())
