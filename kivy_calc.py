from kivy.app import App

from kivy.uix.button import Button  # простой виджет кнопки
from kivy.uix.label import Label  # виджет текстового окна

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
# стоит посмотреть в видосе, определенный тип бокса, куда можно помещпть все что угодно

from kivy.config import Config  # для настроек параметров окна

Config.set('graphics', 'resisable', 0)  # установили значение изменения размеров окна на 0
Config.set('graphics', 'width', 400)  # установили ширину
Config.set('graphics', 'height', 500)  # установили высоту


class Calculator(App):  # создаем класс калькулятора
    def add_number(self, instance):  # функция обработки кнопки, instance содержит инф-ию о кнопке
        self.text += instance.text  # instance.text - текст кнопки
        if self.text == '0':
            self.text = ""
        self.lb1.text = self.text  # lb1.text - установить текст для текстового окна

    def add_operation(self, instance):  # работает аналогично add_number
        if self.text and self.text[-1] in "*-+/":
            self.text = self.text[:len(self.text) - 1] + instance.text
        elif self.text:
            self.text += instance.text
        self.text = self.text.replace("X", "*")
        self.lb1.text = self.text

    def eval_res(self, instance):  # работает аналогично двум функциям выше, добавил try чтобы ниче не вылетало
        try:
            self.lb1.text = str(eval(self.text))
            self.text = ""
        except Exception:
            self.lb1.text = "Error"
            self.text = ""

    def clear(self, instance):  # работает аналогично функциям выше
        self.text = ""
        self.lb1.text = '0'

    def build(self):  # основная функция класса, в ней добавляем объекты, размещаем их в окне
        self.text = ""
        bl = BoxLayout(orientation="vertical", padding=25)
        gl = GridLayout(cols=4, spacing=3, size_hint=(1, .7))
        '''BoxLayout - размещает добавленные в него объекты в колонну либо в строчку,
           задает им одинаковые параметры размеров, если не указать иначе
           
           GridLayout - размещает объекты в виде таблицы, количество колонок и строчек
           указывается в параметрах cols и spacing соответственно'''

        self.lb1 = Label(text="0", size_hint=(1, .3), font_size=40, halign="right",
                         text_size=(400 - 50, 500 * 0.4 - 50), valign="center")
        '''Label - виджет текстового поля, важные параметры:
           text - изначальный текст
           size_hint - размеры окна в процентном соотношении от бокса, в кот оно находится
           font_size - размер шрифта в пикселях
           halign - расположение текста в виджете относительно горизонтали
           text_size - размер допустимого пространства для текста
           valign - расположение текста относительно вертикали'''
        bl.add_widget(self.lb1)  # добавление виджета при помощи add_widget, работает для любых контейнеров

        '''Button - виджет кнопки, имеет те же базовые параметр как и все виджеты, отличие - 
           on_press - функция отклика при нажатии кнопки'''
        gl.add_widget(Button(text="7", font_size=30, on_press=self.add_number))
        gl.add_widget(Button(text="8", font_size=30, on_press=self.add_number))
        gl.add_widget(Button(text='9', font_size=30, on_press=self.add_number))
        gl.add_widget(Button(text='X', font_size=30, on_press=self.add_operation))
        gl.add_widget(Button(text="4", font_size=30, on_press=self.add_number))
        gl.add_widget(Button(text='5', font_size=30, on_press=self.add_number))
        gl.add_widget(Button(text='6', font_size=30, on_press=self.add_number))
        gl.add_widget(Button(text='-', font_size=30, on_press=self.add_operation))
        gl.add_widget(Button(text='1', font_size=30, on_press=self.add_number))
        gl.add_widget(Button(text='2', font_size=30, on_press=self.add_number))
        gl.add_widget(Button(text='3', font_size=30, on_press=self.add_number))
        gl.add_widget(Button(text='+', font_size=30, on_press=self.add_operation))
        gl.add_widget(Button(text='C', font_size=30, on_press=self.clear))
        gl.add_widget(Button(text="0", font_size=30, on_press=self.add_number))
        gl.add_widget(Button(text=".", font_size=30, on_press=self.add_number))
        gl.add_widget(Button(text="=", font_size=30, on_press=self.eval_res))

        bl.add_widget(gl)
        return bl


if __name__ == '__main__':
    Calculator().run()
