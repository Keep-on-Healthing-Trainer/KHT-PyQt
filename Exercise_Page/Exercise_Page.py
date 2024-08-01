import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class FocusLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.default_style = self.styleSheet()
        self.setFixedSize(350, 350)
        self.setStyleSheet("""
            QLabel {
                background-color: white;
                border-radius: 30px;
            }
        """)

    def focusInEvent(self, event):
        self.setStyleSheet("""
            QLabel {
                background-color: white;
                border-radius: 30px;
                border: 3px solid #0075FF;
            }
        """)
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        self.setStyleSheet("""
            QLabel {
                background-color: white;
                border-radius: 30px;
            }
        """)
        super().focusOutEvent(event)

class DirectionalFocusWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Directional Focus Widget')
        self.setGeometry(0, 0, 1920, 1080)
        self.setStyleSheet("background-color: white;")

        layout = QHBoxLayout()

        self.label1 = FocusLabel('Label 1')
        self.label2 = FocusLabel('Label 2')
        self.label3 = FocusLabel('Label 3')

        self.label1.setFocusPolicy(Qt.StrongFocus)
        self.label2.setFocusPolicy(Qt.StrongFocus)
        self.label3.setFocusPolicy(Qt.StrongFocus)

        layout.addWidget(self.label1)
        pixmap = QPixmap("situp.jpg")
        self.label1.setPixmap(pixmap)
        layout.addWidget(self.label2)
        pixmap = QPixmap("squat.png")
        self.label2.setPixmap(pixmap)
        layout.addWidget(self.label3)
        pixmap = QPixmap("pushup.jpg")
        self.label3.setPixmap(pixmap)

        self.setLayout(layout)

        self.label1.setFocus()

    def keyPressEvent(self, event):
        # 현재 포커스 가져오기
        focused_widget = QApplication.focusWidget()

        if event.key() == Qt.Key_Left:
            self.moveFocus(focused_widget, -1)
        elif event.key() == Qt.Key_Right:
            self.moveFocus(focused_widget, 1)

    def moveFocus(self, current_widget, direction):
        widgets = [self.label1, self.label2, self.label3]

        if current_widget in widgets:
            current_index = widgets.index(current_widget)
            next_index = (current_index + direction) % len(widgets)
            widgets[next_index].setFocus()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DirectionalFocusWidget()
    window.show()
    sys.exit(app.exec_())
