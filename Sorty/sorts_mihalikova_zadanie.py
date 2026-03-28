import random
import time
import sys
sys.setrecursionlimit(20000)

def bubblesort(p, n):
    u = 0
    while True:
        y = 0
        for a in range(n - 1 - u):
            if p[a] > p[a + 1]:
                p[a], p[a + 1] = p[a + 1], p[a]
                y += 1
        if y == 0:
            return p
        u += 1

def bubblesortultra(p, n):
    global pocetif, pocetmove
    u = 0
    while True:
        y = 0
        for a in range(n - 1 - u):
            pocetif += 1
            if p[a] > p[a + 1]:
                pocetmove += 2
                p[a], p[a + 1] = p[a + 1], p[a]
                y += 1
        u += 1
        pocetif += 1
        if y == 0:
            return p

def selectsort(p, n):
    for a in range(n - 1):
        i = a
        for b in range(a + 1, n):
            if p[i] > p[b]:
                i = b
        t = p[a]
        p[a] = p[i]
        p[i] = t
    return p

def selectsortultra(p, n):
    global pocetif, pocetmove
    for a in range(n - 1):
        i = a
        for b in range(a + 1, n):
            pocetif += 1
            if p[i] > p[b]:
                i = b
        if i != a:
            p[a], p[i] = p[i], p[a]
            pocetmove += 2
    return p

def insertsort(p, n):
    for a in range(1, n):
        x = p[a]
        b = a - 1
        while b >= 0 and p[b] > x:
            p[b + 1] = p[b]
            b -= 1
        p[b + 1] = x
    return p

def insertsortultra(p, n):
    global pocetif, pocetmove
    for a in range(1, n):
        x = p[a]
        b = a - 1
        pocetmove += 1
        while b >= 0:
            pocetif += 1
            if p[b] > x:
                p[b + 1] = p[b]
                pocetmove += 1
                b -= 1
            else:
                break
        p[b + 1] = x
        pocetmove += 1
    return p

def quicksort(p, l, r):
    if l >= r:
        return

    pivot = p[(l + r) // 2]
    i, j = l, r

    while i <= j:
        while p[i] < pivot:
            i += 1
        while p[j] > pivot:
            j -= 1
        if i <= j:
            p[i], p[j] = p[j], p[i]
            i += 1
            j -= 1

    if l < j:
        quicksort(p, l, j)
    if i < r:
        quicksort(p, i, r)

    return p

def quicksortultra(p, l, r):
    global pocetif, pocetmove
    if l >= r:
        pocetif += 1
        return

    pivot = p[(l + r) // 2]
    pocetmove += 1
    i, j = l, r

    while i <= j:
        pocetif += 1
        while p[i] < pivot:
            pocetif += 1
            i += 1
        while p[j] > pivot:
            pocetif += 1
            j -= 1
        pocetif += 1  # if i <= j
        if i <= j:
            p[i], p[j] = p[j], p[i]
            pocetmove += 2
            i += 1
            j -= 1

    pocetif += 1
    if l < j:
        quicksortultra(p, l, j)
    pocetif += 1
    if i < r:
        quicksortultra(p, i, r)

    return p

def radixsort(p, n):
    mx = max(p)
    e10 = 1
    vysledok = [0] * n
    while e10 < mx:
        cislice = [0] * 10
        for cislo in p:
            cislice[cislo // e10 % 10] += 1
        index = 0
        for i in range(10):
            cislice[i], index = index, index + cislice[i]
        for cislo in p:
            vysledok[cislice[cislo // e10 % 10]] = cislo
            cislice[cislo // e10 % 10] += 1
        p, vysledok = vysledok, p
        e10 *= 10
    return p

def radixsortultra(p, n):
    global pocetif, pocetmove
    mx = max(p)
    e10 = 1
    vysledok = [0] * n
    pocetmove += n
    while e10 < mx:
        cislice = [0] * 10
        for cislo in p:
            pocetmove += 1
            cislice[cislo // e10 % 10] += 1
        index = 0
        for i in range(10):
            pocetmove += 1
            cislice[i], index = index, index + cislice[i]
        for cislo in p:
            pocetmove += 2
            vysledok[cislice[cislo // e10 % 10]] = cislo
            cislice[cislo // e10 % 10] += 1
        p, vysledok = vysledok, p
        pocetmove += 2
        e10 *= 10
    return p

def mergesort(p):
    if len(p) > 1:
        mid = len(p) // 2
        L = p[:mid]
        R = p[mid:]
        mergesort(L)
        mergesort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                p[k] = L[i]
                i += 1
            else:
                p[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            p[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            p[k] = R[j]
            j += 1
            k += 1
    return p

def mergesortultra(p):
    global pocetif, pocetmove
    if len(p) > 1:
        mid = len(p) // 2
        L = p[:mid]
        R = p[mid:]
        pocetmove += len(p)
        mergesortultra(L)
        mergesortultra(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            pocetif += 1
            if L[i] < R[j]:
                p[k] = L[i]
                i += 1
            else:
                p[k] = R[j]
                j += 1
            pocetmove += 1
            k += 1
        while i < len(L):
            p[k] = L[i]
            i += 1
            k += 1
            pocetmove += 1
        while j < len(R):
            p[k] = R[j]
            j += 1
            k += 1
            pocetmove += 1
    return p

def binary_search(arr, key, start, end, comparisons):
    if start == end:
        comparisons += 1
        if arr[start] > key:
            return start, comparisons
        else:
            return start + 1, comparisons
    if start > end:
        return start, comparisons

    mid = (start + end) // 2
    comparisons += 1
    if arr[mid] < key:
        return binary_search(arr, key, mid + 1, end, comparisons)
    elif arr[mid] > key:
        return binary_search(arr, key, start, mid - 1, comparisons)
    else:
        return mid + 1, comparisons

def insertion_binary_sort(arr):
    comparisons = 0
    assignments = 0
    for i in range(1, len(arr)):
        key = arr[i]
        assignments += 1
        pos, comparisons = binary_search(arr, key, 0, i - 1, comparisons)
        arr[pos + 1:i + 1] = arr[pos:i]
        assignments += (i - pos)
        arr[pos] = key
        assignments += 1
    return arr, comparisons, assignments

def insertion_binary_sort_ultra(p, n):
    global pocetif, pocetmove
    for i in range(1, n):
        key = p[i]
        pocetmove += 1
        start, end = 0, i - 1
        while start <= end:
            mid = (start + end) // 2
            pocetif += 1
            if p[mid] < key:
                start = mid + 1
            else:
                end = mid - 1
        for j in range(i, start, -1):
            p[j] = p[j - 1]
            pocetmove += 1
        p[start] = key
        pocetmove += 1
    return p

# Tree sort
class Uzol:
    def __init__(self, hodnota):
        self.hodnota = hodnota
        self.lavy = None
        self.pravy = None

class binarnyTreeSearch:
    def __init__(self):
        self.koren = None

    def vloz(self, hodnota):
        self.koren = self.vlozUzol(self.koren, hodnota)

    def vlozUltra(self, hodnota):
        global pocetif, pocetmove
        self.koren = self.vlozUzolUltra(self.koren, hodnota)

    def vlozUzol(self, koren, hodnota):
        if koren is None:
            return Uzol(hodnota)
        if hodnota < koren.hodnota:
            koren.lavy = self.vlozUzol(koren.lavy, hodnota)
        else:
            koren.pravy = self.vlozUzol(koren.pravy, hodnota)
        return koren

    def vlozUzolUltra(self, koren, hodnota):
        global pocetif, pocetmove

        if koren is None:
            pocetif += 1
            return Uzol(hodnota)

        pocetif += 1
        if hodnota < koren.hodnota:
            koren.lavy = self.vlozUzolUltra(koren.lavy, hodnota)
        else:
            koren.pravy = self.vlozUzolUltra(koren.pravy, hodnota)
        return koren

    def Prechod(self):
        vystup = []
        self.prejdiStrom(self.koren, vystup)
        return vystup

    def prejdiStrom(self, koren, vystup):
        if koren:
            self.prejdiStrom(koren.lavy, vystup)
            vystup.append(koren.hodnota)
            self.prejdiStrom(koren.pravy, vystup)
        return

def treeSort(pole):
    strom = binarnyTreeSearch()
    for prvok in pole:
        strom.vloz(prvok)
    return strom.Prechod()


def treeSortUltra(pole):
    global pocetif, pocetmove
    pocetif = 0
    pocetmove = 0

    strom = binarnyTreeSearch()
    for prvok in pole:
        strom.vlozUltra(prvok)
    return strom.Prechod()


n = int(input("Zadaj pocet prvkov: "))

for i in range(5):
    print(f"----- MERANIE n.{i+1} -----")

    original = [random.randint(0, 10 * n) for _ in range(n)]

    #original = [random.randint(2, 12)]
    #for i in range(n-1):
    #    original.append(random.randint(-2, 7)+original[-1])

    #original=original[::-1]

    # Bubble Sort
    print('BUBBLE SORT:')
    x = original.copy()
    y = original.copy()
    start = time.time()
    bubblesort(x, len(x))
    end = time.time()
    pocetif = 0
    pocetmove = 0
    bubblesortultra(y, len(y))
    print(f"Time: {(end - start)*1000:.3f} ms | Ifs: {pocetif} | Moves: {pocetmove}")

    # Select Sort
    print('SELECT SORT:')
    x = original.copy()
    y = original.copy()
    start = time.time()
    selectsort(x, len(x))
    end = time.time()
    pocetif = 0
    pocetmove = 0
    selectsortultra(y, len(y))
    print(f"Time: {(end - start)*1000:.3f} ms | Ifs: {pocetif} | Moves: {pocetmove}")

    # Insert Sort
    print('INSERT SORT:')
    x = original.copy()
    y = original.copy()
    start = time.time()
    insertsort(x, len(x))
    end = time.time()
    pocetif = 0
    pocetmove = 0
    insertsortultra(y, len(y))
    print(f"Time: {(end - start)*1000:.3f} ms | Ifs: {pocetif} | Moves: {pocetmove}")

    # Insert sort + Binary Search
    print('INSERT SORT + BINARY SEARCH:')
    x = original.copy()
    y = original.copy()
    start = time.time()
    insertion_binary_sort(x)
    end = time.time()
    pocetif = 0
    pocetmove = 0
    insertion_binary_sort_ultra(y, len(y))
    print(f"Time: {(end - start)*1000:.3f} ms | Ifs: {pocetif} | Moves: {pocetmove}")

    # Quick Sort
    print('QUICK SORT:')
    x = original.copy()
    y = original.copy()
    start = time.time()
    quicksort(x, 0, len(x) - 1)
    end = time.time()
    pocetif = 0
    pocetmove = 0
    quicksortultra(y, 0, len(y) - 1)
    print(f"Time: {(end - start)*1000:.3f} ms | Ifs: {pocetif} | Moves: {pocetmove}")

    # Merge Sort
    print('MERGE SORT:')
    x = original.copy()
    y = original.copy()
    start = time.time()
    mergesort(x)
    end = time.time()
    pocetif = 0
    pocetmove = 0
    mergesortultra(y)
    print(f"Time: {(end - start) * 1000:.3f} ms | Ifs: {pocetif} | Moves: {pocetmove}")

    # Radix Sort
    print('RADIX SORT:')
    x = original.copy()
    y = original.copy()
    start = time.time()
    radixsort(x, len(x))
    end = time.time()
    pocetif = 0
    pocetmove = 0
    radixsortultra(y, len(y))
    print(f"Time: {(end - start)*1000:.3f} ms | Ifs: {pocetif} | Moves: {pocetmove}")

    print('TREE SORT:')
    x = original.copy()
    y = original.copy()
    start = time.time()
    treeSort(x)
    end = time.time()
    pocetif = 0
    pocetmove = 0
    treeSortUltra(y)
    print(f"Time: {(end - start) * 1000:.3f} ms | Ifs: {pocetif} | Moves: {pocetmove}")

    print('><><><><><><><><><><><><><><><><><><><><><><><><><><')