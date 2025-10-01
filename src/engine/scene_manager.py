class SceneManager:
    def __init__(self, game):
        self.game = game
        self.current_scene = None
        self.scenes = {}  # {"desktop": DesktopScene(self.game), ...}

    def add_scene(self, name, scene_class):
        self.scenes[name] = scene_class

    def switch_to(self, name):
        if name in self.scenes:
            self.current_scene = self.scenes[name]
            self.current_scene.on_enter()  # Инициализация сцены