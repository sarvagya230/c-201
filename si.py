import tkinter as tk
from tkinter import messagebox

def calculate_simple_interest():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())

        simple_interest = (principal * rate * time) / 100
        result_label.config(text=f"Simple Interest: {simple_interest:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for all fields.")

# Create the main window
root = tk.Tk()
root.title("Simple Interest Calculator")

# Create and place the principal amount label and entry
principal_label = tk.Label(root, text="Principal Amount:")
principal_label.grid(row=0, column=0, padx=10, pady=10)
principal_entry = tk.Entry(root)
principal_entry.grid(row=0, column=1, padx=10, pady=10)

# Create and place the rate of interest label and entry
rate_label = tk.Label(root, text="Rate of Interest (%):")
rate_label.grid(row=1, column=0, padx=10, pady=10)
rate_entry = tk.Entry(root)
rate_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the time period label and entry
time_label = tk.Label(root, text="Time Period (years):")
time_label.grid(row=2, column=0, padx=10, pady=10)
time_entry = tk.Entry(root)
time_entry.grid(row=2, column=1, padx=10, pady=10)

# Create and place the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_simple_interest)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create and place the result label
result_label = tk.Label(root, text="Simple Interest: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
