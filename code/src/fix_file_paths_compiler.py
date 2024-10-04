import sys
from pathlib import Path

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', Path(__file__).parent)
    base_path = Path(base_path) if not isinstance(base_path, Path) else base_path
    return (base_path / relative_path).resolve()