from base.app import App
from base.test.test_scene import TestScene


def main():
    """Входная точка приложения"""
    app = App()  # Чтобы прочитать код класса зажми ctrl и кликни на класс

    app.scene_manager.add_scene("test", TestScene(app))  # Создаём тестовую сцену
    app.scene_manager.switch_to("test")  # Переключаемся на неё

    app.run()  # Запуск главного цикла приложения

if __name__ == '__main__':
    main()
