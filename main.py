import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import os
import subprocess
import json

def load_scripts(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data['scripts']

def create_button(root, text, command, row, column):
    button = ttk.Button(root, text=text, command=command)
    button.grid(row=row, column=column, padx=10, pady=10)

def run_script(path):
    full_path = os.path.abspath(path)
    if os.path.exists(full_path):
        subprocess.Popen(full_path, shell=True)
    else:
        print(f"Script {full_path} does not exist")

# Создаем окно с выбранной темой
root = ThemedTk(theme="equilux")
root.title("LunarLegit - CS2 AHK Cheat by TInyTosha")

# Настраиваем стили
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), padding=10)

# Загружаем скрипты из файла
script_file_path = 'regscripts.json'
scripts = load_scripts(script_file_path)

# Создаем кнопки для каждого скрипта
columns = 3  # Количество колонок
for index, script in enumerate(scripts):
    row = index // columns
    column = index % columns
    create_button(root, text=script['name'], command=lambda p=script['path']: run_script(p), row=row, column=column)

# Запускаем главный цикл обработки событий
root.mainloop()

