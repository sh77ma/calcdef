# Импортируем библиотеку для создания графического интерфейса
from PyQt5 import QtCore, QtGui, QtWidgets

# Создаем класс для калькулятора
class Calculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Создаем интерфейс калькулятора
        self.initUI()

    def initUI(self):
        # Создаем кнопки для цифр
        self.button_0 = QtWidgets.QPushButton("0")
        self.button_1 = QtWidgets.QPushButton("1")
        self.button_2 = QtWidgets.QPushButton("2")
        self.button_3 = QtWidgets.QPushButton("3")
        self.button_4 = QtWidgets.QPushButton("4")
        self.button_5 = QtWidgets.QPushButton("5")
        self.button_6 = QtWidgets.QPushButton("6")
        self.button_7 = QtWidgets.QPushButton("7")
        self.button_8 = QtWidgets.QPushButton("8")
        self.button_9 = QtWidgets.QPushButton("9")

        # Создаем кнопки для операций
        self.button_add = QtWidgets.QPushButton("+")
        self.button_sub = QtWidgets.QPushButton("-")
        self.button_mul = QtWidgets.QPushButton("*")
        self.button_div = QtWidgets.QPushButton("/")
        self.button_equal = QtWidgets.QPushButton("=")

        # Создаем поле для вывода результата
        self.label = QtWidgets.QLabel("0")

        # Создаем layout для кнопок
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button_0)
        layout.addWidget(self.button_1)
        layout.addWidget(self.button_2)
        layout.addWidget(self.button_3)
        layout.addWidget(self.button_4)
        layout.addWidget(self.button_5)
        layout.addWidget(self.button_6)
        layout.addWidget(self.button_7)
        layout.addWidget(self.button_8)
        layout.addWidget(self.button_9)
        layout.addWidget(self.button_add)
        layout.addWidget(self.button_sub)
        layout.addWidget(self.button_mul)
        layout.addWidget(self.button_div)
        layout.addWidget(self.button_equal)

        # Устанавливаем layout для калькулятора
        self.setLayout(layout)

        # Подключаем сигналы к слотам
        self.button_0.clicked.connect(self.on_button_0_clicked)
        self.button_1.clicked.connect(self.on_button_1_clicked)
        self.button_2.clicked.connect(self.on_button_2_clicked)
        self.button_3.clicked.connect(self.on_button_3_clicked)
        self.button_4.clicked.connect(self.on_button_4_clicked)
        self.button_5.clicked.connect(self.on_button_5_clicked)
        self.button_6.clicked.connect(self.on_button_6_clicked)
        self.button_7.clicked.connect(self.on_button_7_clicked)
        self.button_8.clicked.connect(self.on_button_8_clicked)
        self.button_9.clicked.connect(self.on_button_9_clicked)
        self.button_add.clicked.connect(self.on_button_add_clicked)
        self.button_sub.clicked.connect(self.on_button_sub_clicked)
        self.button_mul.clicked.connect(self.on_button_mul_clicked)
        self.button_div.clicked.connect(self.on_button_div_clicked)
        self.button_equal.clicked.connect(self.on_button_equal_clicked)

    def on_button_0_clicked(self):
        # Добавляем цифру 0 к текущему значению
        self.label.setText(self.label.text() + "0")

    def on_button_1_clicked(self):
        # Добавляем цифру 1 к текущему значению
        self.label.setText(self.label.text() + "1")

    def on_button_2_clicked(self):
        # Добавляем цифру 2 к текущему значению
        self.label.setText(self.label.text() + "2")

    def on_button_3_clicked(self):
        # Добавляем цифру 3 к текущему значению
        self.label.setText(self.label.text() + "3")

    def on_button_4_clicked(self):
        # Добавляем цифру 4 к текущему значению
        self.label.setText(self.label.text() + "4")

    def on_button_5_clicked(self):
        # Добавляем цифру 5 к текущему значению
        self.label.setText(self.label.text() + "5")

    def on_button_6_clicked(self):
        # Добавляем цифру 6 к текущему значению
        self.label.setText(self.label.text() + "6")

    def on_button_7_clicked(self):
        # Добавляем цифру 7 к текущему значению
        self.label.setText(self.label.text() + "7")

    def on_button_8_clicked(self):
        # Добавляем цифру 8 к текущему значению
        self.label.setText(self.label.text() + "8")

    def on_button_9_clicked(self):
        # Добавляем цифру 9 к текущему значению
        self.label.setText(self.label.text() + "9")

    def on_button_add_clicked(self):
        # Добавляем операцию сложения к текущему значению
        self.label.setText(self.label.text() + "+")

    def on_button_sub_clicked(self):
        # Добавляем операцию вычитания к текущему значению
        self.label.setText(self.label.text() + "-")

    def on_button_mul_clicked(self):
        # Добавляем операцию умножения к текущему значению
        self.label.setText(self.label.text() + "*")

    def on_button_div_clicked(self):
        # Добавляем операцию деления к текущему значению
        self.label.setText(self.label.text() + "/")

    def on_button_equal_clicked(self):
        # Выполняем расчет и выводим результат
        try:
            result = eval(self.label.text())
            self.label.setText(str(result))
        except Exception as e:
            self.label.setText("Error")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec_()
