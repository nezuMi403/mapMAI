# search_screen.py
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle

# from code.navigation_data import ALL_POINTS


class SearchScreen(Screen):
    def __init__(self, graph, **kwargs):
        super().__init__(**kwargs)
        self.start_point = None
        self.end_point = None
        self._create_ui()

        self.graph = graph
        self.all_points = self.graph.get_all_points()

    def _create_ui(self):
        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_bg, pos=self._update_bg)

        r, g, b = 116, 133, 250

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Заголовок
        title = Label(text='Построение маршрута', font_size='24sp', size_hint_y=0.1,
                      color=(0, 0, 0, 1))
        layout.add_widget(title)

        # Поля выбора точек
        points_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=0.3)

        # Стартовая точка
        start_layout = BoxLayout(orientation='vertical', spacing=10)
        start_layout.add_widget(Label(text='Стартовая точка:', size_hint_y=0.3,
                                      color=(0, 0, 0, 1)))
        self.start_input = TextInput(
            text='Не выбрано',
            readonly=True,
            size_hint_y=0.6,
            #background_color=(r/255.0, g/255.0, b/255.0, 1)
        )
        start_btn = Button(text='Выбрать старт', on_press=self.show_points_list_start,
                           background_color=(r/255.0, g/255.0, b/255.0, 1),
                           background_normal='',
                           background_down=''
                           )
        start_layout.add_widget(self.start_input)
        start_layout.add_widget(start_btn)
        points_layout.add_widget(start_layout)

        # Конечная точка
        end_layout = BoxLayout(orientation='vertical', spacing=10)
        end_layout.add_widget(Label(text='Конечная точка:', size_hint_y=0.3,
                                    color=(0, 0, 0, 1)))
        self.end_input = TextInput(
            text='Не выбрано',
            readonly=True,
            size_hint_y=0.6,
            #background_color=(r/255.0, g/255.0, b/255.0, 1)
        )
        end_btn = Button(text='Выбрать конец', on_press=self.show_points_list_end,
                         background_color=(r/255.0, g/255.0, b/255.0, 1),
                         background_normal='',
                         background_down=''
                         )
        end_layout.add_widget(self.end_input)
        end_layout.add_widget(end_btn)
        points_layout.add_widget(end_layout)
        layout.add_widget(points_layout)

        txg = Label(text='', font_size='12sp', size_hint_y=0.1)
        layout.add_widget(txg)
        # Кнопка построения маршрута
        build_btn = Button(
            text='Построить маршрут',
            on_press=self.build_route,
            size_hint_y=0.1,
            background_color=(r/255.0, g/255.0, b/255.0, 1),
            background_normal='',
            background_down=''
        )
        layout.add_widget(build_btn)

        # Кнопка назад
        back_btn = Button(
            text='Отмена',
            on_press=self.go_back,
            size_hint_y=0.05,
            background_color=(r/255.0, g/255.0, b/255.0, 1),
            background_normal='',
            background_down=''
        )
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def _update_bg(self, instance, value):
        self.bg_rect.size = instance.size
        self.bg_rect.pos = instance.pos

    def show_points_list_start(self, instance):
        """Показать список точек для выбора стартовой точки"""
        self._show_points_list(is_start=True)

    def show_points_list_end(self, instance):
        """Показать список точек для выбора конечной точки"""
        self._show_points_list(is_start=False)

    def _show_points_list(self, is_start=True):
        """Показать всплывающее окно со списком точек"""
        # Создаем layout для popup
        popup_layout = BoxLayout(orientation='vertical', spacing=10)

        # Заголовок
        title = Label(text='Выберите точку:', size_hint_y=0.1)
        popup_layout.add_widget(title)

        # ScrollView со списком точек
        scroll = ScrollView()
        points_layout = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None)
        points_layout.bind(minimum_height=points_layout.setter('height'))

        # Добавляем кнопки для каждой точки
        for point in self.all_points:
            btn = Button(
                text=f"{point['name']} ({point['building']}, этаж {point['level']})",
                size_hint_y=None,
                height=40,
                on_press=lambda instance, p=point, start=is_start: self._select_point(p, start)
            )
            points_layout.add_widget(btn)

        scroll.add_widget(points_layout)
        popup_layout.add_widget(scroll)

        # Кнопка отмены
        cancel_btn = Button(text='Назад', size_hint_y=0.1)
        popup_layout.add_widget(cancel_btn)

        # Создаем popup
        popup = Popup(
            title='',
            content=popup_layout,
            size_hint=(0.9, 0.8),
            auto_dismiss=True
        )

        cancel_btn.on_press = popup.dismiss

        popup.open()

    def _select_point(self, point, is_start):
        """Выбрать точку и обновить интерфейс"""
        if is_start:
            self.start_point = point
            self.start_input.text = f"{point['name']} ({point['building']}, этаж {point['level']})"
        else:
            self.end_point = point
            self.end_input.text = f"{point['name']} ({point['building']}, этаж {point['level']})"

        # Закрываем все открытые popup
        for child in self.children[:]:
            if isinstance(child, Popup):
                child.dismiss()

    def build_route(self, instance):
        """Построить маршрут и перейти на карту"""
        if not self.start_point or not self.end_point:
            self._show_error("Выберите стартовую и конечную точки")
            return

        # Сохраняем точки в глобальные параметры
        self.manager.params['start_point'] = self.start_point
        self.manager.params['end_point'] = self.end_point

        # Определяем, на какой экран карты переходить
        target_screen = self.start_point['building']

        # Переходим на экран карты
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = target_screen

    def _show_error(self, message):
        """Показать сообщение об ошибке"""
        popup = Popup(
            title='Ошибка',
            content=Label(text=message),
            size_hint=(0.7, 0.3),
            auto_dismiss=True
        )
        popup.open()

    def go_back(self, instance):
        """Возврат в меню"""
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'menu'

    def on_enter(self):
        """Вызывается при входе на экран"""
        # Сбрасываем выбранные точки при каждом входе
        self.start_point = None
        self.end_point = None
        self.start_input.text = 'Не выбрано'
        self.end_input.text = 'Не выбрано'