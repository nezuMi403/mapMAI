class SceneManager:
    """
    Класс, управляющий всеми сценами
    """

    def __init__(self, app):
        self.app = app  # Хранит в себе app, чтобы у нас был доступ к нему из любой функции
        self.current_scene = None  # Текущая сцена
        self.scenes = {}  # {"test": TestScene, ...}

    def add_scene(self, name, scene_class):
        """Добавление сцены"""
        self.scenes[name] = scene_class

    def switch_to(self, name):
        """Переключение сцен"""
        if name in self.scenes:
            self.current_scene = self.scenes[name]
            self.current_scene.on_enter()  # Инициализация сцены