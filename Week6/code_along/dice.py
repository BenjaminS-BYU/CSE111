import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
import random

def main():
    root = tk.Tk()
    root.option_add("*Font", "Helvetica 10")
    frame_main = Frame(root)
    frame_main.master.title("Dice") # type: ignore
    frame_main.pack(padx=3,pady=3,fill=tk.BOTH,expand=True)

    setup_main(frame_main)

    frame_main.mainloop()

def setup_main(frm):
    label_side = Label(frm,text="Enter the number of sides on the dice (4-20)")
    label_side.grid(row=0,column=0)
    entry_side = IntEntry(frm,width=4,lower_bound=4,upper_bound=20)
    entry_side.grid(row=0,column=1)

    label_count = Label(frm,text="Enter the number of dice to roll (1-10)")
    label_count.grid(row=1,column=0)
    entry_count = IntEntry(frm,width=4,lower_bound=1,upper_bound=10)
    entry_count.grid(row=1,column=1)

    button_roll = Button(frm,text="Roll your dice")
    button_roll.grid(row=2,column=0)
    label_roll=Label(frm,text="")
    label_roll.grid(row=3,column=0)

    def roll_dice(sides, count):
        sum = 0
        roll_text = ""
        for roll in range(count):
            die_roll = random.randint(1,sides)
            sum += die_roll
            roll_text += f"{die_roll}"
        roll_text = f"Total {sum}"
        return roll_text

    def roll_action():
        try:
            sides = entry_side.get()
            count = entry_count.get()
        except ValueError: 
            label_roll.config(text="Not valid value")
            return
            
        label_text = roll_dice(sides,count)

        label_roll.config(text=label_text)

    button_roll.config(command=roll_action)



if __name__ == "__main__":
    main()