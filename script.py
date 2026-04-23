import json
import random
import tkinter as tk
from tkinter import Variable, messagebox, ttk



def CmdButtonTaskList():
    btnTaskRandom.place_forget()
    cbCategory.place(relx=0.5, rely=0.05, relwidth=0.5, relheight=0.1)
    btnAddTask.place(relx=0, rely=0.4, relwidth=0.5, relheight=0.21)
    lbTask.config(listvariable=Variable(value=tasksList))

def AddTask():
    cbCategory.place_forget()
    labelAddTask.place(relx=0.5, rely=0, relwidth=0.35, relheight=0.1)
    entryAddTask.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.1)
    labelCategoryTask.place(relx=0.5, rely=0.2, relwidth=0.4, relheight=0.1)
    cbAddTaskCategory.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.1)
    btnAddTaskToList.place(relx=0.5, rely=0.4, relwidth=0.25, relheight=0.1)
    btnCancel.place(relx=0.75, rely=0.4, relwidth=0.25, relheight=0.1)

#Функция кнопки btnAddTaskToList
def AddTaskToList():
    if entryAddTask.get() == "":
        messagebox.showinfo("Предупреждение","Поле для ввода пустое")
    task = [entryAddTask.get(), cbAddTaskCategory.get()]
    tasks.append(task)
    tasksList.append(f"{task[0]}, {task[1]}")
    CancelAddTask()
    lbTask.config(listvariable=Variable(value=tasksList))

#Функция очистки виджетов доавбления задачи
def CancelAddTask():
    labelAddTask.place_forget()
    entryAddTask.delete(0, tk.END)
    entryAddTask.place_forget()
    labelCategoryTask.place_forget()
    cbAddTaskCategory.delete(0, tk.END)
    cbAddTaskCategory.place_forget()
    btnAddTaskToList.place_forget()
    btnCancel.place_forget()
    cbCategory.place(relx=0.5, rely=0.05, relwidth=0.5, relheight=0.1)

#Выборка случайной задачи
def CmdButtonTaskRandomList():
    btnAddTask.place_forget()
    cbCategory.place_forget()
    CancelAddTask()
    cbCategory.place_forget()
    lbTask.config(listvariable=Variable(value=randomTasksList))
    btnTaskRandom.place(relx=0.5, rely=0.4, relwidth=0.5, relheight=0.21)

def CmdTaskRandom():
    randomTask = random.sample(tasks, 1)
    messagebox.showinfo("Случайная задача", f"Случайно выбранная задача:\n{randomTask[0][0]}")
    randomTasks.append(randomTask[0])
    randomTasksList.append(f"{randomTask[0][0]}, {randomTask[0][1]}")
    lbTask.config(listvariable=Variable(value=randomTasksList))

#Сохранение данных перед закрытием
def SaveLists():
    try:
        print(123)
        with open("task.json", "w") as file:
            json.dump(tasks, file, indent=4)
        with open("taskRandom.json", "w") as file:
            json.dump(randomTasks, file, indent=4)
        window.destroy()
    except:
        messagebox.showerror("Ошибка", "Ошибка работы с файлов")
        window.destroy()

#Обработка выбора категории
def SelectedCategory():
    tasksList = []
    for task in tasks:
        print(cbCategory.get())
        if task[1] == cbCategory.get():
            tasksList.append(f"{task[0]}, {task[1]}")
        elif cbCategory.get() == "Сбросить выбор":
            tasksList.append(f"{task[0]}, {task[1]}")
        lbTask.config(listvariable=Variable(value=tasksList))


window = tk.Tk()
window.title("Генератор случайных задач")
window.geometry("400x300")
window.minsize(400, 300)

try:
    with open("task.json", "r") as file:
        tasks = json.load(file)
    with open("taskRandom.json", "r") as file:
        randomTasks = json.load(file)
except:
    messagebox.showerror("Ошибка", "Ошибка чтения файла")
    window.destroy()

tasksList = []
randomTasksList = []
print(randomTasks)
for task in tasks:
    tasksList.append(f"{task[0]}, {task[1]}")
for randomTask in randomTasks:
    randomTasksList.append(f"{randomTask[0]}, {randomTask[1]}")

#Универсальный список задач
lbTask = tk.Listbox(window, listvariable=Variable(value=tasksList), width=150, font=("Arial", 12))
lbTask.place(relx=0, rely=0, relwidth=0.5, relheight=0.5)

frameButtons = tk.Frame(window, width=150, height=75)
frameButtons.place(relx=0, rely=0.55, relwidth=0.5, relheight=0.5)

#Главная панель управления
btnTaskList = tk.Button(frameButtons, text="Список задач", width=9, command=CmdButtonTaskList)
btnTaskList.place(relx=0, rely=0.1, relwidth=0.5, relheight=0.21)
btnTaskRandomList = tk.Button(frameButtons, text="История\nзадач", width=9, command=CmdButtonTaskRandomList)
btnTaskRandomList.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.21)

btnAddTask = tk.Button(frameButtons, text="Добавить задачу", width=9, command=AddTask)
btnAddTask.place(relx=0, rely=0.4, relwidth=0.5, relheight=0.21)
btnTaskRandom = tk.Button(frameButtons, text="Сгенерировать\nзадачу", width=9, command=CmdTaskRandom)

#Виджеты добавления задачи
entryAddTask = tk.Entry(window, font=("Arial", 15))
labelAddTask = tk.Label(window, text="Напишите задачу", font=("Arial", 12))
labelCategoryTask = tk.Label(window, text="Выберите категорию", font=("Arial", 12))
categoryAddTask = ["дела по дому","учеба","спорт","работа"]
cbAddTaskCategory = ttk.Combobox(window, values=categoryAddTask, font=("Arial", 12))
btnAddTaskToList = tk.Button(window, text="Добавить", command=AddTaskToList)
btnCancel = tk.Button(window, text="Отмена", command=CancelAddTask)


category = ["Сбросить выбор","дела по дому","учеба","спорт","работа"]
cbCategory = ttk.Combobox(window, values=category, font=("Arial", 12))
cbCategory.current(0)
cbCategory.place(relx=0.5, rely=0.05, relwidth=0.5, relheight=0.1)
cbCategory.bind("<<ComboboxSelected>>", lambda event: SelectedCategory())

window.protocol("WM_DELETE_WINDOW", SaveLists)

window.mainloop()