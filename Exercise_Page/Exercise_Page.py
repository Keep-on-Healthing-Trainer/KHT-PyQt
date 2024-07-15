import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class FocusLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.default_style = self.styleSheet()
        self.setFixedSize(350, 350)

    def focusInEvent(self, event):
        self.setStyleSheet("border: 3px solid #0075FF;")
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        self.setStyleSheet(self.default_style)
        super().focusOutEvent(event)


class DirectionalFocusWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Directional Focus Widget')
        self.setGeometry(0, 0, 1920, 1080)  # 윈도우 크기 설정

        # 레이아웃 설정
        layout = QHBoxLayout()

        # 라벨 위젯 생성
        self.label1 = FocusLabel('Label 1')
        self.label2 = FocusLabel('Label 2')
        self.label3 = FocusLabel('Label 3')

        # 포커스 정책 설정
        self.label1.setFocusPolicy(Qt.StrongFocus)
        self.label2.setFocusPolicy(Qt.StrongFocus)
        self.label3.setFocusPolicy(Qt.StrongFocus)

        # 레이아웃에 라벨 추가
        layout.addWidget(self.label1)
        pixmap = QPixmap("pushup.jpg")
        self.label1.setPixmap(pixmap)
        layout.addWidget(self.label2)
        pixmap = QPixmap("situp.jpg")
        self.label2.setPixmap(pixmap)
        layout.addWidget(self.label3)
        pixmap = QPixmap("squat.png")
        self.label3.setPixmap(pixmap)

        self.setLayout(layout)

        # 기본 포커스 설정
        self.label1.setFocus()

    def keyPressEvent(self, event):
        # 현재 포커스 위젯 가져오기
        focused_widget = QApplication.focusWidget()

        if event.key() == Qt.Key_Left:
            self.moveFocus(focused_widget, -1)
        elif event.key() == Qt.Key_Right:
            self.moveFocus(focused_widget, 1)

    def moveFocus(self, current_widget, direction):
        # 위젯 목록
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
