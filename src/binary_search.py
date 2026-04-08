from src.my_array import MyArray


def binary_search(array: MyArray, target: int) -> int:
    
    low = 0
    high = len(Array) -1

    while low <= high
        mid = (low + high) // 2

        guess = array.mid

        if guess == target
            return mid

        if guess < target
            low = mid  + 1

        else:
            low = mid - 1

    return -1 