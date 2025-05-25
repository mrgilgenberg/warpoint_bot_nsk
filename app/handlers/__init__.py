from importlib import import_module
from os.path import dirname
from pathlib import Path


def load_handlers(folders: list[str]) -> None:
    for folder in folders:
        modules = Path(dirname(__file__), folder).glob('*.py')
        modules = [f.stem for f in modules if f.is_file() and f.name != '__init__.py']
        modules.sort()

        for module in modules:
            import_module(f'{__name__}.{folder}.{module}')
