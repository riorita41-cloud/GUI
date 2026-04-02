from tkinter import *
from tkinter import messagebox
import stackSTL as stack  #  модуль-обёртки над C++ DLL

#Добавить элемент
def add():
    text = entryNumber.get()
    if len(text) == 0:
        messagebox.showinfo('Сообщение', 'Введите имя и возраст через пробел\nПример: Света 25')
        return

    parts = text.split()
    if len(parts) != 2:
        messagebox.showinfo('Сообщение', 'Введите имя и возраст через пробел\nПример: Света 25')
        return

    name = parts[0]
    try:
        age = int(parts[1])
        if age < 0:
            messagebox.showinfo('Сообщение', 'Возраст не может быть отрицательным')
            return
    except ValueError:
        messagebox.showinfo('Сообщение', 'Возраст должен быть числом')
        return

    success = stack.push(name, age) #  Вызываем push из нашего модуля стека.
    if success:
        entryNumber.delete(0, END)
        repaint()
    else:
        messagebox.showinfo('Ошибка', 'Не удалось добавить элемент')

#Удалить элемент
def dl():
    if stack.size() > 0:
        stack.pop_element()
        repaint()
    else:
        messagebox.showinfo('Сообщение', 'Стек пуст.')

#Показ вершины
def show_top():
    if stack.size() > 0:
        name, age = stack.peek()
        messagebox.showinfo('Вершина стека', f'Верхний элемент: {name} ({age})')
    else:
        messagebox.showinfo('Сообщение', 'Стек пуст.')

#Очистить
def clear_stack():
    if stack.size() > 0:
        if messagebox.askyesno('Подтверждение', 'Вы действительно хотите очистить стек?'):
            stack.clear()
            repaint()
    else:
        messagebox.showinfo('Сообщение', 'Стек уже пуст.')

#Выход
def exit_program():
    if messagebox.askyesno('Подтверждение', 'Вы действительно хотите выйти?'):
        window.quit()
        window.destroy()


def repaint():## Стираем всё, что было нарисовано ранее!
    canvas.delete('all')
    wCnv = canvas.winfo_width() # ширина холста
    hCnv = canvas.winfo_height() # высоота хлста
    wRect = 200 # ширина прямоугольника(блока)
    hRect = 30# высота прямоугольника

    # Начальная позиция  первого прямоугольника (снизу)
    point = [wCnv / 2 - wRect / 2, hCnv - hRect]

    elements = stack.get_all()  # Получаем все элементы стека
    elements_reversed = list(reversed(elements)) # Переворачиваем список, чтобы рисовать снизу- вверх

    for i, elem in enumerate(elements_reversed):
        name = elem[0]
        age = elem[1]
        display_text = f"{name} ({age})"

        #  Последний элемент в цикле это вершина
        if i == len(elements_reversed) - 1:
            fill_color = "#4CAF50"  # зелёный для вершины
            text_color = "white"
        else:
            fill_color = "#80CBC4"  # бирюзовый цвет
            text_color = "#004D40"

        # рисуем прямоугольник
        canvas.create_rectangle(
            point[0], point[1],   # Левый-верхний угол
            point[0] + wRect, point[1] + hRect, #Правый-нижний угол
            fill=fill_color, # Цвет заливки

        )

        # Рисуем текст внутри прямоугольника
        canvas.create_text(
            point[0] + wRect / 2, point[1] + hRect / 2,
            text=display_text, fill=text_color, font=("Arial", 10)
        )

        point[1] -= hRect  #  Рисуем  следующий блок выше текущего.

    # Подпись "Вершина" рядом с верхним блоком
    if len(elements) > 0:
        canvas.create_text(
            point[0] + wRect + 20, point[1] + hRect + hRect / 2,
            text="← Вершина", fill="#4CAF50", font=("Arial", 10, "bold"), anchor=W
        )

window = Tk()  # Создаём главное окно
window.title('Работа со стеком') # Заголовок окна
window.geometry('800x700')  # Размер окна

frame = Frame(window)
frame.pack(expand=True)

canvas = Canvas(frame, bg="white", width=800, height=450)
canvas.grid(row=0, column=0)  # Холст для рисования стека

#Поле ввода для имени и возраста
entryNumber = Entry(frame, font=("Arial", 12))
entryNumber.grid(row=1, column=0, pady=5)

btnAdd = Button(frame, text='Добавить элемент в стек', command=add, font=("Arial", 10), width=30)
btnAdd.grid(row=2, column=0, pady=2)

btnDelete = Button(frame, text='Удалить элемент из стека', command=dl, font=("Arial", 10), width=30)
btnDelete.grid(row=3, column=0, pady=2)

btnShowTop = Button(frame, text='Показать вершину', command=show_top, font=("Arial", 10), width=30)
btnShowTop.grid(row=4, column=0, pady=2)

btnClear = Button(frame, text='Очистить стек', command=clear_stack, font=("Arial", 10), width=30)
btnClear.grid(row=5, column=0, pady=2)

btnExit = Button(frame, text='Выход', command=exit_program, font=("Arial", 10), width=30)
btnExit.grid(row=6, column=0, pady=2)

stack.init()

window.mainloop()