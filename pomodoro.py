import time
#import threading
import tkinter as tk

class Pomodoro:
    def __init__(self, repeat, root, work_min=25, break_min=5):
        self.repeat = repeat
        self.root = root

        self.work_seconds = work_min * 60
        self.break_seconds = break_min * 60

        self.is_paused = False
        self.is_running = False

        self.current_seconds = self.work_seconds
        self.on_break = False

        self.status_label = tk.Label(root, text="Ready", font=("Arial",14))
        self.status_label.pack(pady=10)

        self.timer_label = tk.Label(root, text="25:00", font=("Arial", 30))
        self.timer_label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start_work_session)
        self.start_button.pack()

        self.pause_button = tk.Button(root, text="Pause", command=self.pause)
        self.pause_button.pack()

        self.resume_button = tk.Button(root, text="Resume", command=self.resume)
        self.resume_button.pack()

        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack()

    def start_work_session(self):

        if not self.is_running:
            self.is_running = True
            self.status_label.config(text="Work Session Has Begun!")
            self.count_down()
    """
    def start_break_session(self):
        print("\nBreak Time!")
        self.count_down(self.break_min * 60)
     
        print("Break Over")
    """
    """
    def count_down(self, seconds):

        #This allows the loop to run to 0
        while seconds >= 0 and self.is_running:

            if self.is_paused:
                time.sleep(0.1)
                continue

            #gound division returns the whole number value
            minutes = seconds // 60

            #modulus returns the remainder of the quotient
            remaining_seconds = seconds % 60

            #the :02 is a format specifier that keeps the width of the timer with two digits
            #NOTE: we are also keeping the first digit 0 when it drops below that digit
            #end="\r" allows us to print on the same line giving the appearance of a live counter
            
            print(f"{minutes:02}:{remaining_seconds:02}", end="\r")

            #this allows usi to stop right at 00:00
            if seconds == 0:
                #This keeps the last portion of the code from being executed
                break

            #we create a 1 second delay 
            time.sleep(1)
            
            #decrements the seconds by 1
            seconds -= 1
            
        print("\nTime's up!")
    """
    def count_down(self):
        if not self.is_running:
            return

        if self.is_paused:
            self.root.after(1000, self.count_down)
            return
        minutes = self.current_seconds // 60
        seconds = self.current_seconds % 60

        self.timer_label.config(text=f"{minutes:02}:{seconds:02}")

        if self.current_seconds > 0:
            self.current_seconds -= 1

            self.root.after(1000, self.count_down)

        else:
            if not self.on_break:

                self.status_label.config(text="Work Session Complete!")
                self.status_label.config(text="Break Time!")

                self.on_break = True
                self.current_seconds = self.break_seconds

                self.root.after(1000, self.count_down)

            else:
                self.status_label.config(text="Break Over")
                
                self.repeat -= 1

                if self.repeat <= 0:

                    self.timer_label.config(text="Done!")

                    self.is_running = False

                    self.status_label.config(text="All Cycles Complete!")

                    return
                self.status_label.config(text="Work Session Has Begun!")
                self.on_break = False
                self.current_seconds = self.work_seconds

                self.root.after(1000, self.count_down)
    def pause(self):
        self.is_paused = True
        self.status_label.config(text="\nTimer Paused")

    def resume(self):
        self.is_paused = False
        self.status_label.config(text="\nTimer Resumed")

    def stop(self):
        self.is_running = False
        self.status_label.config(text="\nTimer Stopped")

        self.root.destroy()

"""
    def cycle(self):
        while self.repeat > 0:
            self.start_work_session()
            if not self.is_running:
                break

            self.start_break_session()
            if not self.is_running:
                break
            self.repeat -= 1
"""
"""
def listen_cmd(timer):
    print("command listener started!")
    while timer.is_running:
        command = input("[p]ause [r]esume [q]uit: ").lower()

        if command == "p":
            timer.pause()

        elif command == "r":
            timer.resume()

        elif command == "q":
            timer.stop()
            break
"""
repeat = int(input("Please enter how many working cycles you would like: "))


#listen_thread = threading.Thread(target=listen_cmd, args=(timer,),daemon=True)
#listen_thread.start()
#timer.cycle()

root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry("400x400")

timer = Pomodoro(repeat,root)

root.mainloop()
