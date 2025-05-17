import os
from PIL import Image, ImageOps, ImageFilter
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QFileDialog, QListWidget, QMessageBox
workdir = ''

class ImageProcessor():
    def __init__(self):
        self.filename = None
        self.image = None
        self.dir = None
        self.save_dir = 'Modefied/'

    def loadImage(self, filename):
        self.filename = filename
        self.dir = workdir
        image_path = os.path.join(self.dir, self.filename)
        self.image = Image.open(image_path)

    def showImage(self, path):
        pixmapimage = QPixmap(path)
        label_width = Kartinka.width()
        label_heigth = Kartinka.height()
        scaled_pixmad = pixmapimage.scaled(label_width, label_heigth, Qt.KeepAspectRatio)
        Kartinka.setPixmap(scaled_pixmad)
        Kartinka.setVisible(True)

    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
    
    def do_bw(self):
        if spisok_cartinok.selectedItems():
            self.image = ImageOps.grayscale(self.image)
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('VENOM')
            error_win.exec()

    def do_levo(self):
        if spisok_cartinok.selectedItems():
            self.image = self.image.rotate(90)
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('VENOM')
            error_win.exec()

    def do_pravo(self):
        if spisok_cartinok.selectedItems():
            self.image = self.image.rotate(-90)
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('VENOM')
            error_win.exec()

    def do_mirror(self):
        if spisok_cartinok.selectedItems():
            self.image = ImageOps.mirror(self.image)
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('VENOM')
            error_win.exec()

    def do_shapen(self):
        if spisok_cartinok.selectedItems():
            try:
                self.image = self.image.filter(ImageFilter.SHARPEN)
            except:
                error_win = QMessageBox()
                error_win.setText('CARNAGE')
                error_win.exec()
            
            
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir, self.filename)
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('VENOM')
            error_win.exec()
    

workimage = ImageProcessor()

def showChosenImage():
    if spisok_cartinok.currentRow() >= 0:
        filename = spisok_cartinok.currentItem().text()
        workimage.loadImage(filename)
        image_path = os.path.join(workimage.dir, filename)
        workimage.showImage(image_path)           



def chooseWorkDir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files,extensions):
    result = []
    for filename in files:
        for extension in extensions:
            if filename.endswith(extension):
                result.append(filename)
    return result


def showFilenamesList():
    chooseWorkDir()
    extensions = ['.jpg', '.fpeg', '.png', '.gif']
    files = os.listdir(workdir)
    files = filter(files, extensions)
    spisok_cartinok.clear()
    spisok_cartinok.addItems(files)





main_app = QApplication([])
main_win = QWidget()
main_win.resize(700, 500)
main_win.setWindowTitle('Easy Editor')
papka = QPushButton('Папка')
spisok_cartinok = QListWidget()
Kartinka = QLabel('Картинка')
levo = QPushButton('Лево')
pravo = QPushButton('Право')
zerkalo = QPushButton('Зеркало')
rezkost = QPushButton('Резкость')
chb = QPushButton('Ч/Б')


Glavnaya = QHBoxLayout()
gor = QHBoxLayout()
ver1 = QVBoxLayout()
ver2 = QVBoxLayout()

gor.addWidget(levo)
gor.addWidget(pravo)
gor.addWidget(zerkalo)
gor.addWidget(rezkost)
gor.addWidget(chb)

ver1.addWidget(papka)
ver1.addWidget(spisok_cartinok)
ver2.addWidget(Kartinka)

ver2.addLayout(gor)
Glavnaya.addLayout(ver1)
Glavnaya.addLayout(ver2)
main_win.setLayout(Glavnaya)


papka.clicked.connect(showFilenamesList)
chb.clicked.connect(workimage.do_bw)
levo.clicked.connect(workimage.do_levo)
pravo.clicked.connect(workimage.do_pravo)
zerkalo.clicked.connect(workimage.do_mirror)
rezkost.clicked.connect(workimage.do_shapen)

spisok_cartinok.currentRowChanged.connect(showChosenImage)


main_win.show()
main_app.exec_()