from kivy.uix.widget import Widget
from kivy.graphics import (Color, Line, Rectangle, Ellipse)
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window

class PaintWidget(Widget):
    def on_touch_down(self, touch):
        '''Срабатывает при нажатии мышкой или пальцем на экран, в touch хр-ся информация о мышке

           При помощи touch.id между методами для нажатий можно передавать(сохранять) информацию,
           в данном случае я сохраняю объект линии и при перемещении зажатой мышки я обновляю ее точки'''
        with self.canvas:
            Color(1, 0, 1, 1)
            rad = 30
            Ellipse(pos=(touch.x - rad / 2, touch.y - rad / 2), size=(rad, rad))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=15)

    def on_touch_move(self, touch):
        touch.ud['line'].points += (touch.x, touch.y)


class Painter_app(App):
    def build(self):
        self.id_img, self.id_screen = 1, 1 # для сохранения картинок
        main_widg = Widget() # внутри него разместим последовательно все - канву и кнопки
        self.painter = PaintWidget()

        '''Добавляем внутрь кнопки и канву, на канве рисуем'''
        main_widg.add_widget(self.painter)
        main_widg.add_widget(Button(text="Clear", on_press=self.clear, size=(200, 100), pos=(0, 0)))
        main_widg.add_widget(Button(text="Save", on_press=self.save, size=(200, 100), pos=(200, 0)))
        main_widg.add_widget(Button(text="Screenshot", on_press=self.screen, size=(200, 100), pos=(400, 0)))
        return main_widg

    def save(self, instance):
        '''Для сохранения картинки, без установки self.painter.size() у нас бы сохранялась только часть
           картинки размером 100*100
           Функция export_to_png позволяет экспортировать изображение виджета указанного размера в файл'''
        self.painter.size = (Window.size[0], Window.size[1])
        self.painter.export_to_png(f'image{self.id_img}.png')
        self.id_img += 1

    def screen(self, instance):
        '''Работает аналогично методу save, но сохраняет все окно, а не указанный виджет'''
        Window.screenshot(f'Screen{self.id_screen}.png')
        self.id_screen += 1

    def clear(self, instance):
        '''Метод канвы, просто очищает ее'''
        self.painter.canvas.clear()


if __name__ == '__main__':
    Painter_app().run()
