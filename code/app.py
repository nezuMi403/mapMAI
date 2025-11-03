from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scatter import ScatterPlane
from kivy.config import Config
from kivy.metrics import dp
from kivy.uix.widget import Widget

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 360)
Config.set('graphics', 'height', 640)

class MainApp(App):
    cur_img_path = 'assets/sprites/GUK/GUKV2.png'


    def build(self):
        main_wig = Widget()
        scatter_plane = ScatterPlane(scale=1.5)
        scatter_plane.pos = (0, 0)
        scatter_plane.scale_max=5
        scatter_plane.scale_min=1.5
        img_map = Image(source=self.cur_img_path, pos=(0, 0), mipmap=True)
        img_map.size = (360, 360)
        img_map.pos = ((360-img_map.width)//2, (640-img_map.height)//2)

        # Шакалы шакальные
        label1 = Label(
            text='Теремок',
            color=(0, 0, 0, 1),
            font_size='12sp',
            size_hint=(None, None),
            shorten=True,
            mipmap=True
        )
        label1.pos = (230, 260)
        label1.font_name = 'Arial'

        scatter_plane.add_widget(img_map)
        scatter_plane.add_widget(label1) # добавление шакальных шакалов

        main_wig.add_widget(scatter_plane)


        return main_wig


if __name__ == '__main__':
    MainApp().run()