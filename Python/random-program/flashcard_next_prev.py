import os
import random
from PIL import Image, ImageTk
import tkinter as tk

# Path to the folder containing your images
folder_path = "L:/My Drive/HelloWorld/Python/random-program/CALTECH - PRACTICE  PROBLEM SOLVING"

# Get a list of all image files in the folder
image_files = [f for f in os.listdir(
    folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Initialize Tkinter
root = tk.Tk()
root.title("Image Flashcard with Countdown Timer")

# Initialize label for image display
image_label = tk.Label(root)
image_label.pack()

# Initialize countdown variable
count = 10

# Initialize label for countdown timer
countdown_label = tk.Label(
    root, text=f"Time left: {count}", font=('Helvetica', 16))
countdown_label.pack()

# Initialize index to keep track of the current image
current_image_index = 0

# Function to update the countdown timer


def update_timer():
    global count
    count -= 1
    countdown_label.config(text=f"Time left: {count}")

    if count > 0:
        root.after(1000, update_timer)
    else:
        show_random_image()

# Function to display a random image


def show_random_image():
    global current_image_index
    current_image_index = random.randint(0, len(image_files) - 1)
    image_path = os.path.join(folder_path, image_files[current_image_index])
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    image_label.configure(image=photo)
    image_label.image = photo

    # Reset countdown timer
    global count
    count = 10
    countdown_label.config(text=f"Time left: {count}")
    update_timer()

# Function to show the next image


def next_image():
    show_random_image()


# Initial image display
show_random_image()


# Next button
next_button = tk.Button(root, text="Next", command=next_image)
next_button.pack(side=tk.RIGHT)

root.mainloop()
