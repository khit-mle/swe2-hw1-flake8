import shutil
from pathlib import Path


def clear_media_dir():
    """Clears the '../media/' directory."""

    media_dir = Path("../media")
    for p in media_dir.glob("*"):
        if p.is_file():
            p.unlink()
        elif p.is_dir():
            shutil.rmtree(p)


def perform_st_rerun_tasks():
    clear_media_dir()
