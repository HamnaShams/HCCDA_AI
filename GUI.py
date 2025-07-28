import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_feet = float(height_entry.get())
        height_m = height_feet * 0.3048
        bmi = weight / (height_m ** 2)
        result = f"Your BMI is: {bmi:.2f}\n"

        if bmi < 18.5:
            result += "You are underweight."
        elif 18.5 <= bmi <= 24.9:
            result += "Your weight is normal."
        elif 30 <= bmi <= 34.9:
            result += "You are obese."
        else:
            result += "You are extremely obese."

        result_label.config(text=result)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x300")
root.configure(bg="#f0f8ff")

# Heading
heading = tk.Label(root, text="BMI Calculator", font=("Arial", 16, "bold"), bg="#f0f8ff")
heading.pack(pady=10)

# Weight input
tk.Label(root, text="Weight (kg):", bg="#f0f8ff", font=("Arial", 12)).pack()
weight_entry = tk.Entry(root, font=("Arial", 12))
weight_entry.pack(pady=5)

# Height input
tk.Label(root, text="Height (feet):", bg="#f0f8ff", font=("Arial", 12)).pack()
height_entry = tk.Entry(root, font=("Arial", 12))
height_entry.pack(pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate BMI", font=("Arial", 12), command=calculate_bmi)
calculate_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f8ff", fg="darkblue", wraplength=280)
result_label.pack(pady=10)

# Run the app
root.mainloop()
