from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.config import Config
from kivy.graphics import Color, Rectangle  # Импортируем для работы с цветом

Width, Height = 960, 540

Config.set('graphics', 'resisable', 0)
Config.set('graphics', 'width', Width)
Config.set('graphics', 'height', Height)


class Calculator(App):
    def add_number(self, instance):
        self.text += instance.text
        if self.text == '0':
            self.text = ""
        self.lb1.text = self.text

    def add_operation(self, instance):
        if self.text and self.text[-1] in "*-+/":
            self.text = self.text[:len(self.text) - 1] + instance.text
        elif self.text:
            self.text += instance.text
        self.text = self.text.replace("X", "*")
        self.lb1.text = self.text

    def eval_res(self, instance):
        try:
            self.lb1.text = str(eval(self.text))
            self.text = ""
        except Exception:
            self.lb1.text = "Error"
            self.text = ""

    def clear(self, instance):
        self.text = ""
        self.lb1.text = '0'

    def build(self):
        self.text = ""

        # Создаем главный layout с белым фоном
        main_layout = BoxLayout(orientation="vertical", padding=25)

        # Устанавливаем белый фон
        with main_layout.canvas.before:
            Color(1, 1, 1, 1)  # Белый цвет (RGB: 1,1,1, альфа: 1)
            self.rect = Rectangle(size=main_layout.size, pos=main_layout.pos)

        # Обновляем размер прямоугольника при изменении размера layout
        main_layout.bind(size=self._update_rect, pos=self._update_rect)

        self.scatter = Scatter(
            size_hint=(None, None),
            do_rotation=False,
            do_scale=True,
            do_translation=True
        )
        bl2 = BoxLayout(orientation="vertical", size_hint=(1, .8))
        self.lb1 = Label(text="1029381029381023", size_hint=(1, .1), font_size=20, halign="center",
                         text_size=(Width - 50, Height * 0.1 - 10), valign="center",
                         color=(0, 0, 0))  # Изменил цвет текста на черный
        self.im_Map = Image(source='GUKB2.jpg', size_hint=(1, .8))
        self.text_inp = TextInput(
            hint_text='Куда Вам нужно?',
            size_hint=(1, None),
            height=40,
            multiline=False,
            background_color=(1, 1, 1, 1)  # Белый фон для TextInput
        )

        self.scatter.size = self.im_Map.size
        self.scatter.add_widget(self.im_Map)

        bl2.add_widget(self.scatter)

        main_layout.add_widget(bl2)
        main_layout.add_widget(self.text_inp)
        main_layout.add_widget(Button(text="7", font_size=10, on_press=self.add_number, size_hint=(1, .1)))

        return main_layout

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


if __name__ == '__main__':
    Calculator().run()
