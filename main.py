import winsound
import time

# Таймер
def countdown(minutes, task, width):
    time_forend = int(minutes * 60)
    while time_forend >= 0:
        print(f"\r{(time_forend // 60):02d}:{(time_forend % 60):02d}| {task:{width}}", end="")
        if time_forend > 0:
            time.sleep(1)
        time_forend -= 1
    winsound.Beep(500, 500)


# Переменные
round_num = 1
name_task = input("Привет!\nНапиши, чем хочешь заняться?\n")
name_break = "Отдых"
name_final = "Готовимся к следующей задаче"
max_width = max(len(name_task), len(name_break), len(name_final))

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
