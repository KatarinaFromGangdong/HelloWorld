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
label = tk.Label(root)
label.pack()

# Initialize countdown timer label
timer_label = tk.Label(root, font=('Helvetica', 16))
timer_label.pack()

# Function to update the displayed image and countdown timer


def update_image_and_timer(count=30):
    # Select a random image file
    random_image = random.choice(image_files)

    # Open the random image using PIL
    image_path = os.path.join(folder_path, random_image)
    image = Image.open(image_path)

    # Display the image using Tkinter
    photo = ImageTk.PhotoImage(image)
    label.configure(image=photo)
    label.image = photo

    # Update countdown timer label
    timer_label.config(text=f"Next image in: {count} seconds")

    if count > 0:
        # Schedule the next update after 1 second
        root.after(10000, lambda: update_image_and_timer(count - 1))
    else:
        # Update the image and reset the timer after 10 seconds
        update_image_and_timer()


# Initial image update
update_image_and_timer()

root.mainloop()
