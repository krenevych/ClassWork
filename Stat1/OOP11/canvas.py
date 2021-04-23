from tkinter import *

root = Tk()  # створюємо головне вікно програми


canvas = Canvas(root,  # Батьківський віджет
             width=400,  # ширина віджета у пікселях
             height=300) # висота віджета у пікселях

canvas.pack()

# id = canvas.create_line(10, 200, 300, 10)
# id = canvas.create_rectangle(10, 200, 300, 10)
# Завантажуємо зображення з диску
photo = PhotoImage(file = 'cat.png')
cat_id = canvas.create_image(0, 0, image=photo, anchor=NW)


isMoving = False

def moveCat(id):

    if isMoving:
        canvas.move(id, 5, 5)

    canvas.after(150, moveCat, id)

def onCanvasClick(event):
    global isMoving
    isMoving = not isMoving
    print(event)

moveCat(cat_id)
canvas.bind('<Button-1>', onCanvasClick)



root.mainloop()