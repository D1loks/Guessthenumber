import tkinter as tk
from tkinter import messagebox
import random


def main():
    root = tk.Tk()
    root.geometry("400x400")
    root.title("Hello World")
    label_min = tk.Label(root, text="Введіть мінімальне число:")
    label_min.pack(pady=10)
    entry1 = tk.Entry(root, width=30)
    entry1.pack(pady=10)
    label_max = tk.Label(root, text="Введіть максимальне число:")
    label_max.pack(pady=10)
    entry2 = tk.Entry(root, width=30)
    entry2.pack(pady=10)
    button1 = tk.Button(root, text="Submit",
                        command=lambda: on_submit(entry1, entry2, label_min, label_max, button1, root))
    button1.pack()
    root.mainloop()


def on_submit(entry1: tk.Entry, entry2: tk.Entry, label_min: tk.Label, label_max: tk.Label, button1: tk.Button,
              root: tk.Tk) -> None:
    try:
        min_num = int(entry1.get())
        max_num = int(entry2.get())
        if min_num < max_num:
            count = 5
            secret_number = random.randint(min_num, max_num)

            def check_guess():
                nonlocal count
                user_guess = int(new_entry.get())
                count -= 1
                label_max.config(text=f"Залишилось спроб: {count}")
                if user_guess == secret_number:
                    messagebox.showinfo("Congratulations", "Вітаємо! Ви вгадали число!")
                    root.quit()
                elif user_guess < secret_number:
                    messagebox.showinfo("Incorrect", "Ваше число занадто мале.")
                elif user_guess > secret_number:
                    messagebox.showinfo("Incorrect", "Ваше число занадто велике.")
                if count == 0:
                    messagebox.showinfo("Game Over", f"Ви не вгадали. Загадане число було {secret_number}.")
                    root.quit()

            label_min.config(text=f"Вгадайте число від {min_num} до {max_num}")
            label_max.config(text=f"Залишилось спроб: {count}")
            entry1.destroy()
            entry2.destroy()
            button1.destroy()
            new_entry = tk.Entry(root, width=30)
            new_entry.pack()
            guess_button = tk.Button(root, text="Guess", command=check_guess)
            guess_button.pack()
        elif min_num > max_num:
            messagebox.showerror("Error", "Мінімальне число більше за максимальне число!")
        elif min_num == max_num:
            messagebox.showerror("Error", "Мінімальне число не може дорівнювати максимальному числу.")
    except ValueError:
        messagebox.showerror("Error", "Будь ласка, введіть дійсні цілі числа.")


if __name__ == '__main__':
    main()
