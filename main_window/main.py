from kivy.app import App

from kivy.uix.button import Button  # простой виджет кнопки
from kivy.uix.label import Label  # виджет текстового окна
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

from kivy.config import Config  # для настроек параметров окна

Width, Height = 960, 540

Config.set('graphics', 'resisable', 0)  # установили значение изменения размеров окна на 0
Config.set('graphics', 'width', Width)  # установили ширину
Config.set('graphics', 'height', Height)  # установили высоту


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
        self.scatter = Scatter(
            size_hint=(None, None),
            do_rotation=True,  # разрешить вращение
            do_scale=True,  # разрешить масштабирование
            do_translation=True  # разрешить перемещение
        )
        bl = BoxLayout(orientation="vertical", padding=25)
        bl2 = BoxLayout(orientation="vertical", size_hint=(1, .8))
        self.lb1 = Label(text="1029381029381023", size_hint=(1, .1), font_size=20, halign="center",
                         text_size=(Width - 50, Height * 0.1 - 10), valign="center", color=(255, 255, 255))
        self.im_Map = Image(source='GUKB2.jpg', size_hint=(1, .8))
        self.text_inp = TextInput(
            hint_text='Куда Вам нужно?',
            size_hint=(1, None),
            height=40,
            multiline=False
        )

        self.scatter.size = self.im_Map.size
        self.scatter.add_widget(self.im_Map)

        bl2.add_widget(self.scatter)

        bl.add_widget(bl2)
        bl.add_widget(self.text_inp)
        bl.add_widget(Button(text="7", font_size=10, on_press=self.add_number, size_hint=(1, .1)))

        return bl


if __name__ == '__main__':
    Calculator().run()
