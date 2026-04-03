import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    url = entry.get()
    
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL")
        return
    
    # Generate QR
    qr = qrcode.make(url)
    qr.save("qr_code.png")
    
    # Display QR in GUI
    img = Image.open("qr_code.png")
    img = img.resize((200, 200))
    img = ImageTk.PhotoImage(img)
    
    label_img.config(image=img)
    label_img.image = img

# Main window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("300x350")

# Input label
label = tk.Label(root, text="Enter URL:")
label.pack(pady=10)

# Entry box
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Generate button
btn = tk.Button(root, text="Generate QR Code", command=generate_qr)
btn.pack(pady=10)

# QR display label
label_img = tk.Label(root)
label_img.pack(pady=20)

# Run app
root.mainloop()