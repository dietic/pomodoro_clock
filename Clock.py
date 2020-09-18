import tkinter as tk
import time
import sys


class Clock:
    def __init__(self, parent, t):
        self.parent = parent
        # t is in hours
        self.study_time = t*60*60
        # all variables in seconds
        self.study_elapsed_time = 0
        self.temp_study_elapsed_time = 0
        self.break_elapsed_time = 0
        # hours
        self.study_hours = 0
        self.break_hours = 0
        # minutes
        self.study_minutes = 0
        self.break_minutes = 0
        # seconds
        self.study_seconds = 0
        self.break_seconds = 0
        # break time in minutes
        self.break_time_starts_at = 60 * 60
        self.break_time = 25*60
        # labels
        self.header = tk.Label(parent, font=(
            "Open Sans", 20), text="Reloj Pomodoro", width=120)
        self.header.grid(row=1, columnspan=120)

        self.study_label = tk.Label(
            parent, font=("Open Sans", 20), text="Tiempo de trabajo", width=30, height=5)
        self.study_label.grid(row=2, column=1, columnspan=30)

        self.break_label = tk.Label(parent, font=(
            "Open Sans", 20), text="Break", width=30, height=5)
        self.break_label.grid(row=3, column=1, columnspan=30)

        self.segundos = tk.Label(parent, font=("Open Sans", 20), text="0")
        self.segundos.grid(row=2, column=91, columnspan=30)

        self.minutos = tk.Label(parent, font=("Open Sans", 20), text="0")
        self.minutos.grid(row=2, column=61, columnspan=30)

        self.horas = tk.Label(parent, font=("Open Sans", 20), text="0")
        self.horas.grid(row=2, column=31, columnspan=30)

        self.break_segundos = tk.Label(
            parent, font=("Open Sans", 20), text="0")
        self.break_segundos.grid(row=3, column=91, columnspan=30)

        self.break_minutos = tk.Label(parent, font=("Open Sans", 20), text="0")
        self.break_minutos.grid(row=3, column=61, columnspan=30)

        self.break_horas = tk.Label(parent, font=("Open Sans", 20), text="0")
        self.break_horas.grid(row=3, column=31, columnspan=30)

        self.button = tk.Button(parent, font=("Open Sans", 20), text="Comenzar",
                                width=30, command=self.start_clock)
        self.button.grid(row=4, column=41, columnspan=40)

    def refreshSeconds(self):
        self.segundos.configure(text="%i" % self.study_seconds)

    def refreshMinutes(self):
        self.minutos.configure(text="%i" % self.study_minutes)

    def refreshHours(self):
        self.horas.configure(text="%i" % self.study_hours)

    def refreshBreakSeconds(self):
        self.break_segundos.configure(text="%i" % self.break_seconds)

    def refreshBreakMinutes(self):
        self.break_minutos.configure(text="%i" % self.break_minutes)

    def refreshBreakHours(self):
        self.break_horas.configure(text="%i" % self.break_hours)

    def start_clock(self):
        while(self.study_elapsed_time < self.study_time):
            self.study_elapsed_time += 1
            self.study_seconds += 1
            self.temp_study_elapsed_time += 1
            if self.temp_study_elapsed_time % 60 == 0:
                self.study_seconds = 0
                self.study_minutes += 1
                self.refreshMinutes()
            if self.temp_study_elapsed_time % 3600 == 0:
                self.study_seconds = 0
                self.study_minutes = 0
                self.study_hours += 1
                self.refreshMinutes()
                self.refreshHours()
            self.refreshSeconds()
            self.parent.update()
            time.sleep(1/150)
            if (self.temp_study_elapsed_time % self.break_time_starts_at == 0) and self.study_elapsed_time < self.study_time:
                self.break_elapsed_time = 0
                self.break_hours = 0
                self.break_minutes = 0
                self.break_seconds = 0
                while (self.break_elapsed_time < self.break_time):
                    self.break_elapsed_time += 1
                    self.study_elapsed_time += 1
                    self.break_seconds += 1
                    if self.break_elapsed_time % 60 == 0:
                        self.break_seconds = 0
                        self.break_minutes += 1
                        self.refreshBreakMinutes()
                    if self.break_elapsed_time % 3600 == 0:
                        self.break_seconds = 0
                        self.break_minutes = 0
                        self.break_hours += 1
                        self.refreshBreakMinutes()
                        self.refreshBreakHours()
                    self.refreshBreakSeconds()
                    self.parent.update()
                    time.sleep(1/150)
                    print(self.break_elapsed_time)


root = tk.Tk()
clock = Clock(root, 2)
root.mainloop()
