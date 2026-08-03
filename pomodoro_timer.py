"""
This is a Pomodoro Time Management Application
Devon Williams
Aug. 2nd 2026
"""
import time
import threading

#Need to create countdown first
#NOTE: 25 mins is needed for a work session

"""
#This is our start time
work_time_sec = 25 * 60

#we need it to run till it is 0
while work_time_sec >= 0:

    clock_time_min = work_time_sec // 60
    clock_time_sec = work_time_sec % 60

    print(f"{clock_time_min:02d}:{clock_time_sec:02d}\n", end="\r")

    time.sleep(1)

    work_time_sec -= 1
"""
pause_timer = threading.Event()
quit_timer = threading.Event()

pause_timer.set()

#Timer Countdown function in seconds
def countdown(total_seconds):

    #Counts down till 0
    while total_seconds >= 0:

        if quit_timer.is_set():
            print("\nTimer Stopped")
            return

        pause_timer.wait()

        #creates a tuple of ground and modulo division
        mins, secs = divmod(total_seconds, 60)

        #display our counter on the same line
        print(f"{mins:02d}:{secs:02d}", end="\r")

        #delay program 1 second
        time.sleep(1)

        #decrement our counter
        total_seconds -= 1

    print("\nTime's Up!")

#session runs for 25min
def work_session(work_time=2):
    timer_threading(work_time, "work session")
    
#break session runs for 5min
def break_session(break_time=2):
    timer_threading(break_time, "break session")

#repeat sessions
def cycle(repeat):
    while repeat > 0 and not quit_timer.is_set():

        #run work and break sessions
        work_session()

        if quit_timer.is_set():
            break

        break_session()

        #decrement repeat
        repeat -= 1

        #display how many more sessions left
        print(f"{repeat} Session(s) left!\n")

def timer_threading(duration, session_type):
    print(f"\n{session_type} Start!")

    timer_thread = threading.Thread(
            target=countdown,
            args=(duration,)
    )

    timer_thread.start()

    while timer_thread.is_alive():

        command = input("\n[P]ause [R]esume ").lower()

        if command == "p":
            pause_timer.clear()
            print("Timer Paused")

        elif command == "r":
            pause_timer.set()
            print("Timer Resumed")

        elif command == "q":
            quit_timer.set()
            pause_timer.set()
            break
    timer_thread.join()
    print(f"{session_type} End!\n")

#take user input for number of cycles
user_input = int(input("Please input the number of cycles: "))
cycle(user_input)
