class GameSettings:
    resolution: tuple[int, int]
    volume: float
    fullscreen: bool

    display_width: int = None
    display_height: int = None

    X0: int = 0
    Y0: int = 0

    @staticmethod
    def calculate_x0_y0():
        if not GameSettings.fullscreen:
            GameSettings.X0, GameSettings.Y0 = 0, 0
            return
        GameSettings.X0 = (GameSettings.display_width - GameSettings.resolution[0]) // 2
        GameSettings.Y0 = (GameSettings.display_height - GameSettings.resolution[1]) // 2
