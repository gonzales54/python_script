import tkinter as tk
from tkinter import ttk
from tkinter import font
import time


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.master.geometry("300x300")
        self.master.title("Tkinter Freezes after clicking Buttons")

        self.font_lbl_big = font.Font(family="Meiryo UI", size=30, weight="bold")
        self.font_lbl_middle = font.Font(family="Meiryo UI", size=15, weight="bold")
        self.font_lbl_small = font.Font(family="Meiryo UI", size=12, weight="normal")

        self.create_widgets()

    def create_widgets(self):
        # Frame
        self.main_frame = tk.LabelFrame(self.master, text='', font=self.font_lbl_small)
        self.main_frame.place(x=25, y=25)
        self.main_frame.configure(height=250, width=250)
        self.main_frame.grid_propagate(0)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Start Button
        self.btn_Start = ttk.Button(self.main_frame)
        self.btn_Start.configure(text='Start')
        self.btn_Start.configure(command=self._main_func)
        self.btn_Start.grid(column=0, row=0, pady=10, sticky='NESW')

        # Label Title
        self.lbl_title = ttk.Label(self.main_frame)
        self.lbl_title.configure(text='Calculation Results Shown Here')
        self.lbl_title.grid(column=0, row=1, padx=20, pady=20, sticky='EW')

        # Label Result
        self.lbl_result = ttk.Label(self.main_frame)
        self.lbl_result.configure(text='')
        self.lbl_result.grid(column=0, row=2, padx=100, pady=10, sticky='EW')

    def _main_func(self):
        for i in range(10):
            print(i)
            self.lbl_result.configure(text=i, font=self.font_lbl_big)
            time.sleep(0.1)


def main():
    root = tk.Tk()
    app = Application(master=root)  # Inherit
    app.mainloop()


if __name__ == "__main__":
    main()
