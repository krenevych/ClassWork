from tkinter import *
from tkinter.filedialog import askopenfilename


def openPicture():
    global canvas
    filename = askopenfilename()
    photo = PhotoImage(file=filename)
    id = canvas.create_image(0, 0, image=photo, anchor=NW)
    pass


def main():
    root = Tk()  # створюємо головне вікно програми
    global canvas
    canvas = Canvas(root,       # батьківський віджет
                    width=800,  # ширина віджета у пікселях
                    height=600  # висота віджета у пікселях
                    )
    canvas.pack()  # відображення віджета у вікні

    btn = Button(root,
                 width=20, height=2,
                 text="Move object",
                 command=onBtnClick
                 )
    btn.pack()

    photo = PhotoImage(file="cat.png")
    global id_cat
    id_cat = canvas.create_image(0, 0, image=photo, anchor=NW)
    move(id_cat, 3, 3)

    root.mainloop()  # запускаємо цикл головного вікна

isMoving = False
def onBtnClick():
    global isMoving
    isMoving= not isMoving


def move(id, dx, dy):
    global canvas, isMoving
    print("Move")

    if isMoving:
        canvas.move(id_cat, 3, 3)

    canvas.after(25, move, id, dx, dy)


if __name__ == "__main__": main()