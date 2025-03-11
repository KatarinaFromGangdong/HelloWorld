import tkinter as tk

# Initialize Tkinter
root = tk.Tk()
root.title("Countdown Timer")

# Initialize countdown variable
count = 10

# Initialize label to display countdown
countdown_label = tk.Label(root, text=f"Time left: {count}", font=('Helvetica', 16))
countdown_label.pack()

# Function to update the countdown timer
def update_timer():
    global count
    count -= 1
    countdown_label.config(text=f"Time left: {count}")

    if count > 0:
        root.after(1000, update_timer)
    else:
        countdown_label.config(text="Time's up!")

# Start the countdown timer
update_timer()

root.mainloop()
