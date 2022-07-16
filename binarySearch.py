

def Binary_Search(list, target):
    length = len(list)
    
    if length == 2:
        if list[0] == target or list[1] == target:
            return True
        else:
            return False
    
    mid = length // 2

    if list[mid] == target:
        return True
    elif list[mid] < target:
        return Binary_Search(list[mid:], target)
    else:
        return Binary_Search(list[:mid], target)


if __name__ == "__main__":
    list = [1, 3, 4, 7, 9, 10, 13, 15, 16, 22, 32, 35, 39, 48, 51, 54]

    print(Binary_Search(list, 15))
    print(Binary_Search(list, 17))
    print(Binary_Search(list, 1))
