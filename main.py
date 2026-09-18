import winsound
import time

# Таймер
def countdown(minutes):
    time_forend = int(minutes*60)
    while time_forend >= 0:
        print(f"\r{(time_forend // 60):02d}:{(time_forend % 60):02d}", end="")
        time.sleep(1)
        time_forend -= 1
    winsound.Beep(500,500)
    print("\nОтсчет окончен")

countdown(25)
