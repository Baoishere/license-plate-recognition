import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import threading
from lp_recognition import process_image, process_webcam

def select_image():
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
    if filepath:
        img_label.config(text=f"Đã chọn: {filepath}")
        display_image(filepath)
        plates = process_image(filepath)  # Gọi hàm xử lý và lấy danh sách biển số
        display_plate_results(plates)

def display_image(filepath):
    img = Image.open(filepath)
    img = img.resize((400, 300))  # Resize for display
    img_tk = ImageTk.PhotoImage(img)
    panel.config(image=img_tk)
    panel.image = img_tk

def display_plate_results(plates):
    if plates:
        result_text = "\n".join([f"Biển số: {plate}" for plate in plates])
    else:
        result_text = "Không nhận dạng được biển số!"
    plate_result_label.config(text=result_text)

def start_webcam():
    threading.Thread(target=process_webcam).start()

# Tạo giao diện Tkinter
app = tk.Tk()
app.title("Hệ thống nhận dạng biển số")
app.geometry("600x600")

# Tiêu đề
title = tk.Label(app, text="Hệ Thống Nhận Dạng Biển Số Xe", font=("Arial", 18, "bold"))
title.pack(pady=10)

# Nút chọn ảnh
btn_frame = tk.Frame(app)
btn_frame.pack(pady=10)
btn_select = tk.Button(btn_frame, text="Chọn Hình Ảnh", command=select_image, width=20, bg="lightblue")
btn_select.pack(side="left", padx=5)
btn_webcam = tk.Button(btn_frame, text="Bật Webcam", command=start_webcam, width=20, bg="lightgreen")
btn_webcam.pack(side="right", padx=5)

# Hiển thị thông tin hình ảnh
img_label = tk.Label(app, text="Chưa chọn hình ảnh")
img_label.pack()

# Panel hiển thị ảnh
panel = tk.Label(app)
panel.pack()

# Kết quả biển số
plate_result_label = tk.Label(app, text="", font=("Arial", 12), fg="blue", justify="left")
plate_result_label.pack(pady=10)

# Thoát
btn_exit = tk.Button(app, text="Thoát", command=app.quit, width=20, bg="red", fg="white")
btn_exit.pack(pady=20)

app.mainloop()
