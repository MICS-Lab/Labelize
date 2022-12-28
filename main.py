import os
import tkinter as tk
from tkinter import PhotoImage, filedialog

# Create a Tkinter window
window = tk.Tk()

# Prompt the user to select the directory containing the images
directory = filedialog.askdirectory()

# Get a list of all the images in the directory
images = os.listdir(directory)

# Set the size to which you want to resize the images
size = (200, 200)

# Create a counter to keep track of the current image
counter = 0

# Function to display the next image
def next_image():
  global counter
  global images
  global size
  global window
  global label
  # Increment the counter
  counter += 1
  # Check if the counter has reached the end of the list
  if counter >= len(images):
    # Reset the counter
    counter = 0
  print(counter)

  img = PhotoImage(file=os.path.join(directory, images[counter]))
  label.configure(image=img)
  label.image = img


# Create a button to display the next image
button = tk.Button(window, text='Next', command=next_image)
button.pack()


img = PhotoImage(file=os.path.join(directory, images[0]))
label = tk.Label(window, image=img)
label.pack()

# Run the Tkinter event loop
window.mainloop()
