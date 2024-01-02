import tkinter as tk
from tkinter import filedialog
from moviepy.editor import *

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])  # Limit file types to .mp4
    if file_path:
        entry.delete(0, tk.END)  # Clear the entry field
        entry.insert(0, file_path)  # Insert the selected file path into the entry field

def convert_selected_file():
    file_path = entry.get()
    if file_path:
        convert_video_to_audio(file_path)

def convert_video_to_audio(video_path):
    try:
        video = VideoFileClip(video_path)
        audio_path = os.path.splitext(video_path)[0] + ".mp3"
        audio = video.audio
        audio.write_audiofile(audio_path)
        print(f"Audio extracted and saved to {audio_path}")
        print("Conversion complete!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Create a tkinter window
root = tk.Tk()
root.title("Video to Audio Converter")

# Create an Entry field for file path input
entry = tk.Entry(root, width=50)
entry.pack()

# Add a button to select a file
select_button = tk.Button(root, text="Select File", command=select_file)
select_button.pack()

# Add a button to start conversion
convert_button = tk.Button(root, text="Convert", command=convert_selected_file)
convert_button.pack()

# Start the tkinter main loop
root.mainloop()
