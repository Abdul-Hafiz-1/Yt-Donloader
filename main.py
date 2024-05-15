import tkinter
import customtkinter
from pytube import YouTube

def startdownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)  
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")

        video.download()
        finishLabel.configure(text="Downloaded!", text_color="white")
    except:
        finishLabel.configure(text="Download Error", text_color="red")

def on_progress(stream, chunks, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + "%")
    pPercentage.update()

    # Update progress bar
    pProgressBar.set(float(percentage_of_completion) / 100)

# System settings
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

# App frame -- size, dimension etc.
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Vid installer")

# Ui elements
title = customtkinter.CTkLabel(app, text="Insert Youtube link")
title.pack(pady=10, padx=10)

# Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Download percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

pProgressBar = customtkinter.CTkProgressBar(app, width=400)
pProgressBar.set(0)
pProgressBar.pack(padx=10, pady=10)

# Download button
download = customtkinter.CTkButton(app, text="Download", command=startdownload)
download.pack(padx=10, pady=10)

# Run App
app.mainloop()