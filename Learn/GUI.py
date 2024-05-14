import customtkinter as ctk                        # pip install customtkinter
import tkinter                
import os
import sys                                            # pip install tkinter
from tkinter import filedialog, messagebox       
from PIL import Image, ImageTk                     # pip install pillow



# Lưu kích thước ban đầu của canvas
original_width = 512
original_height = 512

# Khởi tạo biến để lưu trữ đường dẫn của tệp hình ảnh
file_path = None



# Function Import Image from path
def import_img_button():
    global file_path
    file_path = filedialog.askopenfilename(
        title="Select an image file",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"), ("All Files", "*.*")]
    )

    if file_path:
        image = Image.open(file_path)
        width, height = int(image.width / 2), int(image.height / 2)
        image = image.resize((width, height), Image.BILINEAR)
        canvas.configure(width=image.width, height=image.height)
        image = ImageTk.PhotoImage(image)
        canvas.image = image
        canvas.create_image(0, 0, image=image, anchor="nw")




# Function Classification Image
def classifi_button():
    print("Generate2")



# Function Clear Image
def clear_button():
    ans = messagebox.askquestion('Delete', 'Are you sure delete image?', icon='warning')
    if ans == 'yes':
        canvas.delete("all")
        # Đặt lại kích thước của canvas về kích thước ban đầu
        canvas.configure(width=original_width, height=original_height)



# Setting for Window Display
root = ctk.CTk()
root.title("Image Classification")
ctk.set_appearance_mode("dark")
root.resizable(width=False, height=False)





# Frame include button
frame_button = ctk.CTkFrame(root)
frame_button.pack(side="bottom", expand=True, padx=20, pady=20)




# Frame include Result of the Classifi
frame_result = ctk.CTkFrame(root)
frame_result.pack(side="right", expand=True, padx=20, pady=20)





# Button for Import Image from path
import_img_button = ctk.CTkButton(
    frame_button, text="Import Image", command=import_img_button, hover_color="orange", text_color="black"
)
import_img_button.pack(side="left", padx=10, pady=10)




# Button for Classification Image
classifi_button = ctk.CTkButton(
    frame_button, text="Classifi", command=classifi_button, hover_color="orange", text_color="black"
)
classifi_button.pack(side="left", padx=10, pady=10)




# Button for Clear Image
clear_button = ctk.CTkButton(
    frame_button, text="Clear", command=clear_button, hover_color="red", text_color="black"
)
clear_button.pack(side="left", padx=10, pady=10)



# Function to open new window
def open_new_window():
    new_window = ctk.CTkToplevel(root)
    new_window.title("Image Generate")
    new_window.geometry("512x512")
    new_window.resizable(width=False, height=False)


    # Fucntion close new window
    def close():
        new_window.destroy()

    # Close the window    
    new_button = ctk.CTkButton(
        new_window, text="Close Window", command=close
    )

    new_button.pack(side="bottom", padx=10, pady=10)




# Where the Import Image will display in
canvas = tkinter.Canvas(root, width=original_width, height=original_height)
canvas.pack(side="top")



# Tạo nút mới bên trong canvas
new_func_button = ctk.CTkButton(root, text="Function", command=open_new_window)
new_func_button.pack(side="top", pady = 3)



root.mainloop()


