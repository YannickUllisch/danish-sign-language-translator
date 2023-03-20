from tkinter import *
import cv2
from PIL import Image, ImageTk
import numpy as np
import import_ipynb
# import filedialog module
from tkinter import filedialog

#import functions
import DataExtraction
import Predictions
import DataPreprocessing

words =  np.array(['hvad', 'ja', 'soed'])

label_map = {label:num for num, label in enumerate(words)}
  
# Define a video capture object

def importFunctions():
    model, X_test, y_test = Predictions.import_data("../export_data/")
    return model

'''
 
# Declare the width and height in variables
width, height = 800, 600
  

  
# Create a GUI app
app = Tk()
#app.geometry("500x300")
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
# Bind the app with Escape keyboard to
# quit app whenever pressed
app.bind('<Escape>', lambda e: app.quit())
  
# Create a label and display it on app
label_widget = Label(app)
label_widget.pack()
  
# Create a function to open camera and
# display it in the label_widget on app

vid = cv2.VideoCapture(0)
# Set the width and height
vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
  
def open_camera():

    # Capture the video frame by frame
    _, frame = vid.read()

    # Convert image from one color space to other
    opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    # Capture the latest frame and transform to image
    captured_image = Image.fromarray(opencv_image)

    # Convert captured image to photoimage
    photo_image = ImageTk.PhotoImage(image=captured_image)

    # Displaying photoimage in the label
    label_widget.photo_image = photo_image

    # Configure image in the label
    label_widget.configure(image=photo_image)

    # Repeat the same process after every 10 seconds
    label_widget.after(10, open_camera)

    goBackButton = Button(app, text="Go Back", command=app.withdraw)
    goBackButton.pack()
def importFunctions():
    model, X_test, y_test = Predictions.import_data("../export_data/")
    return model

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("mp4 files",
                                                        "*.mp4"),
                                                       ("mov files",
                                                        "*.mov")))
      
    # Change label contents
    model = importFunctions()
    label_file_explorer.configure(text="File Opened: "+filename)
    test = DataExtraction.mp_sv_processing(filename)
    processed_data = DataPreprocessing.process_data([test], 151)
    output = words[np.argmax(model.predict(processed_data))]
    label = Label(app, text="predicted word: " + output)
    label.pack(fill=BOTH)



# Create a File Explorer label
label_file_explorer = Label(app,
                            text = "Danish Sign Language Translator",
                            width = 100, height = 4,
                            fg = "blue")
# Create a button to open the camera in GUI app
button1 = Button(app, text="Open Camera", command=open_camera)
button1.pack()
button2 = Button(app, text="Browse file", command=browseFiles)
button2.pack()
  
# Create an infinite loop for displaying app on screen
app.mainloop()
'''

from tkinter import *
from tkinter import ttk
import sys

class SignLanguageGUI(object):

    def __init__(self, root):
        self.root = root
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.WebcamButton = Button(root, text="Use Webcam", command=self.WebcamFeed)
        self.WebcamLabel = Label(root, text="Click to use the webcam to predict sign language:", fg="white", font=("Helvetica",16))

        self.GetVideoButton = Button(root, text="Get local file", command=self.LocalVideoPrediction)
        self.GetVideoLabel = Label(root, text="Click to translate a local video file:", fg="white", font=("Helvetica",16))

        self.ExitButton = Button(root, text="Exit",command=self.Exit)
        self.ExitLabel = Label(root, text="Click to exit application:", fg="white", font=("Helvetica",16))

        self.InstructionsLabel = Label(root, text="An application that translates videos of danish sign language to text \n Currently supported words:"
            + str(res) , fg="white", font=("Calibri", 14))

        self.ReturnMenu = Button(root, text="Return to Main Menu", command=self.MainMenu)

        self.MainMenu()

    def MainMenu(self):
        self.RemoveAll()
        self.InstructionsLabel.grid(pady=(20,100), padx=20,column=1, sticky="n")
        #spacer1 = Label(root, text="")
        #spacer1.grid(row=4, column=0)
        self.WebcamLabel.grid(row=1, column=0, padx=(20,0), sticky="e")
        self.WebcamButton.grid(row=2, column=0, padx=(20,0), sticky="e")
        
        self.GetVideoLabel.grid(row=1, column=2, padx=(0,20), sticky="w")
        self.GetVideoButton.grid(row=2, column=2, padx=(0,20), sticky="w")
        
        self.ExitButton.grid(pady=(100,20), padx=20, column=1, sticky="s")
        

    def WebcamFeed(self):
        self.WebcamButton.grid_remove()
        self.WebcamLabel.grid_remove()
        self.ExitButton.grid_remove()

    def LocalVideoPrediction(self):
        filename = filedialog.askopenfilename(initialdir = "/",
                                                title = "Select a File",
                                                filetypes = (("mp4 files",
                                                            "*.mp4"),
                                                            ("mov files",
                                                            "*.mov")))
            
        # Change label contents
        model = importFunctions()
        #label_file_explorer.configure(text="File Opened: "+filename)
        test = DataExtraction.mp_sv_processing(filename)
        processed_data = DataPreprocessing.process_data([test], 151)
        output = words[np.argmax(model.predict(processed_data))]
        self.PredictLabel = Label(root, text="predicted word: " + output)
        self.PredictLabel.grid(padx=20, pady=(0,20), column=1, row=2)
        self.ReturnMenu.grid(padx=20, column=1, row=3, pady=(0,20))

    def RemoveAll(self):
        self.WebcamButton.grid_remove()
        self.WebcamLabel.grid_remove()
        self.GetVideoButton.grid_remove()
        self.GetVideoLabel.grid_remove()
        self.ExitButton.grid_remove()
        self.InstructionsLabel.grid_remove()
        self.ReturnMenu.grid_remove()

    def Exit(self):
        self.root.quit
        sys.exit(0)


if __name__ == '__main__':

    root = Tk()
    SignLanguageGUI = SignLanguageGUI(root)
    root.mainloop()