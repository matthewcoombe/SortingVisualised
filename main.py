# Matthew Coombe
# 09 January 2021
# Sorting visualisation

import pygame
import pygame_gui
from math import floor, ceil
import numpy as np

pygame.init()
clock = pygame.time.Clock()
fps = 60
running = True
WIDTH = 1000
HEIGHT = 700
pygame.display.set_caption("Sorting Visualisation")
screen = pygame.display.set_mode([WIDTH, HEIGHT])
background = pygame.Surface((WIDTH, HEIGHT))
background.fill((0, 0, 0))
manager = pygame_gui.UIManager((WIDTH, HEIGHT))
MAX = 500
margin = 20
size = 240
gap = min(ceil(240 / size), 6)
arr = np.random.choice(range(size), size, replace=False)
delay = gap * 50 - round(1 / (7 - gap)) + 1

# SLIDERS

arr_slider_dim = pygame.Rect(725, 20, 200, 40)
slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=arr_slider_dim, start_value=5, value_range=(5, 480),
                                                manager=manager)
slider.set_current_value(240)
time_slider_dim = pygame.Rect(725, 77, 200, 40)
time_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=time_slider_dim, start_value=1, value_range=(1, 300),
                                                     manager=manager)
time_slider.set_current_value(150)
arr_text_dim = pygame.Rect(595, 20, 130, 40)
array_text = pygame_gui.elements.UITextBox(html_text="<font size=5>Array Size</font>",
                                           relative_rect=arr_text_dim, manager=manager)
size_dim = pygame.Rect(925, 20, 55, 40)
size_text = pygame_gui.elements.UITextBox(html_text="<font size=5>240</font>",
                                          relative_rect=size_dim, manager=manager)

speed_text_dim = pygame.Rect(595, 77, 130, 40)
speed_text = pygame_gui.elements.UITextBox(html_text="<font size=5>Speeeeeeed</font>",
                                           relative_rect=speed_text_dim, manager=manager)

speedv_dim = pygame.Rect(925, 77, 55, 40)
speedv_text = pygame_gui.elements.UITextBox(html_text="<font size=5>25</font>",
                                            relative_rect=speedv_dim, manager=manager)

# BUTTONS

sort_button_dim = pygame.Rect(424, 20, 151, 97)
sort_button = pygame_gui.elements.UIButton(relative_rect=sort_button_dim, text="SOOORT", manager=manager)

quick_button_dim = pygame.Rect(20, 20, 114, 40)
quick_button = pygame_gui.elements.UIButton(relative_rect=quick_button_dim, text="Quick", manager=manager)

bubble_button_dim = pygame.Rect(154, 20, 114, 40)
bubble_button = pygame_gui.elements.UIButton(relative_rect=bubble_button_dim, text="Bubble", manager=manager)

selection_button_dim = pygame.Rect(288, 20, 114, 40)
selection_button = pygame_gui.elements.UIButton(relative_rect=selection_button_dim, text="Selection", manager=manager)

insertion_button_dim = pygame.Rect(20, 77, 114, 40)
insertion_button = pygame_gui.elements.UIButton(relative_rect=insertion_button_dim, text="Insertion", manager=manager)

merge_button_dim = pygame.Rect(154, 77, 114, 40)
merge_button = pygame_gui.elements.UIButton(relative_rect=merge_button_dim, text="Merge", manager=manager)

heap_button_dim = pygame.Rect(288, 77, 114, 40)
heap_button = pygame_gui.elements.UIButton(relative_rect=heap_button_dim, text="Heap", manager=manager)


def quicksort(list, lo, hi):
    if lo < hi:
        p = partition(list, lo, hi)
        quicksort(list, lo, p - 1)
        quicksort(list, p + 1, hi)


def partition(list, lo, hi):
    pivot = list[hi]
    pygame.time.wait(delay)
    screen.fill((0, 0, 0))
    draw(list[lo:hi])
    pygame.display.update()
    i = lo
    for j in range(lo, hi):
        if list[j] < pivot:
            list[i], list[j] = list[j], list[i]
            i += 1
    list[i], list[hi] = list[hi], list[i]
    return i


def bubblesort(list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(list)):
            screen.fill((0, 0, 0))
            draw([i, i + 1])
            pygame.display.update()
            if i + 1 < len(list) and list[i] > list[i + 1]:
                swapped = True
                list[i], list[i + 1] = list[i + 1], list[i]
        pygame.time.wait(delay)


def selectionsort(list):
    for i in range(len(list) - 1):
        min = i
        for j in range(i + 1, len(list)):

            screen.fill((0, 0, 0))
            draw([j, min])
            pygame.display.update()
            if list[j] < list[min]:
                min = j
        list[min], list[i] = list[i], list[min]
        pygame.time.wait(delay)


def insertionsort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        pygame.time.wait(delay)
        screen.fill((0, 0, 0))
        draw([j + 1, i])
        pygame.display.update()
        list[j + 1] = key


def mergesort(list, left, right):
    if left < right:
        mid = (left + right) // 2
        mergesort(list, left, mid)
        mergesort(list, mid + 1, right)

        L = list[left:mid + 1].copy()
        R = list[mid + 1:right + 1].copy()
        i = j = 0

        for k in range(left, right + 1):
            if i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    list[k] = L[i]
                    i += 1
                else:
                    list[k] = R[j]
                    j += 1
            elif i < len(L):
                list[k] = L[i]
                i += 1
            else:
                list[k] = R[j]
                j += 1
            screen.fill((0, 0, 0))
            draw([k])
            pygame.display.update()
        pygame.time.wait(delay)


def heapify(list, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and list[largest] < list[l]:
        largest = l

    if r < n and list[largest] < list[r]:
        largest = r

    if largest != i:
        list[i], list[largest] = list[largest], list[i]
        screen.fill((0, 0, 0))
        draw([i, largest])
        pygame.display.update()

        heapify(list, n, largest)


def heapsort(list):
    n = len(list)

    for i in range(n // 2 - 1, -1, -1):
        heapify(list, n, i)
        pygame.time.wait(delay)

    for i in range(n - 1, 0, -1):
        list[i], list[0] = list[0], list[i]
        heapify(list, i, 0)


def draw(drawArr):
    global margin
    margin = 20
    colWidth = ((WIDTH - 2 * margin) - (len(arr) - 1) * gap) / len(arr)
    margin += ((colWidth - floor(colWidth)) * (len(arr)) // 2)
    colWidth = floor(colWidth)

    for i in range(len(arr)):
        if i == drawArr[-1]:
            pygame.draw.rect(screen, (0, 255, 0),
                             [margin + (colWidth + gap) * i, MAX + 150 - (arr[i] * MAX // len(arr)),
                              colWidth, arr[i] * MAX / len(arr)])
        elif i in drawArr:
            pygame.draw.rect(screen, (255, 0, 0),
                             [margin + (colWidth + gap) * i, MAX + 150 - (arr[i] * MAX // len(arr)),
                              colWidth, arr[i] * MAX / len(arr)])
        else:
            pygame.draw.rect(screen, (255, 255, 255),
                             [margin + (colWidth + gap) * i, MAX + 150 - (arr[i] * MAX // len(arr)),
                              colWidth, arr[i] * MAX / len(arr)])
    manager.draw_ui(screen)


def main():
    global running
    global size
    global arr
    global gap
    function = quicksort
    time_delta = clock.tick(60) / 1000.0

    while running:
        draw([-1])
        slider.enable()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                    if event.ui_element == slider:
                        size = slider.get_current_value()
                        gap = min(ceil(240 / size), 6)
                        arr = np.random.choice(range(size), size, replace=False)
                        size_text = pygame_gui.elements.UITextBox(html_text=f"<font size=5>{size}</font>",
                                                                  relative_rect=size_dim, manager=manager)
                        draw([-1])
                    if event.ui_element == time_slider:
                        global delay
                        input = round(time_slider.get_current_value() / (7 - gap)) + 1
                        delay = gap * 50 - input
                        speedv_text = pygame_gui.elements.UITextBox(html_text=f"<font size=5>{min(input, 50)}</font>",
                                                                    relative_rect=speedv_dim, manager=manager)
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == quick_button:
                        print("quick")
                        function = quicksort
                    if event.ui_element == merge_button:
                        function = mergesort
                        print("merge")
                    if event.ui_element == selection_button:
                        print("selection")
                        function = selectionsort
                    if event.ui_element == heap_button:
                        print("heap")
                        function = heapsort
                    if event.ui_element == bubble_button:
                        print("bubble")
                        function = bubblesort
                    if event.ui_element == insertion_button:
                        print("insertion")
                        function = insertionsort
                    if event.ui_element == sort_button:
                        try:
                            print("sorting")
                            if function == mergesort or function == quicksort:
                                args = [arr, 0, len(arr) - 1]
                            else:
                                args = [arr]
                            function(*args)
                            draw([-1])
                        except:
                            print("Select a sorting algorithm first")

            manager.process_events(event)

        manager.update(time_delta)
        screen.blit(background, (0, 0))
        manager.draw_ui(screen)
        slider.show()
        draw([-1])
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()


if __name__ == '__main__':
    main()
