import sys

file_one = open(sys.argv[1], "r")
data_one = file_one.read().replace("\n", " ").split(" ")
file_one.close()

x = float(data_one[0])
y = float(data_one[1])
r = float(data_one[2])


file_two = open(sys.argv[2], "r")
data_two = file_two.read().replace("\n", " ").split(" ")
file_two.close()

for i in range(0, len(data_two), 2):
  if (float(data_two[i]) - x)**2 + (float(data_two[i+1]) - y)**2 == r**2:
    print('0', end = ' ')
  elif (float(data_two[i]) - x)**2 + (float(data_two[i+1]) - y)**2 < r**2:
    print('1', end = ' ')
  else:
    print('2', end = ' ')





