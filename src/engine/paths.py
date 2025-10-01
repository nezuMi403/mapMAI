import sys
import os


def resource_path(relative_path):
    """Эта штука нужна чтобы при сборке ничего не ломалось"""
    """Получение абсолютного пути с учетом всех возможных вариантов сборки"""
    # Пробуем стандартный путь для PyInstaller
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
        path = os.path.join(base_path, relative_path)
        if os.path.exists(path):
            return path

    # Проверяем все возможные варианты путей
    possible_bases = [
        os.path.abspath("."),  # Текущая директория
        os.path.dirname(sys.executable),  # Директория с exe
        os.path.join(os.path.dirname(sys.executable), '_internal'),  # Для non-onefile
        os.path.join(sys._MEIPASS, '..') if hasattr(sys, '_MEIPASS') else None  # Для onefile
    ]

    for base in filter(None, possible_bases):
        path = os.path.join(base, relative_path)
        if os.path.exists(path):
            return path

    # Последняя попытка - убрать "../" из пути
    clean_path = relative_path.replace("../", "")
    for base in filter(None, possible_bases):
        path = os.path.join(base, clean_path)
        if os.path.exists(path):
            return path

    raise FileNotFoundError(
        f"Resource not found: {relative_path}\n"
        f"Checked paths: {[os.path.join(b or '', relative_path) for b in possible_bases if b]}\n"
        f"Current dir: {os.getcwd()}\n"
        f"Executable: {sys.executable}\n"
        f"_MEIPASS: {getattr(sys, '_MEIPASS', 'N/A')}"
    )
