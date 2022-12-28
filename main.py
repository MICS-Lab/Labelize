import os
import tkinter as tk
from tkinter import PhotoImage, filedialog
from PIL import Image

# Create a Tkinter window
window = tk.Tk()

# Prompt the user to select the directory containing the images
directory = filedialog.askdirectory()

# Get a list of all the images in the directory
images = os.listdir(directory)

# Set the size to which you want to resize the images
size = (200, 200)

# Iterate through the images and display them one by one
for image in images:
  # Load the image using the PIL library
  pil_image = Image.open(os.path.join(directory, image))

  # Resize the image
  pil_image = pil_image.resize(size)

  # Convert the image to a PhotoImage object
  img = PhotoImage(data=pil_image.tobytes())

  # Display the image in the Tkinter window
  label = tk.Label(window, image=img)
  label.pack()
  window.mainloop()
