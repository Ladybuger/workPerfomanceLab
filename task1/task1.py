import sys
n = int(sys.argv[1])
m = int(sys.argv[2])

element = 0
arr = list()
result = ""
last = 0

for i in range (1, n + 1):
    arr.append(i)


while last != arr[0]:
    result += str(arr[element])

    for i in range(element, element + m):
        element = i  % n
        last = arr[element]

print(result)