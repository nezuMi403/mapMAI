from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scatter import ScatterPlane
from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 360)
Config.set('graphics', 'height', 640)

class MainApp(App):
    cur_img_path = 'assets/sprites/GUK/GUKV2.png'


    def build(self):
        main_wig = ScatterPlane(scale=1.5)
        main_wig.pos = (0, 0)
        main_wig.scale_max=5
        main_wig.scale_min=1.5
        img_map = Image(source=self.cur_img_path, pos=(0, 0))
        img_map.size = (360, 360)
        img_map.pos = ((360-img_map.width)//2, (640-img_map.height)//2)


        label1 = Label(text='Теремок', color=(0, 0, 0, 1))
        label1.pos = (230, 260)

        main_wig.add_widget(img_map)
        main_wig.add_widget(label1)


        return main_wig


if __name__ == '__main__':
    MainApp().run()