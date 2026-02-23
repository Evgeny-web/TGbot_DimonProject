from pathlib import Path


class ProjectPaths:
    """Синглтон для управления путями проекта"""

    def __init__(self):
        self.root = Path(__file__).parent.parent  # Поднимаемся из utils в корень

    @property
    def media(self) -> Path:
        return self.root / "media"

    @property
    def handlers(self) -> Path:
        return self.root / "handlers"

    def get_media(self, subdir: str, filename: str) -> Path:
        return self.media / subdir / filename

    def exists(self, path: Path) -> bool:
        return path.exists()


# Создаем глобальный экземпляр
Project_Path = ProjectPaths()