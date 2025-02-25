import sys

from PyQt6.QtGui import QPixmap, qRgba
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QRadioButton, QButtonGroup, QPushButton
import requests

PG_UP = 16777238
PG_DOWN = 16777239
RIGHT = 16777236
LEFT = 16777234
DOWN = 16777237
UP = 16777235

APIKEY = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
MAP_API_SERVER = "https://static-maps.yandex.ru/v1"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 600, 450)
        self.setWindowTitle("Карты")
        self.setUpUI()
        self.setUpMapParams()
        self.updateMapImage()

    def setUpMapParams(self):
        self.zoom = 15
        self.l0 = 37.530887
        self.l1 = 55.703118
        self.map_image_size = (600, 450)

    def setUpUI(self):
        self.image = QLabel(self)
        self.image.setGeometry(0, 0, 600, 450)
        self.theme_group = QButtonGroup()
        self.dark_theme_button = QPushButton("Темная тема")
        self.dark_theme_button.move(800, 300)
        self.white_theme_button = QRadioButton("Светлая тема")
        self.theme_group.addButton(self.dark_theme_button, 1)
        self.theme_group.addButton(self.white_theme_button, 2)
        self.theme_group.buttonClicked.connect(self.onThemeChange)

    def onThemeChange(self):
        pass

    def getImage(self):
        map_params = {
            "ll": f"{self.l0},{self.l1}",
            "size": f"{self.map_image_size[0]},{self.map_image_size[1]}",
            "z": f"{self.zoom}",
            "apikey": APIKEY,
        }

        response = requests.get(MAP_API_SERVER, params=map_params)
        with open("map.png", "wb") as file:
            file.write(response.content)

    def updatePixmap(self):
        self.image.setPixmap(QPixmap("map.png"))

    def updateMapImage(self):
        self.getImage()
        self.updatePixmap()

    def keyPressEvent(self, event):
        key = event.key()

        if key == PG_UP:
            if self.zoom <= 21:
                self.zoom += 1
        elif key == PG_DOWN:
            if self.zoom >= 0:
                self.zoom -= 1
        elif key == RIGHT:
            if self.l0 <= 180:
                self.l0 += 0.026
        elif key == LEFT:
            if self.l0 >= -180:
                self.l0 -= 0.026
        elif key == DOWN:
            if self.l1 >= -90:
                self.l1 -= 0.011
        elif key == UP:
            if self.l1 <= 90:
                self.l1 += 0.011

        self.updateMapImage()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
