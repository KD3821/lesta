'''
Python 3.8
Релизован алгоритм быстрой сортировки.
Взят средний элемент как опорный для случая обработки отсортированного списка, чтобы время выполнения было О(n log n), а не O(n**2)
'''
def mysort(arr):
    if len(arr) <= 2:
        if len(arr) < 2:
            return arr
        else:
            if arr[0] > arr[1]:
                arr.reverse()
                return arr
            else:
                return arr
    else:
        mid = int(len(arr)/2)
        pivot = arr[mid]
        arr.pop(mid)
        less = [i for i in arr if i<=pivot]
        greater = [i for i in arr if i>pivot]
        return mysort(less) + [pivot] + mysort(greater)

