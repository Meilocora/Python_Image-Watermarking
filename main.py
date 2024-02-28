from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

image_path = ''

def open_image():
    file_path = filedialog.askopenfilename(title="Open Image File", filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")])
    if file_path:
        global image_path
        image_path = file_path
        image = Image.open(file_path)
        render_image(image)

def watermark_image():
    image = Image.open(image_path)
    # Call draw Method to add 2D graphics in an image
    watermarked_photo = ImageDraw.Draw(image)
    # Add Text from user_input field to image
    myFont = ImageFont.truetype('arial.ttf', 65)
    watermark_text = user_entry.get()
    watermarked_photo.text((10, 10), watermark_text, fill=(255, 0, 0), font=myFont)
    render_image(image)
    # Save the edited image with filename extented by Watermark Text
    name_list = image_path.split('.')
    name_list.insert(-1, watermark_text)
    join_symbol = '.'
    new_path = join_symbol.join(name_list)
    image.save(new_path)

# Displays given image with max-width of 400px
def render_image(image):
    max_width = 400
    pixels_x, pixels_y = tuple([int(max_width / image.size[0] * x) for x in image.size])
    photo = ImageTk.PhotoImage(image.resize((pixels_x, pixels_y)))
    image_label.config(image=photo)
    image_label.photo = photo


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Image Watermarker")
window.config(padx=30, pady=30)

open_button = Button(text="Open Image", command=open_image)
open_button.grid(row=0, column=1)

image_label = Label(window)
image_label.grid(row=1, column=0, columnspan=3)

entry_label = Label(text="Watermark Text:")
entry_label.grid(row=2, column=0)
user_entry = Entry(width=30)
user_entry.grid(row=2, column=1, columnspan=2, padx=20)

watermark_button = Button(text="Add Watermark", command=watermark_image)
watermark_button.grid(row=2, column=2, padx=(20,0))

window.mainloop()