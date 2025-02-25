import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel
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
        self.spn0 = 0.02
        self.spn1 = 0.02
        self.map_image_size = (600, 450)

    def setUpUI(self):
        self.image = QLabel(self)
        self.image.setGeometry(0, 0, 600, 450)

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
            self.pageUpPressed()
            if self.zoom <= 21:
                self.zoom += 1
        elif key == PG_DOWN:
            self.pageDownPressed()
            if self.zoom >= 0:
                self.zoom -= 1
        elif key == RIGHT:
            self.rightPressed()
        elif key == LEFT:
            self.leftPressed()
        elif key == DOWN:
            self.downPressed()
        elif key == UP:
            self.upPressed()

        self.updateMapImage()

    def updateMap(self):
        pass

    def upPressed(self):
        pass

    def downPressed(self):
        pass

    def leftPressed(self):
        pass

    def rightPressed(self):
        pass

    def leftPressed(self):
        pass

    def pageDownPressed(self):
        pass

    def pageUpPressed(self):
        pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
