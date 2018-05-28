from random import randint
import time

elements = []
liczbaElementow = 4999
#   DODANIE ELEMENTÓW
def randomize():
    for i in range (0, liczbaElementow+1):
        elements.append(randint(0, 10000))


def babelkowe():
    start = time.time()
    stop = False
    i = 0
    while(stop != True):
        stop = True
        for i in range(0, liczbaElementow):
            if(elements[i+1] < elements[i]):
                bufor = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = bufor
                stop = False
    end = time.time()
    print("Czas wykonywania się sortowania bąbelkowego: ", end-start)


def przezWybor():
    start = time.time()
    localMin = 10001
    for i in range(0, liczbaElementow+1):
        for j in range(i, liczbaElementow+1):
            if(elements[j] <= localMin):
                localMin = elements[j]
                index = j
        bufor = elements[i]
        elements[i] = localMin
        elements[index] = bufor
        localMin = 10001
    end = time.time()
    print("Czas wykonywania się sortowania przez wybór: ", end - start)

def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < pivot:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part






randomize()
print("\n\nPrzed srotowaniem: ", elements)
babelkowe()
print(elements)


elements = []
randomize()
print("\n\nPrzed srotowaniem: ", elements)
przezWybor()
print(elements)


elements = []
randomize()
print("\n\nPrzed srotowaniem: ", elements)
start = time.time()
quicksort(elements)
end = time.time()
print("Czas wykonywania się sortowania przez wybór: ", end - start)
print(elements)


