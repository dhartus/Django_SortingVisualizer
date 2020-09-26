import time

class BubbleSort:
    def __init__(self, array):
        self.array = array
        self.barcolor = 'red'

    def sort(self):
        n = len(self.array)
        arr = self.array
        print(n)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    yield arr


