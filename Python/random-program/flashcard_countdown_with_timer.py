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
count = 144

# Initialize label for countdown timer
countdown_label = tk.Label(
    root, text=f"Time left: {count}%M:%S", font=('Helvetica', 16))
countdown_label.pack()

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




def next_image():
    show_random_image()


def show_random_image():
    # Select a random image file
    random_image = random.choice(image_files)

    # Open the random image using PIL
    image_path = os.path.join(folder_path, random_image)
    image = Image.open(image_path)

    # Display the image using Tkinter
    photo = ImageTk.PhotoImage(image)
    image_label.configure(image=photo)
    image_label.image = photo

    # Reset countdown timer
    global count
    count = 144
    countdown_label.config(text=f"Time left: {count}")
    update_timer()


# Initial image display
show_random_image()

root.mainloop()
