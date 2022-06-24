import tkinter as tk
import random

# Function to swap two bars that will be animated

canvas=0
window=0

def swap(pos_0, pos_1):
    global canvas
    bar11, _, bar12, _ = canvas.coords(pos_0)
    bar21, _, bar22, _ = canvas.coords(pos_1)
    canvas.move(pos_0, bar21-bar11, 0)
    canvas.move(pos_1, bar12-bar22, 0)

worker = None

barList = 0
lengthList = 0

# Insertion Sort Algorithm

def _insertion_sort():
    global barList
    global lengthList

    for i in range(len(lengthList)):
        cursor = lengthList[i]
        cursorBar = barList[i]
        pos = i

        while pos > 0 and lengthList[pos - 1] > cursor:
            lengthList[pos] = lengthList[pos - 1]
            barList[pos], barList[pos - 1] = barList[pos - 1], barList[pos]
            swap(barList[pos], barList[pos-1])
            yield
            pos -= 1

        lengthList[pos] = cursor
        barList[pos] = cursorBar
        swap(barList[pos], cursorBar)


# Bubble Sort Algorithm

def _bubble_sort():
    global barList
    global lengthList

    for i in range(len(lengthList) - 1):
        for j in range(len(lengthList) - i - 1):
            if(lengthList[j] > lengthList[j + 1]):
                lengthList[j], lengthList[j + 1] = lengthList[j + 1], lengthList[j]
                barList[j], barList[j + 1] = barList[j + 1], barList[j]
                swap(barList[j + 1], barList[j])
                yield

# Selection Sort Algorithm

def _selection_sort():
    global barList
    global lengthList

    for i in range(len(lengthList)):
        min = i
        for j in range(i + 1, len(lengthList)):
            if(lengthList[j] < lengthList[min]):
                min = j
        lengthList[min], lengthList[i] = lengthList[i], lengthList[min]
        barList[min], barList[i] = barList[i], barList[min]
        swap(barList[min], barList[i])
        yield

# Quick sort Algorithm

def _quick_sort():
    global barList
    global lengthList
    array = 0
    start = 0
    algorithm = 0
   
    def partition(start, end):
        x = array[end]
        i = start-1
        for j in range(start, end+1, 1):
            if lengthList[j] <= x:
                i += 1
                if i < j:
                    lengthList[i], lengthList[j] = lengthList[j], lengthList[i]
                    barList[i], barList[j] = barList[j], barList[i]
                    swap(lengthList[i], lengthList[j])
                    yield
                    
    if array == []:
        array = lengthList
        end = len(lengthList) - 1

        if start < end:
            pivot = partition(array, start, end)
            algorithm(array, start, pivot-1)
            algorithm(array, pivot+1, end)


# Triggering Fuctions

def insertion_sort():
    global worker
    worker = _insertion_sort()
    animate()

def selection_sort():
    global worker
    worker = _selection_sort()
    animate()

def bubble_sort():
    global worker
    worker = _bubble_sort()
    animate()

def quick_sort():
    global worker
    worker = _bubble_sort()
    animate()

# Animation Function

def animate():
    global worker
    global window
    if worker is not None:
        try:
            next(worker)
            window.after(10, animate)
        except StopIteration:
            worker = None
        finally:
            window.after_cancel(animate)

# Generator function for generating data

def generate():
    global window
    global barList
    global lengthList
    global canvas

    canvas.delete('all')
    barstart = 5
    barend = 15
    barList = []
    lengthList = []

    # Creating a rectangle

    for bar in range(1, 60):
        randomY = random.randint(1, 360)
        bar = canvas.create_rectangle(
            barstart, randomY, barend, 365, fill='thistle3')
        barList.append(bar)
        barstart += 10
        barend += 10

    # Getting length of the bar and appending into length list
    
    for bar in barList:
        bar = canvas.coords(bar)
        length = bar[3] - bar[1]
        lengthList.append(length)

    # Differentiating the smallest and the largest
    
    for i in range(len(lengthList)-1):
        if lengthList[i] == min(lengthList):
            canvas.itemconfig(barList[i], fill='red2')
        elif lengthList[i] == max(lengthList):
            canvas.itemconfig(barList[i], fill='OrangeRed4')

def main_window():
    global window
    global canvas

    # Making a window using the Tk widget
    
    window = tk.Tk()
    window.title('Sorting Visualizer')
    window.geometry('600x450')

    # Making a Canvas within the window to display contents
    
    canvas = tk.Canvas(window, width='600', height='400')
    canvas.grid(column=0, row=0, columnspan=50)
    canvas.configure(bg="PaleTurquoise1")

    # Buttons
    
    insert = tk.Button(window, text='Insertion Sort', command=insertion_sort,bg="LightBlue2",fg="blue4")
    select = tk.Button(window, text='Selection Sort', command=selection_sort,bg="LightBlue2",fg="blue4")
    bubble = tk.Button(window, text='Bubble Sort', command=bubble_sort,bg="LightBlue2",fg="blue4")
    Quick = tk.Button(window, text='Quick Sort', command=quick_sort,bg="LightBlue2",fg="blue4")
    shuf = tk.Button(window, text='Shuffle', command=generate,bg="LightBlue2",fg="blue4")
    insert.grid(column=1, row=1)
    select.grid(column=2, row=1)
    bubble.grid(column=3, row=1)
    Quick.grid(column=4, row=1)
    shuf.grid(column=0, row=1)

    generate()
    window.mainloop()
