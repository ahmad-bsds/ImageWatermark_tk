import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk

window = tk.Tk()

window.title('Watermark App')
window.geometry("350x200") 
window.configure(bg='#4682A9')


label = tk.Label(window, text='Enter your water mark text below:',bg='#4682A9', font=("Helvetica", 10))
label.grid(row=1, column=1)

waterMarkText = tk.Text(height=1, width=40)
waterMarkText.grid(row=2, column=1, pady=10, columnspan=10)
waterMarkText.config(bg='#F6F4EB')

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])
    if file_path:
        PHOTO = file_path

def apply_watermark():
    try:
        watermark_text = waterMarkText.get("1.0", "end-1c")
        image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])
        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)
        width, height = image.size
        font = ImageFont.truetype("arial.ttf", 36)  # You can change the font and size

        # Calculate text bounding box
        text_bbox = draw.textbbox((10, 10), watermark_text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        x = width - text_width - 10
        y = height - text_height - 10
        draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))  # You can change the color and opacity

        image.show()
    except Exception as e:
        print("Error applying watermark:", e)


apply_button = tk.Button(window, text="Select Image and Apply", command=apply_watermark, bg='#91C8E4', foreground='black')
apply_button.grid(row=3, column=2, pady=10)


window.mainloop()

