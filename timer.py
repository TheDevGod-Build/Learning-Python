import time

my_timer = int(input("Enter the time for the timer in seconds: "))
for timer in range (my_timer , 0 , -1) :
    seconds = timer % 60
    minutes = int (timer/60)%60
    hours = int(timer  / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIme Up")