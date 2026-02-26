import os
from pathlib import Path

def remove_placeholder_files():
    for path in Path(".").rglob("REMOVE_ME"):
        path.unlink()

if __name__ == "__main__":
    remove_placeholder_files()
