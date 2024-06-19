import sys
from cx_Freeze import setup, Executable

# Убедитесь, что используете pythonw.exe для запуска без консоли
base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("main.py", base=base)]

setup(
    name="LunarLegit - CS2 AHK Cheat by TinyTosha",
    version="1.0",
    description="By ChatGPT and TinyTosha",
    options={"build_exe": {"packages": ["tkinter", "subprocess", "os", "psutil", "ttkthemes"]}},
    executables=executables
)

