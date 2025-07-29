import os
import shutil

def add_to_startup(file_path=None):
    if file_path is None:
        file_path = os.path.realpath(__file__)
    startup_path = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup")
    shutil.copy(file_path, startup_path)
