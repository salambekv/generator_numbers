from random import randint

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox)

def get_number():
    rand1.setText(str(randint(1, 3)))
    rand2.setText(str(randint(1, 3)))
    if rand1.text() == rand2.text():
        answer = QMessageBox()
        answer.setText('Поздравляем')
        answer.move(190, 200)
        answer.exec()
    
app = QApplication([])
window = QWidget()
window.resize(250, 200)
window.move(150, 150)
window.setWindowTitle('Генератор чисел!')

line = QVBoxLayout()
line_hor = QHBoxLayout()

text = QLabel('Сгенерировать число:')
rand1 = QLabel('?')
rand2 = QLabel('?')
btn_OK = QPushButton('Нажать')

line_hor.addWidget(rand1, alignment=Qt.AlignCenter)
line_hor.addWidget(rand2, alignment=Qt.AlignCenter)

line.addWidget(text, alignment=Qt.AlignCenter)
line.addLayout(line_hor)
line.addWidget(btn_OK, alignment=Qt.AlignCenter)

btn_OK.clicked.connect(get_number)

window.setLayout(line)
window.show()
app.exec()