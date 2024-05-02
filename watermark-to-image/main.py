from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageFont, ImageDraw

def watermark_image():
    """Generates watermark on image and saves a copy of it."""
    path = path_entry.get()
    text = watermark_entry.get()

    if path == '' or text == '':
        messagebox.showinfo(title="Oops", message="Please enter valid path and text.")
    else:
        im = Image.open(rf'{path}')
        x = im.size[0]/2
        y = im.size[1]/2
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype("arial.ttf", 60)
        draw.text((x, y), text, font=font, fill=(255, 255, 255))
        im.save("watermarked_image.jpg")

        path_entry.delete(0, END)
        watermark_entry.delete(0, END)

        messagebox.showinfo(title="Saved", message="The watermarked image is saved in "
                                                   "your device please search for 'watermarked_image.jpg'.")


window = Tk()
window.title("Add Watermark to your image!")
window.config(padx=20, pady=70)

# Enter path details
path_label = Label(text="Path to image: ")
path_label.grid(column=0, row=0)
path_entry = Entry(width=35)
path_entry.grid(column=1, row=0)


# Enter watermark text
watermark_label = Label(text="Enter watermark text:")
watermark_label.grid(column=0, row=1)
watermark_entry = Entry(width=35)
watermark_entry.grid(column=1, row=1)

# Write text over image and save it as jpg file
save_button = Button(text="Watermark and save image", command=watermark_image)
save_button.grid(column=0, row=2, columnspan=2)

quit_button = Button(text="Quit", command=window.destroy)
quit_button.grid(column=0, row=3, columnspan=2)


window.mainloop()
