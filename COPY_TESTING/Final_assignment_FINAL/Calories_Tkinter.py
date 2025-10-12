import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import csv
import random
from datetime import datetime

# Consts
FOOD_DICT_FILE_PATH = "common_foods_with_mealplan.csv"
DAILY_FOOD_FILE_PATH = "daily_food_calories.csv"
QUOTES_TXT_FILE_PATH = "motivational_weight_loss_quotes.txt"
KEY_INDEX = 0
VALUE_INDEX = 1

# Global dicts
food_dict = {}
quote_dict = {}

# ------------------------
# Backend logic (from your original code)
# ------------------------

def food_dict_maker(csv_file, _dict):
    try:
        with open(csv_file) as food_file_csv:
            next(food_file_csv)
            reader = csv.reader(food_file_csv)
            for line in reader:
                key = line[KEY_INDEX]
                value = float(line[VALUE_INDEX])
                _dict[key] = value
    except FileNotFoundError:
        open(csv_file, "w").close()
    return _dict


def motivation_dict_maker(txt_file):
    try:
        with open(txt_file, encoding="utf-8") as file:
            next(file)
            for line in file:
                separate_line = line.split(".")
                key = separate_line[KEY_INDEX]
                quote = separate_line[VALUE_INDEX]
                quote_dict[key] = quote.strip()
    except FileNotFoundError:
        open(txt_file, "w").close()
    return quote_dict


def todays_date(food_file):
    today = datetime.today()
    formatted_date = today.strftime("%Y, %d, %m")

    try:
        with open(food_file, "r") as f:
            first_line = f.readline().strip()
    except FileNotFoundError:
        first_line = ""

    if first_line != formatted_date:
        with open(food_file, "w") as f:
            f.write(f"{formatted_date}\n")


def csv_to_list(csv_file):
    _list = []
    try:
        with open(csv_file) as f:
            next(f)
            reader = csv.reader(f)
            for line in reader:
                _list.append(line)
    except FileNotFoundError:
        open(csv_file, "w").close()
    return _list


def add_food(food_file, code, food, total_cals):
    with open(food_file, "a", newline='') as f:
        f.write(f"{code},{food},{total_cals:.1f}\n")


def remove_food(food, food_file):
    temp_list = []
    with open(food_file) as f:
        reader = csv.reader(f)
        for line in reader:
            temp_list.append(line)
    for line in temp_list:
        if food in line:
            temp_list.remove(line)
            break
    with open(food_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(temp_list)


def get_quote(quotes):
    if not quotes:
        return "Stay motivated!"
    num = str(random.randint(1, len(quotes)))
    return quotes[num] + "!"


def format_input(user_input):
    return user_input.strip().capitalize()


# ------------------------
# GUI logic
# ------------------------

class CalorieTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calorie Tracker")
        self.root.geometry("700x600")
        self.root.configure(bg="#222831")

        self.foods_frame = tk.Frame(root, bg="#393E46")
        self.foods_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Initialize data
        food_dict_maker(FOOD_DICT_FILE_PATH, food_dict)
        quotes = motivation_dict_maker(QUOTES_TXT_FILE_PATH)
        todays_date(DAILY_FOOD_FILE_PATH)
        self.current_quote = get_quote(quotes)

        # --- Header / Quote ---
        self.quote_label = tk.Label(
            self.foods_frame,
            text=self.current_quote,
            font=("Segoe UI", 12, "italic"),
            fg="#00ADB5",
            bg="#393E46",
            wraplength=600
        )
        self.quote_label.pack(pady=10)

        # --- Food list display ---
        self.food_listbox = tk.Listbox(
            self.foods_frame, font=("Segoe UI", 11),
            bg="#EEEEEE", fg="#222831", height=15, width=60
        )
        self.food_listbox.pack(pady=10)

        # --- Total calories ---
        self.total_label = tk.Label(
            self.foods_frame, text="Total Calories: 0", font=("Segoe UI", 12, "bold"),
            fg="#FFD369", bg="#393E46"
        )
        self.total_label.pack(pady=5)

        # --- Buttons ---
        btn_frame = tk.Frame(self.foods_frame, bg="#393E46")
        btn_frame.pack(pady=15)

        ttk.Button(btn_frame, text="Add Food", command=self.add_food_gui).grid(row=0, column=0, padx=10)
        ttk.Button(btn_frame, text="Remove Food", command=self.remove_food_gui).grid(row=0, column=1, padx=10)
        ttk.Button(btn_frame, text="Change Quote", command=self.change_quote).grid(row=0, column=2, padx=10)
        ttk.Button(btn_frame, text="Refresh List", command=self.refresh_list).grid(row=0, column=3, padx=10)
        ttk.Button(btn_frame, text="Exit", command=root.quit).grid(row=0, column=4, padx=10)

        # Load foods on startup
        self.refresh_list()

    def refresh_list(self):
        """Refresh the list of foods and total calories"""
        self.food_listbox.delete(0, tk.END)
        _list = csv_to_list(DAILY_FOOD_FILE_PATH)
        total_cals = 0

        for _, name, cals in _list:
            self.food_listbox.insert(tk.END, f"{name} - {float(cals):.1f} kcal")
            total_cals += float(cals)
        self.total_label.config(text=f"Total Calories: {total_cals:.1f}")

    def add_food_gui(self):
        """Add a new food item"""
        food_name = simpledialog.askstring("Add Food", "Food name:")
        if not food_name:
            return
        formatted = format_input(food_name)

        grams = simpledialog.askfloat("Grams", "How many grams?")
        if not grams:
            return

        # If food is known
        if formatted in food_dict:
            calories = food_dict[formatted]
        else:
            cal_per_100 = simpledialog.askfloat("Calories per 100g", f"Calories per 100g for {formatted}?")
            if not cal_per_100:
                return
            calories = cal_per_100
            with open(FOOD_DICT_FILE_PATH, "a", newline='') as f:
                f.write(f"{formatted},{calories:.1f}\n")
            food_dict[formatted] = calories

        total_cals = (calories / 100) * grams
        code = random.randint(999, 10000)
        add_food(DAILY_FOOD_FILE_PATH, code, formatted, total_cals)
        messagebox.showinfo("Added", f"{formatted} added: {total_cals:.1f} kcal")
        self.refresh_list()

    def remove_food_gui(self):
        """Remove a food"""
        selected = self.food_listbox.get(tk.ACTIVE)
        if not selected:
            messagebox.showwarning("Remove", "No food selected.")
            return
        food_name = selected.split(" - ")[0]
        remove_food(food_name, DAILY_FOOD_FILE_PATH)
        self.refresh_list()
        messagebox.showinfo("Removed", f"{food_name} removed.")

    def change_quote(self):
        quotes = motivation_dict_maker(QUOTES_TXT_FILE_PATH)
        self.current_quote = get_quote(quotes)
        self.quote_label.config(text=self.current_quote)


# ------------------------
# Run App
# ------------------------
if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.theme_use("clam")
    app = CalorieTrackerApp(root)
    root.mainloop()
