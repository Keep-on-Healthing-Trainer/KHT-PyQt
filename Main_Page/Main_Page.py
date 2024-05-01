import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import requests
url = {url/exercise/uuid}
data = {
    "count": 13
}
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {token}"
}

print(url)
print(headers)
print(data)

response = requests.post(url, headers=headers, json=data)
print(response.text)

js = response.json

form_class = uic.loadUiType("Main_Page_UI.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
