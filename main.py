import os
import tkinter as tk
from tkinter import PhotoImage

# Set the directory containing the images
directory = 'faces'

# Get a list of all the images in the directory
images = os.listdir(directory)

# Create a Tkinter window
window = tk.Tk()

# Iterate through the images and display them one by one
for image in images:
  img = PhotoImage(file=os.path.join(directory, image))
  label = tk.Label(window, image=img)
  label.pack()
  window.mainloop()
