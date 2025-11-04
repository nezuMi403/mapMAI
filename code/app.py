from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scatter import ScatterPlane
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.metrics import dp
from kivy.uix.widget import Widget

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 360)
Config.set('graphics', 'height', 640)

class MainApp(App):
    cur_img_path = 'assets/sprites/GUK/V/GUKV2.png'
    img_map = Image()
    scatter_plane = ScatterPlane()

    def build(self):
        main_wig = Widget()
        ux = ScatterPlane(scale=1.5,
                          do_translation=False,
                          do_rotation=False,
                          do_scale=False)
        self.scatter_plane = ScatterPlane(scale=1.5)
        self.scatter_plane.pos = (0, 0)
        self.scatter_plane.scale_max=5
        self.scatter_plane.scale_min=1.5
        self.img_map = Image(source=self.cur_img_path, pos=(0, 0), mipmap=True)
        self.img_map.size = (360, 360)
        self.img_map.pos = ((360-self.img_map.width)//2, (640-self.img_map.height)//2)

        d = 0.8
        b_up = Image(
            source='assets/sprites/buttons/button_up.png',
            pos = (360-40, 640-200),
            size = (50*d, 50*d),
            mipmap=True,
        )
        b_dw = Image(
            source='assets/sprites/buttons/button_down.png',
            pos=(360 - 40, 640 - 250),
            size=(50*d, 50*d),
            mipmap=True,
        )
        b_pl = Image(
            source='assets/sprites/buttons/plus.png',
            pos=(360 - 40, 640 - 330),
            size=(50 * d, 50 * d),
            mipmap=True,
        )
        button_pl = Button(on_press=self.plus,
                           size=b_pl.size, pos=b_pl.pos,
                           background_color=(0, 0, 0, 0),
                           background_normal=''
                           )
        b_mn = Image(
            source='assets/sprites/buttons/minus.png',
            pos=(360 - 40, 640 - 380),
            size=(50 * d, 50 * d),
            mipmap=True,
        )
        button_mn = Button(on_press=self.minus,
                           size=b_mn.size, pos=b_mn.pos,
                           color=(0, 0, 0, 0),
                           background_color=(0, 0, 0, 0),
                           background_normal=''
                           )

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

        self.scatter_plane.add_widget(self.img_map)
        self.scatter_plane.add_widget(label1)

        ux.add_widget(b_up)
        ux.add_widget(b_dw)
        ux.add_widget(b_pl)
        ux.add_widget(b_mn)
        ux.add_widget(button_pl)
        ux.add_widget(button_mn)

        main_wig.add_widget(self.scatter_plane)
        main_wig.add_widget(ux)

        return main_wig

    def plus(self, instance):
        # Запоминаем текущий масштаб и позицию
        old_scale = self.scatter_plane.scale
        old_pos = self.scatter_plane.pos

        # Вычисляем новый масштаб
        new_scale = min(self.scatter_plane.scale_max, old_scale + 0.2)

        # Если масштаб изменился
        if new_scale != old_scale:
            # Вычисляем центр экрана
            center_x = 360*1.5 / 2
            center_y = 640*1.5 / 2

            # Вычисляем смещение для масштабирования к центру
            dx = (center_x - old_pos[0]) * (new_scale / old_scale - 1)
            dy = (center_y - old_pos[1]) * (new_scale / old_scale - 1)

            # Применяем новый масштаб и позицию
            self.scatter_plane.scale = new_scale
            self.scatter_plane.pos = (old_pos[0] - dx, old_pos[1] - dy)

    def minus(self, instance):
        # Запоминаем текущий масштаб и позицию
        old_scale = self.scatter_plane.scale
        old_pos = self.scatter_plane.pos

        # Вычисляем новый масштаб
        new_scale = max(self.scatter_plane.scale_min, old_scale - 0.2)

        # Если масштаб изменился
        if new_scale != old_scale:
            # Вычисляем центр экрана
            center_x = 360*1.5 / 2
            center_y = 640*1.5 / 2

            # Вычисляем смещение для масштабирования к центру
            dx = (center_x - old_pos[0]) * (new_scale / old_scale - 1)
            dy = (center_y - old_pos[1]) * (new_scale / old_scale - 1)

            # Применяем новый масштаб и позицию
            self.scatter_plane.scale = new_scale
            self.scatter_plane.pos = (old_pos[0] - dx, old_pos[1] - dy)

if __name__ == '__main__':
    MainApp().run()