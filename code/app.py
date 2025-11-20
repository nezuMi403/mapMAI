from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

from code.images_paths import ImagesPaths
from code.map_screen import MapScreen


Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 360)
Config.set('graphics', 'height', 640)

class MainScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.params = {
            'cur_build': None
        }

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
        self.manager.transition = SlideTransition(
            direction='right',  # 'left', 'right', 'up', 'down'
            duration=0.5  # длительность в секундах
        )
        self.manager.current = 'guka'

    def set_gukb(self, instance):
        return
        self.manager.transition = SlideTransition(
            direction='right',  # 'left', 'right', 'up', 'down'
            duration=0.5  # длительность в секундах
        )
        self.manager.current = 'gukb'

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
        screen_manager = MainScreenManager()

        guka_screen = MapScreen(cur_build=ImagesPaths.GUKA, name='guka')
        # gukb_screen = MapScreen(cur_build=ImagesPaths.GUKB, name='gukb')
        gukv_screen = MapScreen(cur_build=ImagesPaths.GUKV, name='gukv')
        menu_screen = MenuScreen(name='menu')

        outside_screen = MapScreen(cur_build=ImagesPaths.OUTSIDE, name='outside')

        screen_manager.add_widget(menu_screen)
        screen_manager.add_widget(guka_screen)
        #screen_manager.add_widget(gukb_screen)
        screen_manager.add_widget(gukv_screen)
        screen_manager.add_widget(outside_screen)

        screen_manager.current = 'menu'

        return screen_manager
