import os
import tkinter as tk
from tkinter import PhotoImage, filedialog

# csv = 'image path, classification\n'
csv = ''
counter = 0

window = tk.Tk()
directory = filedialog.askdirectory()
images = os.listdir(directory)

# Function to display the next image
def next_image():
  global counter
  global images
  global window
  global label
  counter += 1
  if counter >= len(images):
    counter = 0
  print(counter)

  img = PhotoImage(file=os.path.join(directory, images[counter]))
  label.configure(image=img)
  label.image = img# Function to display the next image

def prev_image():
  global counter
  global images
  global window
  global label
  counter -= 1
  if counter <0:
    counter = len(images) - 1
  print(counter)

  img = PhotoImage(file=os.path.join(directory, images[counter]))
  label.configure(image=img)
  label.image = img


def classify_image(classification):
  global counter
  global images
  global window
  global label
  global csv
  csv += f"{images[counter]}, {classification}\n"
  next_image()

top_btns = tk.Frame(window)
button = tk.Button(top_btns, text='Next', command=next_image)
button.grid(column=0, row=0)
button = tk.Button(top_btns, text='Previous', command=prev_image)
button.grid(column=1, row=0)
top_btns.pack()

classes_btns = tk.Frame(window)
button0 = tk.Button(classes_btns, text='Glasses', command=lambda :classify_image("glasses"))
button0.grid(column=0, row=0)
button1 = tk.Button(classes_btns, text='No Glasses', command=lambda :classify_image("no glasses"))
button1.grid(column=1, row=0)
button1 = tk.Button(classes_btns, text='Unclear', command=lambda :classify_image("unclear"))
button1.grid(column=2, row=0)

img = PhotoImage(file=os.path.join(directory, images[0]))
label = tk.Label(window, image=img)
label.pack()
classes_btns.pack()

# Run the Tkinter event loop
window.mainloop()


# export csv
with open('output.csv', 'a') as f:
  f.write(csv)
