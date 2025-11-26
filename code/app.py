# app.py
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
#from kivy.core.window import Window

from code.images_paths import ImagesPaths
from code.map_screen import MapScreen
from code.navigation_data import NAVIGATION_DATA

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 360)
Config.set('graphics', 'height', 640)
#Window.size = (360, 640)


class MainScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.params = {'cur_build': None}


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._create_ui()

    def _create_ui(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        widgets = [
            Label(text='Карта МАИ', font_size='30sp'),
            Button(text='Открыть карту', size_hint_y=0.3, on_press=self.set_outside),
            Button(text='ГУК А', size_hint_y=0.3, on_press=self.set_guka),
            Button(text='ГУК Б', size_hint_y=0.3, on_press=self.set_gukb),
            Button(text='ГУК В', size_hint_y=0.3, on_press=self.set_gukv)
        ]

        for widget in widgets:
            layout.add_widget(widget)

        self.add_widget(layout)

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

        screens = [
            MapScreen(cur_build=ImagesPaths.GUKA, name='guka'),
            MapScreen(cur_build=ImagesPaths.GUKV, name='gukv'),
            MenuScreen(name='menu'),
            MapScreen(cur_build=ImagesPaths.OUTSIDE, name='outside')
        ]

        for screen in screens:
            # Передаем данные навигации каждому экрану
            if hasattr(screen, 'set_navigation_data'):
                screen.set_navigation_data(NAVIGATION_DATA)
            screen_manager.add_widget(screen)

        screen_manager.current = 'menu'
        return screen_manager