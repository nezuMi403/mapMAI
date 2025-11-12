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


"""class ScatterLoader:
    def __init__(self):
        self.all = {}
    
    @staticmethod
    def new_scatter(path):
        scatter_plane = ScatterPlane(scale=1.5)
        scatter_plane.pos = (0, 0)
        scatter_plane.scale_max = 5
        scatter_plane.scale_min = 1.5

        img_map = Image(source=path, pos=(0, 0), mipmap=True)
        img_map.size = (360, 360)
        img_map.pos = ((360 - img_map.width) // 2, (640 - img_map.height) // 2)

        scatter_plane.add_widget(img_map)
        return scatter_plane
        
    def load(self):
        # Собираем все пути
        all_arrs = {}
        all_arrs.update(ImagesPaths.BUTTONS)
        all_arrs.update(ImagesPaths.GUKA)
        all_arrs.update(ImagesPaths.GUKB)
        all_arrs.update(ImagesPaths.GUKV)


        # Загружаем каждое изображение
        for item in all_arrs:
            path = all_arrs[item]
            try:
                self.all[item] = self.new_scatter(path)
                print(f"Successfully loaded: {path}")
            except Exception as e:
                print(f"Failed to load {path}: {e}")"""


class OutsideScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MapScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cur_level = 2
        self.cur_build = ImagesPaths.GUKV
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
        """self.scatter_loader = ScatterLoader()
        self.scatter_loader.load()

        self.scatter_plane = self.scatter_loader.all[self.cur_img_path]"""

        self.add_ux()
        self.update_widgets()

    def load_img(self):
        all_arrs = {}
        all_arrs.update(ImagesPaths.BUTTONS)
        all_arrs.update(ImagesPaths.GUKA)
        all_arrs.update(ImagesPaths.GUKB)
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

    def update_widgets(self):
        self.scatter_plane.pos = (0, 0)
        self.scatter_plane.rotation = 0
        self.scatter_plane.translation = (0, 0)
        self.scatter_plane.scale = 1.5
        self.scatter_plane.clear_widgets()
        # self.ux.clear_widgets()
        self.main_wig.clear_widgets()
        self.clear_widgets()

        with self.canvas.before:
            Color(1, 1, 1, 1)
            Rectangle(size=(360*2, 640*2), pos=self.pos)

        self.scatter_plane.add_widget(self.img_map)

        """self.ux.add_widget(self.img_up)
        self.ux.add_widget(self.img_dw)
        self.ux.add_widget(self.img_pl)
        self.ux.add_widget(self.img_mn)

        self.ux.add_widget(self.button_plus)
        self.ux.add_widget(self.button_minus)
        self.ux.add_widget(self.button_up)
        self.ux.add_widget(self.button_down)"""

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
        new_scale = max(self.scatter_plane.scale_min, old_scale - 0.2)

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


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Создаем layout для второго экрана
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Добавляем виджеты
        label = Label(text='Карта МАИ', font_size='30sp')
        button = Button(
            text='Открыть карту',
            size_hint_y=0.3,
            on_press=self.go_to_first_screen
        )

        layout.add_widget(label)
        layout.add_widget(button)

        # Добавляем layout в экран
        self.add_widget(layout)

    def go_to_first_screen(self, instance):
        # Переключаемся на первый экран
        self.manager.transition = SlideTransition(
            direction='down',  # 'left', 'right', 'up', 'down'
            duration=0.3  # длительность в секундах
        )
        self.manager.current = 'map'

class MainApp(App):
    def build(self):
        screen_manager = ScreenManager()

        first_screen = MapScreen(name='map')
        second_screen = MenuScreen(name='menu')

        screen_manager.add_widget(first_screen)
        screen_manager.add_widget(second_screen)

        screen_manager.current = 'menu'

        return screen_manager
