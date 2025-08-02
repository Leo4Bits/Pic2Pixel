from tkinter import *
from function import *
from PIL import Image,ImageTk # hiển thị ảnh trên tkinter

# tạo main win
win = Tk()
win.title("Pic2Pixel")
win.geometry("500x600")
win.configure(bg="#072409")


# label + button to select path of pic_______
# 0-0
label1 = Label(win,text="Chon file ( JPG ): ",font=("Times New Roman",13),bg="#072409",fg="white")
label1.grid(row=0,column=0,padx=20,pady=10,sticky=W)
#____
# label + label to display file picture being choosed
# 5-0
label5 = Label(win,text="File duoc chon: ",font=("Times New Roman",13),bg="#072409",fg="white")
label5.grid(row=5,column=0,padx=20,pady=10,sticky=W)
# 5-1
label_display_pic = Label(win,text=f"",font=("Times New Roman",13),bg="white",fg="black") # ( 1 )
label_display_pic.grid(row=5,column=1,padx=10,pady=10,sticky=W)
#____
# 0-1 button to select path of pic| BUTTON
button1 = Button(win,text="select",font=("Times New Roman",13),command=lambda:SelectPath(label_display_pic,0)) # label_display_pic # ( 1 ) chọn path và đổi text của label sang path
button1.grid(row=0,column=1,padx=10,pady=10,sticky=W)


# label + entry to save under a name ______
label2 = Label(win,text="Luu voi ten: ",font=("Times New Roman",13),bg="#072409",fg="white")
label2.grid(row=1,column=0,padx=20,pady=10,sticky=W)

text_var = StringVar() # follow the paragraph in entry1 and display it at label_display_pixel               ( 3 )
entry1 = Entry(win,width=20,textvariable=text_var,font=("Times New Roman",13))                        #( 3 )
entry1.grid(row=1,column=1,padx=10,pady=10,sticky=W)


# label + button to save pixel.jpg at _______
# 2-0
label3 = Label(win,text="Luu tai thu muc: ",font=("Times New Roman",13),bg="#072409",fg="white")
label3.grid(row=2,column=0,padx=20,pady=10,sticky=W)
#___
# label + label to display folder being choosed to save pixel
label7 = Label(win,text="Luu tai folder: ",font=("Times New Roman",13),bg="#072409",fg="white")
label7.grid(row=7,column=0,padx=20,pady=10,sticky=W)

label_display_folder = Label(win,text="",font=("Times New Roman",13),bg="white",fg="black") # ( 2 )
label_display_folder.grid(row=7,column=1,padx=10,pady=10,sticky=W)
#___
# 2-1 button to save pixel.jpg at
button2 = Button(win,text="Browse",font=("Times New Roman",13),command=lambda:SelectPath(label_display_folder,1)) # ( 2 ) chọn path và đổi text của label sang path
button2.grid(row=2,column=1,padx=10,pady=10,sticky=W)

# label + entry (user) enter pixel_size ________
label_pixel_size = Label(win,text="Pixel size: ",font=(("Times New Roman"),13),bg="#072409",fg="white") # người dùng nhập
label_pixel_size.grid(row=3,column=0,padx=20,pady=10,sticky=W)

text_var_pixel_size = StringVar()
entry_pixel_size = Entry(win,width=20,textvariable=text_var_pixel_size,font=("Times New Roman",13)) # (4)
entry_pixel_size.grid(row=3,column=1,padx=10,pady=10,sticky=W)


# THONG TIN gồm các mục (1) (2) (3)
# lable to in4
label4 = Label(win,text="THONG TIN",background="#0E3B14",fg="white")
label4.grid(row=4,column=0,padx=20,pady=10,sticky=W)

# label to display name being typed to save ( var->>>> entry 1)
label6 = Label(win,text="Ten file (pixel): ",font=("Times New Roman",13),bg="#072409",fg="white")
label6.grid(row=6,column=0,padx=20,pady=10,sticky=W)

label_display_pixel = Label(win,text="",textvariable=text_var,font=("Times New Roman",13),bg="#FFFFFF",fg="black") # có textvariable = text_var rồi, không cần update lại ( 3 )
label_display_pixel.grid(row=6,column=1,padx=10,pady=10,sticky=W)

#label to display pixel size being typed to save
label7 = Label(win,text="Pixel size: ",font=("Times New Roman",13),bg="#072409",fg="white")
label7.grid(row=8,column=0,padx=20,pady=10,sticky=W)

label_display_pixel_size = Label(win,text="",textvariable=text_var_pixel_size,font=("Times New Roman",13),bg="#FFFFFF",fg="black") # có textvariable = text_var)pixel_size rồi, không cần update lại ( 4 )
label_display_pixel_size.grid(row=8,column=1,padx=10,pady=10,sticky=W)

#label to report error
label_error = Label(win,text="",font=("Times New Roman",13),bg="#072409")
label_error.grid(row=10,column=1,padx=10,pady=10,sticky=W)

#___________ Hàm trung gian xử lí ngoại lệ trường hợp k có dữ liệu, dữ liệu sai ( để trống )
def run_pic2pixel():
    try:
        pixel_size = int(label_display_pixel_size["text"])
        Pic2Pixel(
            label_display_pixel["text"],
            label_display_pic["text"],
            label_display_folder["text"],
            win,
            label_error,
            pixel_size
        )
    except Exception as e:
        label_error.config(text=f"LỖI: {e}", fg="white", bg="red", width=30, height=2)

# button to convert pic 2 pixel (RUN)
button_run = Button(win,text="RUN",bg="green",fg="white",width=10,height=5,font=("Times New Roman",13),command= run_pic2pixel)
button_run.grid(row=9,column=5,padx=10,pady=10,sticky=W)

# display logo PTIT
import_img = Image.open(r"C:\Users\Lenovo\Desktop\Nhatnam\WorkSpace\HelloPython\HelloTkinter\ProjectTkinter\Pic2Pixel\Picture\Logo_PTIT_University.png")
resize = import_img.resize((100,100),Image.Resampling.LANCZOS)
img_logo = ImageTk.PhotoImage(resize)

button_Ptit = Button(win,image=img_logo)
button_Ptit.grid(row=9,column=0,padx=10,pady=10,sticky=W)

win.mainloop()


'''ver2
Chuyển sang pixel, chuyển sang màu pixel khác ( như các điểm màu đen sẽ thành trắng)
'''