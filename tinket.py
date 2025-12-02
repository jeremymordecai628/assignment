#!/usr/bin/python3
"""
Simple Tkinter University  Court field booking  Application.

Features:
- Collects student id 
- Selects  the sports type using Radiobuttons
- Selects booking time using Combobox
- Shows results in a Text widget
- Uses a Frame for layout organization
"""

import tkinter as tk
from tkinter import ttk


def submit_booking():
    """
    Collect data from widgets, process it, and display output.
    """
    student_id = entry_id.get()
    sport= sport_var.get()
    time_slot = combo_time.get()

    if not student_id or not time_slot or not sport:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Please fill all fields.\n")
        return

    result = (
        f"Booking Confirmation:\n"
        f"------------------------------\n"
        f"Student Id: {student_id}\n"
        f"Sport: {sport}\n"
        f"Time Slot: {time_slot}\n"
        f"Status: Successfully Booked ✔\n"
    )

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)


root = tk.Tk()
root.title("University Court Booking System")
root.geometry("450x420")

frame = tk.Frame(root, bd=2, relief=tk.GROOVE, padx=10, pady=10)
frame.pack(pady=10)



# Student id  
tk.Label(frame, text="Student Id:", font=("Arial", 11)).grid(row=0, column=0, sticky="w")
entry_id = tk.Entry(frame, width=30)
entry_id.grid(row=0, column=1, pady=5)

# Court Type - Radiobutton
tk.Label(frame, text="Select Room Type:", font=("Arial", 11)).grid(row=1, column=0, sticky="w")

sport_var = tk.StringVar()

tk.Radiobutton(frame, text="Tennis court", variable=sport_var, value="Tennisball").grid(row=1, column=1, sticky="w")
tk.Radiobutton(frame, text="Basket court", variable=sport_var, value="Basketball").grid(row=2, column=1, sticky="w")

# Time Slot - Combobox
tk.Label(frame, text="Time Slot:", font=("Arial", 11)).grid(row=4, column=0, sticky="w")
combo_time = ttk.Combobox(frame, width=27, state="readonly")
combo_time["values"] = [
    "08:00 AM - 10:00 AM",
    "10:00 AM - 12:00 PM",
    "12:00 PM - 02:00 PM",
    "02:00 PM - 04:00 PM",
    "04:00 PM - 06:00 PM"
]
combo_time.grid(row=4, column=1, pady=5)


# Submit Button
button_submit = tk.Button(root, text="Book Room", width=20, command=submit_booking)
button_submit.pack(pady=10)

# Output Text Widget
output_box = tk.Text(root, height=10, width=50, borderwidth=2, relief=tk.GROOVE)
output_box.pack()


root.mainloop()

