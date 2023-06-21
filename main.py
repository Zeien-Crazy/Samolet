import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import QtWidgets, QtGui

import random as r
from transliterate import translit, get_available_language_codes
import deployModel.script as gb

from UIv1 import Ui_MainWindow
from UIv2 import Ui_Form

class SecondWindow(Ui_Form, QtWidgets.QWidget):
    def __init__(self, theme=False):
        super(SecondWindow,self).__init__()
        self.setupUi(self)

        self.setFixedSize(QSize(400, 500))
        self.setWindowIcon(QtGui.QIcon(':/newPrefix/icon_image.jpg'))
        self.label.setVisible(False)

        if(theme == True):
            self.Background_image.setPixmap(QtGui.QPixmap(":/newPrefix/Form2_Dark.png"))
        else:
            self.Background_image.setPixmap(QtGui.QPixmap(":/newPrefix/Form2.png"))


class MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):

    isForm = False
    isDarkTheme = False

    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)

        # self.windowTitle("Калькулятор стоймости квартиры")
        self.setFixedSize(QSize(950, 600))
        self.setWindowIcon(QtGui.QIcon(':/newPrefix/icon_image.jpg'))
        self.Line_Button.setVisible(False)


        self.w = SecondWindow(theme=self.isDarkTheme)
        
        self.a2 = self.TextBox_City
        self.a3 = self.TextBox_Street
        self.a4 = self.TextBox_Floor
        self.a5 = self.TextBox_Year_Construction
        self.a6 = self.TextBox_Number_Floors
        self.a7 = self.TextBox_Number_Rooms
        self.a8 = self.TextBox_General
        self.a9 = self.TextBox_Residential_rea
        self.a10 = self.TextBox_Kitchen

        self.a4.setValidator(QIntValidator())
        self.a5.setValidator(QIntValidator())
        self.a6.setValidator(QIntValidator())
        self.a7.setValidator(QIntValidator())
        self.a8.setValidator(QIntValidator())
        self.a9.setValidator(QIntValidator())
        self.a10.setValidator(QIntValidator())

        city_value = QCompleter([
            'Москва',
            'Апрелевка',
            'Балашиха' ,
            'Бронницы',
            'Верея',
            'Видное',
            'Волоколамск',
            'Воскресенск',
            'Высоковск',
            'Голицыно',
            'Дзержинский',
            'Дмитров',
            'Долгопрудный',
            'Домодедово',
            'Дрезна',
            'Дубна',
            'Егорьевск',
            'Жуковский',
            'Зарайск',
            'Звенигород',
            'Ивантеевка',
            'Истра',
            'Кашира' ,
            'Климовск',
            'Клин',
            'Коломна',
            'Королев',
            'Котельники',
            'Красмоармейск',
            'Красногорск',
            'Краснозаводск',
            'Краснознаменск',
            'Кубинка',
            'Куровское',
            'Ликино-Дулево',
            'Лобня',
            'Лосино-Петровский',
            'Луховицы',
            'Лыткарино',
            'Люберцы',
            'Можайск',
            'Мытищи',
            'Наро-Фоминск',
            'Ногинск',
            'Одинцово',
            'Озеры',
            'Орехово-Зуево',
            'Павловский Посад',
            'Пересвет',
            'Подольск',
            'Протвино',
            'Пушкино',
            'Пущино',
            'Раменское',
            'Реутов',
            'Рошаль',
            'Руза',
            'Сергиев Посад',
            'Серпухов',
            'Солнечногорск',
            'Старая Купавна',
            'Ступино',
            'Талдом',
            'Фрязино',
            'Химки',
            'Хотьково',
            'Черноголовка' ,
            'Чехов',
            'Шатура',
            'Щелково',
            'Электрогорск',
            'Электросталь',
            'Электроугли',
            'Юбилейный',
            'Яхрома',
        ])

        district = QCompleter([
            'Академический',
            'Алексеевский',
            'Алтуфьевский',
            'Арбат',
            'Аэропорт',
            'Бабушкинский',
            'Басманный',
            'Беговой',
            'Бескудниковский',
            'Бибирево',
            'Бирюлёво Восточное',
            'Бирюлёво Западное',
            'Богородское',
            'Братеево',
            'Бутово Северное',
            'Бутово Южное',
            'Бутырский',
            'Вешняки',
            'Внуково',
            'Войковский',
            'Восточный',
            'Выхино-Жулебино',
            'Гагаринский',
            'Головинский',
            'Гольяново',
            'Даниловский',
            'Дегунино Восточное',
            'Дегунино Западное',
            'Дмитровский',
            'Донской',
            'Дорогомилово',
            'Замоскворечье',
            'Зюзино',
            'Зябликово',
            'Ивановское',
            'Измайлово Восточное',
            'Измайлово',
            'Измайлово Северное',
            'Капотня',
            'Коньково',
            'Коптево',
            'Косино-Ухтомский',
            'Котловка',
            'Красносельский',
            'Крылатское',
            'Крюково',
            'Кузьминки',
            'Кунцево',
            'Куркино',
            'Левобережный',
            'Лефортово',
            'Лианозово',
            'Ломоносовский',
            'Лосиноостровский',
            'Люблино',
            'Марфино',
            'Марьина роща',
            'Марьино',
            'Матушкино',
            'Медведково Северное',
            'Медведково Южное',
            'Метрогородок',
            'Мещанский',
            'Митино',
            'Можайский',
            'Молжаниновский',
            'Москворечье-Сабурово',
            'Нагатино-Садовники',
            'Нагатинский затон',
            'Нагорный',
            'Некрасовка',
            'Нижегородский',
            'Ново-Переделкино',
            'Новогиреево',
            'Новокосино',
            'Обручевский',
            'Орехово-Борисово Северное',
            'Орехово-Борисово Южное',
            'Останкинский',
            'Отрадное',
            'Очаково-Матвеевское',
            'Перово',
            'Печатники',
            'Покровское-Стрешнево',
            'Преображенское',
            'Пресненский',
            'Проспект Вернадского',
            'Раменки',
            'Ростокино',
            'Рязанский',
            'Савёлки',
            'Савёловский',
            'Свиблово',
            'Северный',
            'Силино',
            'Сокол',
            'Соколиная гора',
            'Сокольники',
            'Солнцево',
            'Старое Крюково',
            'Строгино',
            'Таганский',
            'Тверской',
            'Текстильщики',
            'Тёплый Стан',
            'Тимирязевский',
            'Тропарёво-Никулино',
            'Тушино Северное',
            'Тушино Южное',
            'Филёвский парк',
            'Фили-Давыдково',
            'Хамовники',
            'Ховрино',
            'Хорошёво-Мневники',
            'Хорошёвский',
            'Царицыно',
            'Черёмушки',
            'Чертаново Северное',
            'Чертаново Центральное',
            'Чертаново Южное',
            'Щукино',
            'Южнопортовый',
            'Якиманка',
            'Ярославский',
            'Ясенево',
        ])

        self.a2.setCompleter(city_value)
        self.a3.setCompleter(district)

        self.Calculate_Button.clicked.connect(self.ButtonClick)
        self.a2.textChanged.connect(self.UpTextA2)
        self.a3.textChanged.connect(self.UpTextA3)
        # self.a3.focusInEvent.connect(self.textEneble)
        self.Clear_Button.clicked.connect(self.ClearForm)

        self.w.Confirm_Button.clicked.connect(self.Info)

        self.pushButton.clicked.connect(self.secretDark)

        print(get_available_language_codes())

    def textEneble(self):
        if(self.a2.text() != "Москва"):
            self.a3.setText(self.a2.text())
            self.a3.setEnabled(False)
        else:
            self.a3.setEnabled(True)
                                    

    def ClearForm(self):
        self.a2.clear()
        self.a3.clear()
        self.a4.clear()
        self.a5.clear()
        self.a6.clear()
        self.a7.clear()
        self.a8.clear()
        self.a9.clear()
        self.a10.clear()
        self.label.setText("0 руб. /М²")
        self.label_2.setText("0 руб.")

    def secretDark(self):
        if(self.isDarkTheme == False):
            self.Background_image.setPixmap(QtGui.QPixmap(":/newPrefix/Form1_Dark.png"))
            self.isDarkTheme = True
        else:
            self.Background_image.setPixmap(QtGui.QPixmap(":/newPrefix/Form1.png"))
            self.isDarkTheme = False

    def ButtonClick(self):
        try:
            if (int(self.a4.text()) < 0):
                self.a4.setText(str(int(self.a4.text()) * (-1)))

            if (int(self.a5.text()) < 0):
                self.a5.setText(str(int(self.a5.text()) * (-1)))

            if (int(self.a6.text()) < 0):
                self.a6.setText(str(int(self.a6.text()) * (-1)))

            if (int(self.a7.text()) < 0):
                self.a7.setText(str(int(self.a7.text()) * (-1)))

            if (int(self.a8.text()) < 0):
                self.a8.setText(str(int(self.a8.text()) * (-1)))

            if (int(self.a9.text()) < 0):
                self.a9.setText(str(int(self.a9.text()) * (-1)))

            if (int(self.a10.text()) < 0):
                self.a10.setText(str(int(self.a10.text()) * (-1)))

            if (self.isForm != True):
                self.w.show()
            else:
                self.Info()
        except BaseException:
            dlg = CustomDialog()
            dlg.exec()

    def UpTextA2(self):
        text = self.a2.text()
        if(text != ""):
            self.a2.setText(text[0].upper() + text[1:])

    def UpTextA3(self):
        text = self.a3.text()
        if(text != ""):
            self.a3.setText(text[0].upper() + text[1:])

    def Info(self):

        if(self.w.TextBox_Number.text() != ""):
            self.isForm = True

            self.b1 = translit(value=str(self.a2.text()).lower(), language_code='ru', reversed=True)
            self.b2 = translit(value=str(self.a3.text()).lower(), language_code='ru', reversed=True)

            self.res = gb.handler(city=self.b1, floor=self.a4.text(), floors_count=self.a6.text(), rooms_count=self.a7.text(), total_meters=float(self.a8.text()), year_of_construction=int(self.a5.text()), living_meters=float(self.a9.text()), kitchen_meters=float(self.a10.text()), district=self.b2)

            self.label.setText(str(self.res) + " руб. /М²")
            self.label_2.setText(str(self.res * int(self.a7.text())) + " руб.")
            self.Line_Button.setVisible(True)

            self.w.close()
        else:
            self.w.label.setVisible(True)


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ошибка!")

        QBtn = QDialogButtonBox.StandardButton.Ok

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Вы заполнили не все поля, пожалуйста, заполните их.")
        message.setStyleSheet("font-size: 50 px;")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

import images.images as images

if __name__ =='__main__':
    app = QtWidgets.QApplication(sys.argv)
    mywindow = MainWindow()
    mywindow.show()
    sys.exit(app.exec())