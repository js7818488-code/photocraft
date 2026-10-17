from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance, ImageFilter

root = Tk()
root.title("PhotoCraft")
root.geometry("1200x700")
root.configure(bg="#121212")

img = None
edited_img = None

# ---------- Functions ----------

def show_image(image):
    image = image.copy()
    image.thumbnail((800, 600))

    photo = ImageTk.PhotoImage(image)

    image_label.config(image=photo)
    image_label.image = photo


def upload_image():
    global img, edited_img

    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
    )

    if file_path:
        img = Image.open(file_path)
        edited_img = img.copy()
        show_image(edited_img)
        status.config(text="✅ Image Uploaded")


def brightness():
    global edited_img

    enhancer = ImageEnhance.Brightness(edited_img)
    edited_img = enhancer.enhance(1.5)

    show_image(edited_img)
    status.config(text="✨ Brightness Applied")


def contrast():
    global edited_img

    enhancer = ImageEnhance.Contrast(edited_img)
    edited_img = enhancer.enhance(1.5)

    show_image(edited_img)
    status.config(text="✨ Contrast Applied")


def grayscale():
    global edited_img

    edited_img = edited_img.convert("L")

    show_image(edited_img)
    status.config(text="⚫ Grayscale Applied")


def rotate():
    global edited_img

    edited_img = edited_img.rotate(90, expand=True)

    show_image(edited_img)
    status.config(text="🔄 Image Rotated")


def flip():
    global edited_img

    edited_img = edited_img.transpose(Image.FLIP_LEFT_RIGHT)

    show_image(edited_img)
    status.config(text="↔️ Image Flipped")


def blur():
    global edited_img

    edited_img = edited_img.filter(ImageFilter.BLUR)

    show_image(edited_img)
    status.config(text="🌫 Blur Applied")


def reset_image():
    global edited_img

    if img:
        edited_img = img.copy()
        show_image(edited_img)
        status.config(text="✅ Reset Complete")


def save_image():
    global edited_img

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Files", "*.png")]
    )

    if file_path:
        edited_img.save(file_path)
        status.config(text="💾 Image Saved")


# ---------- Sidebar ----------

sidebar = Frame(root, bg="#1E1E1E", width=250)
sidebar.pack(side=LEFT, fill=Y)

title = Label(
    sidebar,
    text="PhotoCraft",
    bg="#1E1E1E",
    fg="#4CAF50",
    font=("Segoe UI", 22, "bold")
)
title.pack(pady=20)

btn_style = {
    "bg": "#2D2D2D",
    "fg": "white",
    "font": ("Segoe UI", 11, "bold"),
    "bd": 0,
    "width": 18,
    "height": 2
}

Button(sidebar, text="📁 Upload", command=upload_image, **btn_style).pack(pady=5)
Button(sidebar, text="☀ Brightness", command=brightness, **btn_style).pack(pady=5)
Button(sidebar, text="🎨 Contrast", command=contrast, **btn_style).pack(pady=5)
Button(sidebar, text="⚫ Grayscale", command=grayscale, **btn_style).pack(pady=5)
Button(sidebar, text="🔄 Rotate", command=rotate, **btn_style).pack(pady=5)
Button(sidebar, text="↔ Flip", command=flip, **btn_style).pack(pady=5)
Button(sidebar, text="🌫 Blur", command=blur, **btn_style).pack(pady=5)
Button(sidebar, text="♻ Reset", command=reset_image, **btn_style).pack(pady=5)
Button(sidebar, text="💾 Save", command=save_image, **btn_style).pack(pady=5)

# ---------- Image Frame ----------

image_frame = Frame(root, bg="#121212")
image_frame.pack(side=RIGHT, fill=BOTH, expand=True)

image_label = Label(
    image_frame,
    bg="#121212"
)
image_label.pack(expand=True)

# ---------- Status Bar ----------

status = Label(
    root,
    text="Ready ✅",
    bg="#1E1E1E",
    fg="white",
    anchor=W,
    padx=10
)

status.pack(side=BOTTOM, fill=X)

root.mainloop()