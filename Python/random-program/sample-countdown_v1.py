import tkinter as tk

# Initialize Tkinter
root = tk.Tk()
root.title("Countdown Timer")

# Initialize countdown variable
count = 10

# Initialize label for countdown timer
countdown_label = tk.Label(root, text=f"Time left: {count}", font=('Helvetica', 16))
countdown_label.pack()

# Function to update the countdown timer
def update_timer():
    global count
    count -= 1
    countdown_label.config(text=f"Time left: {count}")

    if count > 0:
        root.after(1000, update_timer)

# Function to reset the countdown timer
def reset_timer():
    global count
    count = 10
    countdown_label.config(text=f"Time left: {count}")
    
# Start the countdown timer
update_timer()

# Reset button
reset_button = tk.Button(root, text="Reset Timer", command=reset_timer)
reset_button.pack()

root.mainloop()
