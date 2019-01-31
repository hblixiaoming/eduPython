import math


# 冒泡排序
def buddleSort(array):
    i = 0
    l = len(array)
    while i < l:
        j = 0
        while j < l - i - 1:
            if array[j] > array[j + 1]:
                temp = array[j + 1]
                array[j + 1] = array[j]
                array[j] = temp
                pass
            j = j + 1
            pass
        i = i + 1
        pass
    pass


# 选择排序
def selectSort(array):
    l = len(array)
    i = 0
    while i < l:
        j = i
        minIndex = j
        minValue = array[j]
        while j < l:
            if array[j] < minValue:
                minIndex = j
                minValue = array[j]
                pass
            j = j + 1
            pass
        temp = array[i]
        array[i] = array[minIndex]
        array[minIndex] = temp
        i = i + 1
    pass


# 插入排序
def insertSort(array):
    i = 1
    l = len(array)
    while i < l:
        j = i - 1
        current = array[i]
        while j >= 0 and array[j] > current:
            array[j + 1] = array[j]
            j = j - 1
            pass
        array[j + 1] = current
        pass
    pass


# 归并
def merge(arr1, arr2):
    i = 0
    j = 0
    l1 = len(arr1)
    l2 = len(arr2)
    result = []
    while i < l1:
        while j < l2:
            if i < l1 and arr1[i] < arr2[j]:
                result.append(arr1[i])
                i = i + 1
            elif j < l2:
                result.append(arr2[j])
                j = j + 1
            pass
        break
        pass
    while i < l1:
        result.append(arr1[i])
        i = i + 1
        pass
    while j < l2:
        result.append(arr1[j])
        j = j + 1
        pass
    return result


# 归并排序
def mergeSort(array):
    l = len(array)
    if l < 2:
        return array
    middle = math.ceil(l / 2)
    left = array[0:middle]
    right = array[middle:l]
    return merge(mergeSort(left), mergeSort(right))


# 快速排序
def quickSort(array, left, right):
    if left >= right:
        return
    index = partSort(array, left, right)
    quickSort(array, left, index - 1)
    quickSort(array, index + 1, right)
    pass


def partSort(array, left, right):
    key = array[left]
    pivot = left
    while left < right:
        # 必须先从从基数的对面开始
        # 因为先从左面开始所以left的值一定会大于key在最后的交换后就会造成大于key的数被交换到key的前面
        while left < right and array[right] >= key:
            right = right - 1
        while left < right and array[left] <= key:
            left = left + 1
        temp = array[left]
        array[left] = array[right]
        array[right] = temp
        pass
    temp = array[left]
    array[left] = array[pivot]
    array[pivot] = temp
    return left

if __name__ == '__main__':
    array = [7, 8, 2, 3, 4, 1, 5]
    print("----buddle sort-----")
    buddleSort(array)
    print(array)

    array = [7, 8, 2, 3, 4, 1, 5]
    print("----select sort-----")
    selectSort(array)
    print(array)

    array = [7, 8, 2, 3, 4, 1, 5]
    print("----insert sort-----")
    selectSort(array)
    print(array)

    print("----merge sort-----")
    array = [7, 8, 2, 3, 4, 1, 5]
    result = mergeSort(array)
    print(result)

    print("----quick sort-----")
    array = [7, 8, 2, 3, 4, 1, 5]
    quickSort(array, 0, len(array) - 1)
    print(array)
    pass
