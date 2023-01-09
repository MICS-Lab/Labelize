import os, csv
import tkinter as tk
from tkinter import PhotoImage, filedialog
import yaml

with open('config.yaml', 'r') as f:
    params = yaml.load(f, Loader=yaml.loader.SafeLoader) 
if params['directory'] is None:
    directory = filedialog.askdirectory()
else:
    directory = params['directory']

csv_output = ''
counter = 0
images = os.listdir(directory)
try:
    with open('output.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                images.remove(row['image path'])
            except:
                pass
except FileNotFoundError:
    pass
window = tk.Tk()

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
    global csv_output
    csv_output += f"{images[counter]},{classification}\n"
    next_image()

top_btns = tk.Frame(window)
button = tk.Button(top_btns, text='Next', command=next_image)
button.grid(column=0, row=0)
button = tk.Button(top_btns, text='Previous', command=prev_image)
button.grid(column=1, row=0)
top_btns.pack()

classes_btns = tk.Frame(window)
for i,c in enumerate(params['classes']):
    bt = tk.Button(classes_btns, text=c, command=lambda :classify_image(c))
    bt.grid(column=i, row=0)

try:
    img = PhotoImage(file=os.path.join(directory, images[0]))
except:
    print("No images in directory")
    exit()
label = tk.Label(window, image=img)
label.pack()
classes_btns.pack()

# keyboard shortcuts
window.bind_all('g', func=lambda e:classify_image("glasses"))
window.bind_all('n', func=lambda e:classify_image("no glasses"))
window.bind_all('u', func=lambda e:classify_image("unclear"))
window.bind_all('b', func=lambda e:classify_image("bad image"))
window.bind_all('<Left>', func=lambda e: prev_image())
window.bind_all('<Right>', func=lambda e: next_image())

# Run the Tkinter event loop
window.mainloop()


# export csv
filename = 'output.csv'
try:
    f = open(filename, 'x')
except FileExistsError:
    # File already exists
    # export csv
    with open('output.csv', 'a') as f:
        f.write(csv_output)
else:
    print(f"File {filename} created successfully.")
    f.write("image path,classification\n")
    f.write(csv_output)
    f.close()

# drop duplicates
import pandas as pd

df = pd.read_csv('output.csv')
df_deduped = df.drop_duplicates(subset=['image path'], keep='last')
df_deduped.to_csv('output.csv', index=False)