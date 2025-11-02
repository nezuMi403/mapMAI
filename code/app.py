from kivy.app import App
from kivy.config import Config
from kivy.uix.label import Label

Config.set('graphics', 'resisable', 0)
Config.set('graphics', 'width', 360)
Config.set('graphics', 'height', 640)

class MainApp(App):
    def build(self):
        return Label(text='Hello World')
        pass