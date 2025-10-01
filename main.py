# src/main.py
from src.engine.game import Game
from src.scenes.test_scene import TestScene


def main():
    game = Game()

    # Регистрация сцен
    game.scene_manager.add_scene("testscene", TestScene(game))

    # Стартовая сцена
    game.scene_manager.switch_to("testscene")

    game.run()

if __name__ == "__main__":
    main()
