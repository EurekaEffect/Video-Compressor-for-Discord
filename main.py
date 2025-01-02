# import tkinter as tk  # Import tkinter module and alias tk
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from compress import compress_video
from tkinter import ttk

def get_path(event):
    if event.data.endswith(".mp4}"):
        text_entry.delete(0, END)
        sanitise_path = event.data
        sanitise_path = sanitise_path.replace('{', '')
        sanitise_path = sanitise_path.replace('}', '')
        text_entry.insert(0, sanitise_path)

def compress():
    size = int(scale.get())  # Get the current slider value

    r = compress_video(
        text_entry.get(), size * 1000, frame_rate.get()
    )
    if r == True:
        result_lab.config(text="Done!")
    else:
        result_lab.config(text='Error')


def browseFiles():
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select a File", filetypes=(("Video files", "*.mp4*"), ("all files", "*.*"))
    )
    text_entry.delete(0, len(text_entry.get()))
    text_entry.insert(0, filename)


wind = tk.Tk() # Establishing top level control wind
windHeight = wind.winfo_height()
windWidth = wind.winfo_width()

wind.geometry("320x200")  # Set window size
wind.resizable(False, False)
wind.eval('tk::PlaceWindow . center')
wind.title("Video transcoding")  # Set window title

# Create Title and feedback text
title_lab = ttk.Label(wind, text="Discord Compression", font="Arial 14")
result_lab = ttk.Label(wind, text="")

# create a frame containing an Entry and the button to explore files
frame2 = Frame(wind)

text_entry = ttk.Entry(frame2)

button_explore = ttk.Button(
    frame2, text="...", width=7, command=browseFiles
)

# create a frame containing 3 radio button for different file size
frame = Frame(wind)
limit_file_size = IntVar()
# Create a Scale (slider) widget to select file size from 1MB to 250MB
scale = ttk.Scale(frame, from_=1, to=250, variable=limit_file_size, orient="horizontal", length=300)
scale.set(8)  # Set the default value to 8MB
scale.pack(padx=10, pady=5)

# create a frame containing 2 radio button for different frame rate
frame3 = Frame(wind)
frame_rate = IntVar()
R_fps30 = ttk.Radiobutton(frame3, text="30fps", variable=frame_rate, value=30)
R_fps60 = ttk.Radiobutton(frame3, text="60fps", variable=frame_rate, value=60)
R_fps60.invoke()

# Set the submit button, and set the font style and size
btn = ttk.Button(wind, text="Compress to 8MB", width=windWidth-20, command=compress)

# Update the label and button text with the selected value when the slider moves
def update_text(event):
    size = int(scale.get())  # Get the current slider value
    btn.config(text=f"Compress to {size}MB")  # Update button text

# Bind the slider motion to update the label and button text
scale.bind("<Motion>", update_text)

# Positioning everything on the grid

title_lab.grid(column=1, row=1, pady=7)

frame2.grid(column=1, row=5, padx=10)
text_entry.grid(column=1, row=1)
button_explore.grid(column=2, row=1)

frame.grid(column=1, row=8, pady=4)

frame3.grid(column=1, row=9, pady=4)
R_fps30.pack(side=LEFT)
R_fps60.pack(side=LEFT)

btn.grid(column=1, row=11)
result_lab.grid(column=1, row=12)


wind.mainloop()  # Message loop of windows