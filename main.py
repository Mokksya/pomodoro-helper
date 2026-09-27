import winsound
import time
from  pathlib import Path
import csv
import datetime

# Таймер
def countdown(minutes, task, width):
    time_forend = int(minutes * 60)
    while time_forend >= 0:
        print(f"\r{(time_forend // 60):02d}:{(time_forend % 60):02d}| {task:{width}}", end="")
        if time_forend > 0:
            time.sleep(1)
        time_forend -= 1
    winsound.Beep(500, 500)


# Запись в CSV данных о сессии
def time_session(name, time_start, duration):
    session_file = Path.cwd() / "sessions.csv"
    if not session_file.exists():
        with session_file.open("w", encoding="utf-8", newline="") as f:
            write = csv.writer(f)
            write.writerow(["name_session","start_session","duration"])
    with session_file.open("a", encoding="utf-8", newline="") as f:
        write = csv.writer(f)
        write.writerow([name, time_start, duration])


# Переменные
round_num = 1
name_task = input("Привет!\nНапиши, чем хочешь заняться?\n")
name_break = "Отдых"
name_final = "Готовимся к следующей задаче"
max_width = max(len(name_task), len(name_break), len(name_final))
start_session = datetime.datetime.now()
start_session_text = start_session.strftime("%Y-%m-%d %H:%M:%S")

# Круг таймеров
try:
    while round_num <= 4:
        countdown(25, name_task, max_width)
        if round_num != 4:
            countdown(5, name_break, max_width)
        else:
            countdown(15, name_final, max_width)
        round_num += 1
    print()
    print("Отсчет окончен")
except KeyboardInterrupt:
    print("\nТаймер прерван")


# Запись в файл
end_session = datetime.datetime.now()
time_duration = end_session - start_session
time_session(name_task, start_session_text, int(time_duration.total_seconds()))
