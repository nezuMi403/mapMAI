from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label

class SimpleScreen(Screen):
    def __init__(self, name, text, button_text, target_screen, **kwargs):
        super().__init__(name=name, **kwargs)
        self.add_widget(Label(text=text))
        self.add_widget(Button(
            text=button_text,
            on_press=lambda x: setattr(self.manager, 'current', target_screen)
        ))

class SimpleApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SimpleScreen('first', 'Экран 1', 'Вперед →', 'second'))
        sm.add_widget(SimpleScreen('second', 'Экран 2', '← Назад', 'first'))
        return sm

SimpleApp().run()