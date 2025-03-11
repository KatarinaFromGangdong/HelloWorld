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

# Function to update the displayed image


def update_image():
    # Select a random image file
    random_image = random.choice(image_files)

    # Open the random image using PIL
    image_path = os.path.join(folder_path, random_image)
    image = Image.open(image_path)

    # Display the image using Tkinter
    photo = ImageTk.PhotoImage(image)
    label.configure(image=photo)
    label.image = photo

    # Schedule the next image update after 10 seconds
    root.after(3000, update_image)


# Initial image update
update_image()

root.mainloop()
