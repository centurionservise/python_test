import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
from PyQt5 import uic
from PyQt5 import QtWidgets
from Ui_test import Ui_MainWindow

# import design  # Это наш конвертированный файл дизайна

class SergWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в нашем файле ui файде
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.setWindowTitle("Hello world")
        # self.setWindowIcon()
        self.textEdit_1.setReadOnly(True)

        self.pushButton_1.clicked.connect(self.CopyText)  # Выполнить функцию browse_folder
                                                            # при нажатии кнопки

    def CopyText(self):
        self.textEdit_1.append(self.lineEdit_1.text())
        self.lineEdit_1.setText("SERG")
        # window.setWindowTitle("PyQt")
        pass


    def browse_folder(self):
        self.listWidget.clear()  # На случай, если в списке уже есть элементы
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории

        if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
            for file_name in os.listdir(directory):  # для каждого файла в директории
                self.listWidget.addItem(file_name)   # добавить файл в listWidget

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = SergWindow()  # Создаём объект класса SergWindow
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
    print("Buy-buy")

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()