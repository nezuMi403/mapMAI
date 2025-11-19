from idlelib.mainmenu import menudefs

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scatter import ScatterPlane
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.graphics import (Color, Line, Rectangle, Ellipse)

from code.images_paths import ImagesPaths


Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 360)
Config.set('graphics', 'height', 640)


class MapScreen(Screen):
    def __init__(self, cur_build, **kwargs):
        super().__init__(**kwargs)

        self.cur_level = min(list(cur_build.keys()))
        self.cur_build = cur_build
        self.cur_img_path = self.cur_build[self.cur_level]

        self.main_wig = Widget()
        self.ux = ScatterPlane(scale=1.5,
                          do_translation=False,
                          do_rotation=False,
                          do_scale=False)

        self.scatter_plane = ScatterPlane(scale=1.5)
        self.scatter_plane.pos = (0, 0)
        self.scatter_plane.scale_max = 5
        self.scatter_plane.scale_min = 1.5

        self.img_map = Image(source=self.cur_img_path, pos=(0, 0), mipmap=True)
        self.img_map.size = (360, 360)
        self.img_map.pos = ((360 - self.img_map.width) // 2, (640 - self.img_map.height) // 2)

        self.load_img()


        d = 0.8
        self.img_up = Image(
            source=ImagesPaths.BUTTONS['up'],
            pos=(360 - 40, 640 - 200),
            size=(50 * d, 50 * d),
            mipmap=True,
        )

        self.button_up = Button(
            on_press=self.up,
            size=self.img_up.size, pos=self.img_up.pos,
            background_color=(255, 0, 0, 0),
            background_normal=''
        )
        self.img_dw = Image(
            source=ImagesPaths.BUTTONS['down'],
            pos=(360 - 40, 640 - 250),
            size=(50 * d, 50 * d),
            mipmap=True,
        )
        self.button_down = Button(
            on_press=self.down,
            size=self.img_dw.size, pos=self.img_dw.pos,
            background_color=(0, 255, 0, 0),
            background_normal=''
        )
        self.img_pl = Image(
            source=ImagesPaths.BUTTONS['plus'],
            pos=(360 - 40, 640 - 330),
            size=(50 * d, 50 * d),
            mipmap=True,
        )
        self.button_plus = Button(on_press=self.plus,
                                  size=self.img_pl.size, pos=self.img_pl.pos,
                                  background_color=(0, 0, 0, 0),
                                  background_normal=''
                                  )
        self.img_mn = Image(
            source=ImagesPaths.BUTTONS['minus'],
            pos=(360 - 40, 640 - 380),
            size=(50 * d, 50 * d),
            mipmap=True,
        )
        self.button_minus = Button(on_press=self.minus,
                                   size=self.img_mn.size, pos=self.img_mn.pos,
                                   color=(0, 0, 0, 0),
                                   background_color=(0, 0, 0, 0),
                                   background_normal=''
                                   )


        self.img_menu = Image(
            source=ImagesPaths.BUTTONS['menu'],
            pos=(360 - 320, 640 - 40),
            size=(50 * d, 50 * d),
            mipmap=True,
        )

        self.button_menu = Button(on_press=self.go_to_menu_screen,
                                  size=self.img_menu.size, pos=self.img_menu.pos,
                                  background_color=(0, 0, 0, 0),
                                  background_normal=''
                                  )

        self.img_back = Image(
            source=ImagesPaths.BUTTONS['back'],
            pos=(360 - 270, 640 - 40),
            size=(50 * d, 50 * d),
            mipmap=True,
        )
        self.button_back = Button(on_press=self.back,
                                  size=self.img_back.size, pos=self.img_back.pos,
                                  background_color=(0, 0, 0, 0),
                                  background_normal=''
                                  )

        self.add_ux()
        self.update_widgets()

    def load_img(self):
        all_arrs = {}

        all_arrs.update(ImagesPaths.BUTTONS)
        """all_arrs.update(ImagesPaths.GUKA)
        for item in all_arrs:
            path = all_arrs[item]
            try:
                self.img_map.source = path
                self.scatter_plane.add_widget(self.img_map)
                self.scatter_plane.clear_widgets()

                print(f"Successfully loaded: {path}")
            except Exception as e:
                print(f"Failed to load {path}: {e}")
        all_arrs.update(ImagesPaths.GUKB)
        for item in all_arrs:
            path = all_arrs[item]
            try:
                self.img_map.source = path
                self.scatter_plane.add_widget(self.img_map)
                self.scatter_plane.clear_widgets()

                print(f"Successfully loaded: {path}")
            except Exception as e:
                print(f"Failed to load {path}: {e}")"""
        all_arrs.update(ImagesPaths.GUKV)

        # Загружаем каждое изображение
        for item in all_arrs:
            path = all_arrs[item]
            try:
                self.img_map.source = path
                self.scatter_plane.add_widget(self.img_map)
                self.scatter_plane.clear_widgets()

                print(f"Successfully loaded: {path}")
            except Exception as e:
                print(f"Failed to load {path}: {e}")

        self.scatter_plane.clear_widgets()
        self.img_map.source = self.cur_img_path
        self.scatter_plane.add_widget(self.img_map)

    def add_ux(self):
        self.ux.add_widget(self.img_up)
        self.ux.add_widget(self.img_dw)
        self.ux.add_widget(self.img_pl)
        self.ux.add_widget(self.img_mn)

        self.ux.add_widget(self.button_plus)
        self.ux.add_widget(self.button_minus)
        self.ux.add_widget(self.button_up)
        self.ux.add_widget(self.button_down)

        self.ux.add_widget(self.img_menu)
        self.ux.add_widget(self.button_menu)
        self.ux.add_widget(self.img_back)
        self.ux.add_widget(self.button_back)

    def update_widgets(self):
        self.scatter_plane.pos = (0, 0)
        self.scatter_plane.rotation = 0
        self.scatter_plane.scale = 1.5
        self.scatter_plane.clear_widgets()
        # self.ux.clear_widgets()
        self.main_wig.pos=(0, 0)

        self.main_wig.clear_widgets()
        self.clear_widgets()

        self.scatter_plane.pos = (0, 0)
        self.scatter_plane.rotation = 0
        self.scatter_plane.scale = 1.5

        with self.canvas.before:
            Color(1, 1, 1, 1)
            Rectangle(size=(360*2, 640*2), pos=self.pos)

        self.scatter_plane.add_widget(self.img_map)

        self.main_wig.add_widget(self.scatter_plane)
        self.main_wig.add_widget(self.ux)

        self.add_widget(self.main_wig)

    def up(self, instance):
        arr_levels = list(self.cur_build.keys())
        arr_levels.sort()

        if self.cur_level < max(arr_levels):
            self.cur_level = arr_levels[arr_levels.index(self.cur_level)+1]

        self.cur_img_path = self.cur_build[self.cur_level]

        self.img_map.source = self.cur_img_path

        self.update_widgets()

    def down(self, instance):
        arr_levels = list(self.cur_build.keys())
        arr_levels.sort()

        if self.cur_level > min(arr_levels):
            self.cur_level = arr_levels[arr_levels.index(self.cur_level) - 1]

        self.cur_img_path = self.cur_build[self.cur_level]

        self.img_map.source = self.cur_img_path

        self.update_widgets()

    def plus(self, instance):
        # Запоминаем текущий масштаб и позицию
        old_scale = self.scatter_plane.scale
        old_pos = self.scatter_plane.pos

        # Вычисляем новый масштаб
        new_scale = min(self.scatter_plane.scale_max, old_scale + 0.2)

        # Если масштаб изменился
        if new_scale != old_scale:
            # Вычисляем центр экрана
            center_x = 360 * 1.5 / 2
            center_y = 640 * 1.5 / 2

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
        new_scale = min(self.scatter_plane.scale_max, old_scale - 0.2)

        # Если масштаб изменился
        if new_scale != old_scale:
            # Вычисляем центр экрана
            center_x = 360 * 1.5 / 2
            center_y = 640 * 1.5 / 2

            # Вычисляем смещение для масштабирования к центру
            dx = (center_x - old_pos[0]) * (new_scale / old_scale - 1)
            dy = (center_y - old_pos[1]) * (new_scale / old_scale - 1)

            # Применяем новый масштаб и позицию
            self.scatter_plane.scale = new_scale
            self.scatter_plane.pos = (old_pos[0] - dx, old_pos[1] - dy)

    def back(self, instance):
        if self.cur_build is ImagesPaths.OUTSIDE:
            self.go_to_menu_screen(instance)
            return
        self.go_to_outsude(instance)

    def go_to_menu_screen(self, instance):
        self.manager.transition = SlideTransition(
            direction='right',  # 'left', 'right', 'up', 'down'
            duration=0.5  # длительность в секундах
        )
        self.manager.current = 'menu'

    def go_to_outsude(self, instance):
        self.manager.transition = SlideTransition(
            direction='right',  # 'left', 'right', 'up', 'down'
            duration=0.5  # длительность в секундах
        )
        self.manager.current = 'outside'

"""class OutsideScreen(MapScreen):
    def __init__(self, cur_build**kwargs):
        super().__init__(cur_build=ImagesPaths.OUTSIDE, **kwargs)"""

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Создаем layout для второго экрана
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Добавляем виджеты
        label = Label(text='Карта МАИ', font_size='30sp')
        button1 = Button(
            text='Открыть карту',
            size_hint_y=0.3,
            on_press=self.set_outside
        )

        button2 = Button(
            text='ГУК А',
            size_hint_y=0.3,
            on_press=self.set_guka
        )
        button3 = Button(
            text='ГУК Б',
            size_hint_y=0.3,
            on_press=self.set_gukb
        )
        button4 = Button(
            text='ГУК В',
            size_hint_y=0.3,
            on_press=self.set_gukv,
        )

        layout.add_widget(label)
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)


        # Добавляем layout в экран
        self.add_widget(layout)

    def set_outside(self, instance):
        self.manager.transition = SlideTransition(
            direction='right',  # 'left', 'right', 'up', 'down'
            duration=0.5  # длительность в секундах
        )
        self.manager.current = 'outside'

    def set_guka(self, instance):
        return
        self.manager.transition = SlideTransition(
            direction='right',  # 'left', 'right', 'up', 'down'
            duration=0.5  # длительность в секундах
        )
        self.manager.current = 'gukv'

    def set_gukb(self, instance):
        return
        self.manager.transition = SlideTransition(
            direction='right',  # 'left', 'right', 'up', 'down'
            duration=0.5  # длительность в секундах
        )
        self.manager.current = 'gukv'

    def set_gukv(self, instance):
        self.manager.transition = SlideTransition(
            direction='right',  # 'left', 'right', 'up', 'down'
            duration=0.5  # длительность в секундах
        )
        self.manager.current = 'gukv'

    def go_to_map_screen(self, instance):
        self.manager.transition = SlideTransition(
            direction='left',  # 'left', 'right', 'up', 'down'
            duration=0.5  # длительность в секундах
        )
        self.manager.current = 'gukv'

class MainApp(App):
    def build(self):
        screen_manager = ScreenManager()

        gukv_screen = MapScreen(cur_build=ImagesPaths.GUKV, name='gukv')
        menu_screen = MenuScreen(name='menu')

        outside_screen = MapScreen(cur_build=ImagesPaths.OUTSIDE, name='outside')

        screen_manager.add_widget(menu_screen)
        screen_manager.add_widget(gukv_screen)
        screen_manager.add_widget(outside_screen)

        screen_manager.current = 'menu'

        return screen_manager
