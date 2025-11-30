# app.py
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

from code.graph import Graph
from code.images_paths import ImagesPaths
from code.map_screen import MapScreen
from code.search_screen import SearchScreen

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 360)
Config.set('graphics', 'height', 640)
Window.size = (360, 640)


class MainScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.params = {
            #Тут хранятся глобальные переменные, доступные по всех экранах
            'cur_build': None,
            'start_point': None,
            'end_point': None
        }


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._create_ui()

    def _create_ui(self):
        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_bg, pos=self._update_bg)

        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
        r, g, b = 116, 133, 250
        widgets = [
            Label(text='Карта МАИ', font_size='40sp', color=(r/255.0, g/255.0, b/255.0, 1)),
            Button(
                text='Открыть карту',
                font_size='20sp',
                size_hint_y=0.3,
                on_press=self.set_outside,
                background_color=(r/255.0, g/255.0, b/255.0, 1),
                background_normal='',
                background_down='',

            ),
            Button(
                text='ГУК А',
                font_size='20sp',
                size_hint_y=0.3,
                on_press=self.set_guka,
                background_color=(r/255.0, g/255.0, b/255.0, 1),
                background_normal='',
                background_down=''
            ),
            Button(
                text='ГУК Б',
                font_size='20sp',
                size_hint_y=0.3,
                on_press=self.set_gukb,
                background_color=(r/255.0, g/255.0, b/255.0, 1),
                background_normal='',
                background_down=''
            ),
            Button(
                text='ГУК В',
                font_size='20sp',
                size_hint_y=0.3,
                on_press=self.set_gukv,
                background_color=(r/255.0, g/255.0, b/255.0, 1),
                background_normal='',
                background_down=''
            )
        ]

        for widget in widgets:
            layout.add_widget(widget)

        self.add_widget(layout)

    def _update_bg(self, instance, value):
        self.bg_rect.size = instance.size
        self.bg_rect.pos = instance.pos

    def _switch_screen(self, screen_name):
        self.manager.transition = SlideTransition(direction='right', duration=0.2)
        self.manager.current = screen_name

    def set_outside(self, instance):
        self._switch_screen('outside')

    def set_guka(self, instance):
        self._switch_screen('guka')

    def set_gukb(self, instance):
        return  # Раскомментируйте когда добавите экран ГУК Б
        self._switch_screen('gukb')

    def set_gukv(self, instance):
        self._switch_screen('gukv')


class MainApp(App):
    def build(self):
        screen_manager = MainScreenManager()

        graph = Graph()

        screens = [
            MenuScreen(name='menu'),
            MapScreen(graph=graph, cur_build=ImagesPaths.GUKA, name='guka'),
            # MapScreen(cur_build=ImagesPaths.GUKB, name='gukb'),
            MapScreen(graph=graph, cur_build=ImagesPaths.GUKV, name='gukv'),
            MapScreen(graph=graph, cur_build=ImagesPaths.OUTSIDE, name='outside'),

            SearchScreen(graph=graph, name='search'),
        ]

        for screen in screens:
            screen_manager.add_widget(screen)

        screen_manager.current = 'menu'
        return screen_manager