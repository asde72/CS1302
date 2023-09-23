file = open("C:\\Users\\Jordan\\OneDrive\\Documents\\Python\\CS1302\\Lab5\\words.txt")
words = file.read().splitlines()
print('Number of words read:', len(words))
def binary_search(arr, target):
    low = 0 
    high = len (arr) - 1
    count = 0
    while low <= high:
        count += 1
        mid = (low + high)// 2
        if target == arr[mid]:
            print(f'Target = {target} Found at index = {mid} Number of iterations = {count}')
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    print(f'Target = {target} Found at index = -1 Number of iterations = {count}')
    return -1


target = input('Enter search key: ').lower()
while target != 'exit':
    binary_search(words, target)
    target = input('Enter search key: ').lower()
