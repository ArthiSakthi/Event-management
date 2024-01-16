import tkinter as tk
from tkinter import messagebox

def add_event():
    event_name = event_name_entry.get()
    event_date = event_date_entry.get()
    event_time = event_time_entry.get()
    event_venue = event_venue_entry.get()

    if event_name and event_date and event_time and event_venue:
        event_list.insert(tk.END, f"Event: {event_name} - Date: {event_date} - Time: {event_time} - Venue: {event_venue}")
        event_name_entry.delete(0, tk.END)
        event_date_entry.delete(0, tk.END)
        event_time_entry.delete(0, tk.END)
        event_venue_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please fill in all fields")

def delete_event():
    selected_indices = event_list.curselection()
    if selected_indices:
        for index in selected_indices[::-1]:
            event_list.delete(index)
    else:
        messagebox.showerror("Error", "Please select an event to delete")

root = tk.Tk()
root.title("Event Management System")
root.geometry("500x400")

label_bg_color = "pink" 
button_bg_color ="light blue"

event_name_label = tk.Label(root, text="Event Name:", bg=label_bg_color)
event_name_label.grid(row=0, column=0)

event_date_label = tk.Label(root, text="Date:", bg=label_bg_color)
event_date_label.grid(row=1, column=0)

event_time_label = tk.Label(root, text="Time:", bg=label_bg_color)
event_time_label.grid(row=2, column=0)

event_venue_label = tk.Label(root, text="Venue:", bg=label_bg_color)
event_venue_label.grid(row=3, column=0)

event_name_entry = tk.Entry(root)
event_name_entry.grid(row=0, column=1)

event_date_entry = tk.Entry(root)
event_date_entry.grid(row=1, column=1)

event_time_entry = tk.Entry(root)
event_time_entry.grid(row=2, column=1)

event_venue_entry = tk.Entry(root)
event_venue_entry.grid(row=3, column=1)

add_button = tk.Button(root, text="Add Event", command=add_event, bg=button_bg_color, width=15, height=2)
add_button.grid(row=4, column=0)

delete_button = tk.Button(root, text="Delete Event", command=delete_event, bg=button_bg_color, width=15, height=2)
delete_button.grid(row=4, column=1)

event_list = tk.Listbox(root, width=50)
event_list.grid(row=5, columnspan=2)

root.mainloop()
