def bubble_sort(arr, ascending=True):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if (ascending and arr[j] > arr[j+1]) or (not ascending and arr[j] < arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

n = int(input("Введите количество чисел: "))
numbers = [int(input(f"Введите число {i+1}: ")) for i in range(n)]
direction = input("Введите направление сортировки (возрастанию/убыванию): ").strip().lower()

ascending = True if direction == "возрастанию" else False
bubble_sort(numbers, ascending)
print("Отсортированные числа:", numbers)
