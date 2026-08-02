#import time
#import threading
import tkinter as tk

class Pomodoro:
    def __init__(self, repeat, root, work_min=1, break_min=1):
        self.repeat = repeat
        self.root = root

        #convert min to seconds
        self.work_seconds = work_min * 60
        self.break_seconds = break_min * 60

        #Boolean counter control
        self.is_paused = False
        self.is_running = False
        self.on_break = False

        #Counter for timer
        self.current_seconds = self.work_seconds

        #Header for timer window
        self.status_label = tk.Label(root, text="Ready", font=("Arial",14))
        self.status_label.pack(pady=10)

        #Header for timer
        self.timer_label = tk.Label(root, text="25:00", font=("Arial", 30))
        self.timer_label.pack(pady=20)

        #button for start
        self.start_button = tk.Button(root, text="Start", command=self.start_work_session)
        self.start_button.pack()

        #button for pause
        self.pause_button = tk.Button(root, text="Pause", command=self.pause)
        self.pause_button.pack()

        #button for resume
        self.resume_button = tk.Button(root, text="Resume", command=self.resume)
        self.resume_button.pack()

        #button for stop or terminate
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
    #counter for pomodoro
    def count_down(self):

        #countdown not running
        if not self.is_running:
            return

        #when paused counter waits
        if self.is_paused:
            self.root.after(1000, self.count_down)
            return

        #Counter values
        minutes = self.current_seconds // 60
        seconds = self.current_seconds % 60

        #format for displaying counter
        self.timer_label.config(text=f"{minutes:02}:{seconds:02}")

        #counter begins decrementings
        if self.current_seconds > 0:
            self.current_seconds -= 1

            #updates counter
            self.root.after(1000, self.count_down)

        #break session
        else:
            if not self.on_break:

                #Work Session Complete begin break
                self.status_label.config(text="Work Session Complete!")
                self.status_label.config(text="Break Time!")

                #Sets the timer for break seconds
                self.on_break = True
                self.current_seconds = self.break_seconds

                #begins the timer counter for break
                self.root.after(1000, self.count_down)

            else:

                #End break session
                self.status_label.config(text="Break Over")
                
                #decrement the repeat
                self.repeat -= 1

                #program ends when all cycles complete
                if self.repeat <= 0:

                    self.timer_label.config(text="Done!")

                    self.is_running = False

                    self.status_label.config(text="All Cycles Complete!")

                    return

                #if we repeat begin from the top
                self.status_label.config(text="Work Session Has Begun!")
                self.on_break = False
                self.current_seconds = self.work_seconds

                #update counter
                self.root.after(1000, self.count_down)

    # pause function            
    def pause(self):
        self.is_paused = True
        self.status_label.config(text="\nTimer Paused")

    #resume function    
    def resume(self):
        self.is_paused = False
        self.status_label.config(text="\nTimer Resumed")

    #stop function
    def stop(self):
        self.is_running = False
        self.status_label.config(text="\nTimer Stopped")

        #terminates program
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
#Before opening window ask for how many times we want to repeat
repeat = int(input("Please enter how many working cycles you would like: "))


#listen_thread = threading.Thread(target=listen_cmd, args=(timer,),daemon=True)
#listen_thread.start()
#timer.cycle()


root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry("400x400")

timer = Pomodoro(repeat,root)

root.mainloop()
