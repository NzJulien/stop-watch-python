


import time
import datetime
import winsound
def set_timer():
    try:
        time = input("Enter the time to stop in a 24 hour format: ")
        stop_time = datetime.datetime.strptime(time,"%H:%M").time()
        return stop_time
    except ValueError:
        print("Invalid time!")
def main():
    timer = set_timer()
    seconds = 0
    minute = 0
    hour = 0
    while True:
        if (timer.hour,timer.minute,timer.second) ==\
        (hour,minute,seconds):
            print("Get up! motherfucker")
            freq = 1000
            duration = 500
            for _ in range(10):
                winsound.Beep(freq,duration)
            break
        seconds+=1
        if seconds ==60:
            minute+=1
            seconds=0
        if minute ==60:
            hour+=1
            minute =0
        time.sleep(1)
        print(f"Timer: {hour}:{minute}:{seconds}")
if __name__ =="__main__":
    main()

