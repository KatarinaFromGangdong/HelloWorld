import os
import random
from PIL import Image, ImageTk
import tkinter as tk

# Path to the folder containing your images
folder_path = "J:/My Drive/HelloWorld/Python/random-program/TWICE"

# Get a list of all image files in the folder
image_files = [f for f in os.listdir(
    folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Select a random image file
random_image = random.choice(image_files)

# Open the random image using PIL
image_path = os.path.join(folder_path, random_image)
image = Image.open(image_path)

# Display the image using Tkinter
root = tk.Tk()
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.image = photo
label.pack()

root.mainloop()
