import customtkinter as ctk                        # pip install customtkinter
import tkinter                                     # pip install tkinter
from tkinter import filedialog, messagebox         
from PIL import Image, ImageTk                     # pip install pillow
import matplotlib.image as img                     # pip install matplotlib
import tensorflow as tf                            # pip install tensorflow
import cv2 as cv                                   # pip install opencv-python
from keras import models                        
import numpy as np                                 # pip install numpy

original_width = 500
original_height = 500

model = models.load_model('cat_dog_model_final.h5')
model.save("cat_dog_model_final.h5")

class GUI:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Image Classification")
        ctk.set_appearance_mode("dark")
        self.root.resizable(width=False, height=False)
        
        self.canvas_result = tkinter.Canvas(self.root, width=original_width, height=60, bg="black")
        self.canvas = tkinter.Canvas(self.root, width=original_width, height=original_height)
        self.frame_button = ctk.CTkFrame(self.root)
        self.import_img_button = ctk.CTkButton(
            self.frame_button, text="Import Image", command=self.importImage, hover_color="#CA6200", text_color="white", width=120,height=50,font=(18,18)
        )
    
        self.classifi_button = ctk.CTkButton(
            self.frame_button, text="Generate", command=self.predictImage, hover_color="#CA6200", text_color="white", width=120,height=50,font=(18,18)
        )
        
        self.file_path=""
        self.img_width=0
    
    def importImage(self):
        self.canvas_result.delete('all')
        self.file_path = filedialog.askopenfilename()
        if(self.file_path):
            image = Image.open(self.file_path)
            self.img_width = image.width
            image = image.resize((image.width, image.height), Image.BILINEAR)
            self.canvas.configure(width=image.width, height=image.height)
            self.canvas_result.configure(width=image.width)
            image = ImageTk.PhotoImage(image)
            self.canvas.image = image
            self.canvas.create_image(0, 0, image=image, anchor="nw")
        else:
            self.canvas_result.create_text(original_width/2, 30, text="PLEASE PICK YOUR PICTURE !", fill="red", font=('Calibri 20 bold'))

    def predictImage(self):
        if(self.file_path==""):
            self.canvas_result.delete('all')
            self.canvas_result.create_text(original_width/2, 30, text="PLEASE PICK YOUR PICTURE !", fill="red", font=('Calibri 20 bold'))
        else:
            self.canvas_result.delete('all')
            image = img.imread(self.file_path)
            image = cv.resize(image,(128,128))
            image = tf.expand_dims(image, axis=0)
            pred = model.predict(image)
            print(np.argmax(pred))
            if(np.argmax(pred)==0):
                self.canvas_result.create_text(self.img_width/2, 30, text="THIS IS A CAT", fill="white", font=('Calibri 20 bold'))
            else:
                self.canvas_result.create_text(self.img_width/2, 30, text="THIS IS A DOG", fill="white", font=('Calibri 20 bold'))


    def show(self):
        self.frame_button.pack(side="bottom", expand=True, padx=20, pady=20)
        
        self.import_img_button.pack(side="left", padx=10, pady=10)
        
        self.classifi_button.pack(side="left", padx=10, pady=10)
                
        self.canvas_result.create_text(original_width/2, 30, text="...RESULT...", fill="white", font=('Calibri 20 bold'))
        self.canvas_result.pack(side="top", pady=10, padx=20)

        self.canvas.create_text(original_width/2, original_height/2, text="YOUR PICTURE IN HERE", fill="black", font=('Calibri 20 bold'))
        self.canvas.pack(side="top", pady=5)
        
        self.root.mainloop()



if __name__=="__main__":
    gui = GUI()
    gui.show()