from datetime import datetime
from time import sleep


for i in range(5):
    now = datetime.now().strftime("%H:%M:%S")
    print(f"Текущее время: {now}")
    sleep(1)