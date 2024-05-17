import sys, qrcode, requests
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi

url = {url/exercise/qr}
response = requests.get(url)
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 8,
    border = 4,
)
qr.add_data(response.text)
qr.make(fit = True)

img = qr.make_image(fill_color="black", back_color="white")
img.save({png})

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        loadUi("QR_Page_UI.ui", self)
        self.setWindowTitle("QR")

        pixmap = QPixmap("QR.png")
        self.imageLabel.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
