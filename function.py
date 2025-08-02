# TẠO CHỨC NĂNG BUTTON

from tkinter import *
from tkinter import filedialog
import os
from PIL import Image,ImageDraw

# 0 (mặc định) là chọn file ảnh, 1 là chọn folder (direction) | này mình tự chọn, tự quy định ( user k cần chọn 0 hay 1)
# label để cập nhật hiển thị cho user biết họ đã chọn path nào
#chọn path và đổi text của label sang path
def SelectPath(label,choice:int):
    if choice == 0:
        file_path = filedialog.askopenfilename(title="Chọn ảnh",filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")])
    elif choice == 1:
        file_path = filedialog.askdirectory(title="Chọn folder")

    label.config(text=f"{file_path}")


# tên được lưu, tên ảnh chuyển sang pixel, lưu tại folder, hiển thị label_report_error tại display,____,____
def Pic2Pixel(SavedName,NameImgToPixel,SavedAtFolder,display,label_report_error,pixel_size):

    img_root = Image.open(NameImgToPixel)
    import_img = Image.open(NameImgToPixel)
    width, height = import_img.size
    new_img = import_img.resize((width//pixel_size,height//pixel_size),resample=Image.Resampling.BILINEAR)
    # chuyển về rộng và dài mà chia hết cho pixel_size để khi add grid nó sẽ đẹp k bị dư thừa cắt ngang những khối pixel lớn
    # tức nó chia pixel_size dư nhiêu, thì trừ phần dư sẽ là rộng dài chia hết cho pixel_size
    new_img = new_img.resize((width-width%pixel_size,height-height%pixel_size),resample=Image.Resampling.NEAREST)

    def AddGrid(img,pixel_size,grid_color = "black"):
        draw = ImageDraw.Draw(img)
        width, height = img.size

        #vẽ trục dọc | vẽ trục dọc kéo dài từ tọa độ [x,0]->[x,height]
        for x in range(0,width,pixel_size):
            draw.line(([x,0],[x,height]),fill=grid_color,width=1) # width = 1 pixel
        # vẽ trục ngang 
        for y in range(0,height,pixel_size):
            draw.line(([0,y],[width,y]),fill=grid_color,width=1) # width = 1 pixel
            
        return img
    
    result_img = AddGrid(new_img,pixel_size=pixel_size)

    # nếu nó k phải ảnh RGB mà ở dạng RBGA thì chuyển ( tránh lỗi )
    # chế độ màu "P" (palette), mỗi pixel không lưu trực tiếp giá trị màu (RGB) mà chỉ lưu chỉ số trỏ đến một màu trong bảng màu.
    if result_img.mode in ("RGBA", "P"):  # có alpha hoặc palette
        result_img = result_img.convert("RGB")

    # lưu
    save_path = os.path.join(SavedAtFolder,f"{SavedName}.jpg")
    result_img.save(save_path)

    # show result với img để so sánh
    result_img.show()
    img_root.show()





