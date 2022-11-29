# importing modules

from pytube import YouTube
import tkinter as tk
import threading

# Create an instance of tkinter frame or window
window = tk.Tk()
text = tk.StringVar(window)
res = tk.StringVar(window)

# Set the size of the tkinter window
window.geometry("700x350")
window.title("PythonGeeks")  # give title to the window
tk.Label(window, text="YOUTUBE VIDEO DOWNLOADER", bg='grey', font='Calibre 15').pack()  # a label
tk.Label(window, text="Enter the link to download", font='Calibre 12').pack()  # a label
tk.Entry(window, textvariable=text, width=50).pack()  # entry field
res_button1 = tk.Radiobutton(window, text='360p', value='360p', variable=res)
res_button1.deselect()
res_button1.pack()  # creating checkbox
res_button2 = tk.Radiobutton(window, text='720p', value='720p', variable=res)
res_button2.deselect()
res_button2.pack()
res_button3 = tk.Radiobutton(window, text='1080p', value='1080p', variable=res)
res_button3.deselect()
res_button3.pack()


def donwload_separate_thread():
    threading.Thread(target=downloader).start()


def downloader():  # defining a function
    t = text.get()  # getting the value
    video = YouTube(t)

    video.streams.filter(file_extension='mp4').get_by_resolution(res.get()).download()
    tk.Label(window, text="Downloaded Successfully").pack()


tk.Button(window, text="Download", bg='green', command=donwload_separate_thread).pack()

window.mainloop()
