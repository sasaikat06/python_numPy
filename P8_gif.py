from moviepy.editor import VideoFileClip
from tkinter.filedialog import *


video = askopenfilename()

clip = VideoFileClip(video)

clip.write_gif("Water Fall GIF.gif", fps=60)