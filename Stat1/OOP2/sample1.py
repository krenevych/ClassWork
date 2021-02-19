from turtle import * # Підключаємо модуль turtle

reset()      # Ініціалізуємо режим малювання

# === Малюємо квадрат ===
down()       # Опускаємо перо
pencolor("#AFEEEE")
fillcolor("red")

begin_fill()
forward(150)  # Рухаємося вперед на 50 пікселів,
             # тобто зображуємо першу сторону квадрата
left(90)     # Поворот вліво на 90 градусів
forward(150)  # Зображуємо другу сторону квадрата
left(90)     # Поворот вліво на 90 градусів
forward(150)  # Зображуємо третю сторону квадрата
left(90)     # Поворот вліво на 90 градусів
forward(150)  # Зображуємо четверту сторону квадрата
end_fill()
up()         # Підіймаємо перо
# === Зображення квадрата завершено ===

mainloop()       # Затримуємо вікно на екрані

# # set the fillcolor
# t.fillcolor(col)
#
# # start the filling color
# t.begin_fill()
#
# # drawing the square of side s
# for _ in range(4):
#     t.forward(s)
#     t.right(90)
#
# # ending the filling of the color
# t.end_fill()