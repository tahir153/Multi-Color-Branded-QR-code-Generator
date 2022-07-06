import qrcode
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image


def QR():
    text = entry.get()
    choice_background = back_ground.get()
    logo = Image.open('PWTonlylogo.png')
    basewidth = 70
    wpercent = (basewidth / float(logo.size[1]))
    hsize = int((float(logo.size[1]) * float(wpercent)))
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(text)
    qr.make()

# background and filling choice
    if choice_background == choices_background[0]:
        img = qr.make_image(fill_color='RGB(0, 0, 0)', back_color="RGB(255, 255, 255)").convert("RGB")

    elif choice_background == choices_background[1]:
        img = qr.make_image(fill_color='RGB(4, 19, 171)', back_color="RGB(255, 255, 255)").convert("RGB")

    elif choice_background == choices_background[2]:
        img = qr.make_image(fill_color='RGB(202, 0, 0)', back_color="RGB(255, 255, 255)").convert("RGB")

    elif choice_background == choices_background[3]:
        img = qr.make_image(fill_color='RGB(7, 151, 0)', back_color="RGB(255, 255, 255)").convert("RGB")

    elif choice_background == choices_background[4]:
        img = qr.make_image(fill_color='RGB(4, 19, 171)', back_color="RGB(0,0,0)").convert("RGB")

    elif choice_background == choices_background[5]:
        img = qr.make_image(fill_color='RGB(244, 198, 56)', back_color="RGB(0,0,0)").convert("RGB")

    else:
        img = qr.make_image(fill_color='RGB(0, 0, 0)', back_color="RGB(255, 255, 255)").convert("RGB")


    # img = qr.make_image(fill_color='RGB(244, 198, 56)', back_color="RGB(0,0,0)").convert("RGB")

    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
    pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
    img.paste(logo, pos)

    time_stamp = datetime.datetime.now().strftime('%b-%d-%Y_%I-%M-%S')
    file_name = f'NEW QR {time_stamp}.png'
    img.save(file_name)

#Window
root = tk.Tk()
root.title("QR code generator By TAHIR HABIB")
root.geometry("700x680+250+5")
root.configure(background = "#011D33")
root.columnconfigure(0, weight=1)
root.iconbitmap("C:\\Users\\tahir\PycharmProjects\\pythonProject\\venv\\favicon.ico")


blank_line = Label(root, text="\n", fg="red", bg="#011D33", font=("Helvetica", 15))
blank_line.grid()

label_heading = Label(root, text="< QR Code Generator >", font=("Roboto", 30,"bold"), fg="white",bg="#011D33")
label_heading.grid()

blank_line = Label(root, text="\n", fg="red", bg="#011D33", font=("Helvetica", 15))
blank_line.grid()

label_heading = Label(root, text="Enter Text or Link Here!", font=("Roboto", 15), fg="white",bg="#011D33")
label_heading.grid()

entry = StringVar()
point = Entry(root,font = ("Roboto", 16),width=50,textvariable = entry,)
point.grid(pady=20, padx=25, ipady=5, ipadx=5)

blank_line = Label(root, text="Choose Color Combo(background,fill)", fg="White", bg="#011D33", font=("Helvetica", 15))
blank_line.grid()

choices_background = ["White, Black", "White, Blue", "White, Red", "White, Green", "Black, Blue", "Black, Golden"]
back_ground = ttk.Combobox(root,font=("Comic_Sans_MS",10,"bold"), values=choices_background)
back_ground.grid()

blank_line = Label(root, text="\n", fg="red", bg="#011D33", font=("Helvetica", 25))
blank_line.grid()

Generate_button = Button(root, text="Generate QR", bg="#2063A0", fg="white",font=("Helvetica", 12,"bold"), command=QR)
Generate_button.grid(pady=20, padx=25, ipady=5, ipadx=10)

blank_line = Label(root, text="\n", fg="red", bg="#011D33", font=("Helvetica", 5))
blank_line.grid()

Exit_button = Button(root, text="Exit", bg="#C50400", fg="white", command=root.quit)
Exit_button.grid()


Developer_branding_lable = Label(root, text="\n\n Made By Tahir Habib\n", font=("Comic Sans MS", 10, 'bold'), fg="white",
                                 bg="#011D33")
Developer_branding_lable.grid()


WIDTH= 67
HEIGHT = 52
canvas = Canvas(root,height=HEIGHT, width=WIDTH)
canvas.grid()
canvas.configure(background="black")

background_pic = PhotoImage(file="QR LOGO22.png")
background = canvas.create_image(WIDTH/2, HEIGHT/2,image=background_pic,anchor=CENTER)
root.resizable(width=False, height=False)


root.mainloop()