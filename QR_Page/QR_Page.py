import sys, qrcode, requests, asyncio, websockets
import websocket, rel
from websocket import create_connection
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
from urllib.parse import urlparse, parse_qs

# url parsing
def get_query_string(url):
    response_url = urlparse(url)
    query_string = response_url.query
    parse_string = parse_qs(query_string)

    return parse_string

# qr
url = {base_url/exercise/qr}
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

# sessionId
parsingData = get_query_string(response.text)
sessionId = parsingData['sessionId'][0]

async def connect():
    async with websockets.connect({base_url/exercise}) as websocket:
       data = {
           "messageType": "ENTER",
           "sessionId": sessionId,
           "senderId": {GUI_UUID}
       }
       await websocket.send(data)
       websocket_response = await websocket.recv()
       print(websocket_response)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        super(MainWindow, self).__init__()

        loadUi("QR_Page_UI.ui", self)
        self.setWindowTitle("QR")

        pixmap = QPixmap("QR.png")
        self.imageLabel.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    asyncio.get_event_loop().run_until_complete(connect)
    # asyncio.run(connect())
    sys.exit(app.exec_())