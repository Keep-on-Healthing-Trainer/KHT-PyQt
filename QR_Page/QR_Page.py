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
url = {url}
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
print(parsingData)

sessionId = parsingData['sessionId'][0]
print(sessionId)

#async def connect():
#    async with websockets.connect({url}) as websocket:
#        data = {
#            "messageType": "ENTER",
#            "sessionId": {sessionId},
#            "senderId": {senderId}
#        }
#        await websocket.send(data)
#        await websocket.send("hello")
#        websocket_response = await websocket.recv()
#        print(websocket_response)

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

    ws = websocket.create_connection({url})
    ws.recv()
    print("Sending 'Hello, World'...")
    ws.send("Hello, World")
    print("Sent")
    print("Receiving...")
    result = ws.recv()
    ws.close()
    # asyncio.get_event_loop().run_until_complete(connect())
    sys.exit(app.exec_())