import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont


def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(image)
        canvas.image = photo
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)


def add_watermark():
    watermark_text = watermark_entry.get()
    image = Image.open(filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")]))
    draw = ImageDraw.Draw(image)
    width, height = image.size

    text_width, text_height = int(width / 10), int(height / 10)

    if text_width > text_height:
        text_size = text_height
    elif text_height > text_width:
        text_size = text_width
    else:
        text_size = text_width

    font = ImageFont.truetype("font.ttf", text_size)
    draw.text((0,0), watermark_text, fill=(0, 0, 0, 95), font=font)
    image.show()


window = tk.Tk()
window.title("Image Watermarking Tool")

canvas = tk.Canvas(window, width=300, height=300)
canvas.pack()

# Buttons to open an image and add a watermark
open_btn = tk.Button(window, text="Open Image", command=open_image)
open_btn.pack(pady=10)

watermark_label = tk.Label(window, text="Enter Watermark Text:")
watermark_label.pack()

watermark_entry = tk.Entry(window)
watermark_entry.pack()

add_watermark_btn = tk.Button(window, text="Add Watermark", command=add_watermark)
add_watermark_btn.pack(pady=10)

window.mainloop()
