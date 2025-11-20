# map_screen.py
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scatter import ScatterPlane
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.graphics import Color, Rectangle

from code.images_paths import ImagesPaths


class MapScreen(Screen):
    def __init__(self, cur_build, **kwargs):
        super().__init__(**kwargs)
        self.cur_build = cur_build
        self.cur_level = min(list(cur_build.keys()))
        self._setup_ui()

    def _setup_ui(self):
        # Создаем белый фон один раз
        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_bg, pos=self._update_bg)

        self.main_wig = Widget()
        self.ux = ScatterPlane(scale=1.5, do_translation=False, do_rotation=False, do_scale=False)

        self.scatter_plane = ScatterPlane(scale=1.5, scale_max=5, scale_min=1.5)
        self.img_map = Image(source=self.cur_build[self.cur_level], mipmap=True)
        self._update_image_position()

        self.scatter_plane.add_widget(self.img_map)
        self._create_controls()
        self._assemble_ui()

    def _update_bg(self, instance, value):
        self.bg_rect.size = instance.size
        self.bg_rect.pos = instance.pos

    def _update_image_position(self):
        self.img_map.size = (360, 360)
        self.img_map.pos = ((360 - self.img_map.width) // 2, (640 - self.img_map.height) // 2)

    def _create_controls(self):
        d = 0.8
        controls_data = [
            ('up', (360 - 40, 640 - 200), self.up),
            ('down', (360 - 40, 640 - 250), self.down),
            ('plus', (360 - 40, 640 - 330), self.plus),
            ('minus', (360 - 40, 640 - 380), self.minus),
            ('menu', (360 - 320, 640 - 40), self.go_to_menu_screen),
            ('back', (360 - 270, 640 - 40), self.back)
        ]

        for img_type, pos, callback in controls_data:
            img = Image(
                source=ImagesPaths.BUTTONS[img_type],
                pos=pos,
                size=(50 * d, 50 * d),
                mipmap=True,
            )
            btn = Button(
                on_press=callback,
                size=img.size,
                pos=img.pos,
                background_color=(0, 0, 0, 0),
                background_normal=''
            )
            self.ux.add_widget(img)
            self.ux.add_widget(btn)

    def _assemble_ui(self):
        self.main_wig.add_widget(self.scatter_plane)
        self.main_wig.add_widget(self.ux)
        self.add_widget(self.main_wig)

    def _change_level(self, direction):
        levels = sorted(self.cur_build.keys())
        current_index = levels.index(self.cur_level)

        new_index = current_index + direction
        if 0 <= new_index < len(levels):
            self.cur_level = levels[new_index]
            self.img_map.source = self.cur_build[self.cur_level]
            self.scatter_plane.scale = 1.5
            self.scatter_plane.pos = (0, 0)
            self.scatter_plane.rotation = 0

    def up(self, instance):
        self._change_level(1)

    def down(self, instance):
        self._change_level(-1)

    def _zoom(self, factor):
        old_scale = self.scatter_plane.scale
        new_scale = max(self.scatter_plane.scale_min,
                        min(self.scatter_plane.scale_max, old_scale + factor))

        if new_scale != old_scale:
            center_x, center_y = 360 * 1.5 / 2, 640 * 1.5 / 2
            old_pos = self.scatter_plane.pos

            dx = (center_x - old_pos[0]) * (new_scale / old_scale - 1)
            dy = (center_y - old_pos[1]) * (new_scale / old_scale - 1)

            self.scatter_plane.scale = new_scale
            self.scatter_plane.pos = (old_pos[0] - dx, old_pos[1] - dy)

    def plus(self, instance):
        self._zoom(0.2)

    def minus(self, instance):
        self._zoom(-0.2)

    def back(self, instance):
        if self.cur_build is ImagesPaths.OUTSIDE:
            self.go_to_menu_screen(instance)
        else:
            self.go_to_outsude(instance)

    def go_to_menu_screen(self, instance):
        self.manager.transition = SlideTransition(direction='right', duration=0.2)
        self.manager.current = 'menu'

    def go_to_outsude(self, instance):
        self.manager.transition = SlideTransition(direction='right', duration=0.2)
        self.manager.current = 'outside'