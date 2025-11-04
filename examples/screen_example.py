from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import (
    SlideTransition, SwapTransition,
    FadeTransition, WipeTransition,
    FallOutTransition, RiseInTransition
)


# Первый экран
class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Создаем layout для первого экрана
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Добавляем виджеты
        label = Label(text='Это первый экран!', font_size='30sp')
        button = Button(
            text='Перейти на второй экран',
            size_hint_y=0.3,
            on_press=self.go_to_second_screen
        )

        layout.add_widget(label)
        layout.add_widget(button)

        # Добавляем layout в экран
        self.add_widget(layout)

    def go_to_second_screen(self, instance):
        # Переключаемся на второй экран
        self.manager.transition = SlideTransition(
            direction='up',  # 'left', 'right', 'up', 'down'
            duration=0.3  # длительность в секундах
        )
        self.manager.current = 'second'


# Второй экран
class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Создаем layout для второго экрана
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Добавляем виджеты
        label = Label(text='Это второй экран!', font_size='30sp')
        button = Button(
            text='Вернуться на первый экран',
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
        self.manager.current = 'first'


# Главное приложение
class MultiScreenApp(App):
    def build(self):
        # Создаем менеджер экранов
        screen_manager = ScreenManager()

        # Создаем экраны с именами
        first_screen = FirstScreen(name='first')
        second_screen = SecondScreen(name='second')

        # Добавляем экраны в менеджер
        screen_manager.add_widget(first_screen)
        screen_manager.add_widget(second_screen)

        # Устанавливаем текущий экран
        screen_manager.current = 'first'

        return screen_manager


# Запуск приложения
if __name__ == '__main__':
    MultiScreenApp().run()