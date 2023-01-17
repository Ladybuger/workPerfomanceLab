import sys

file = open(sys.argv[1], "r")
nums_str = file.read().replace("\n", " ").split(" ")
file.close()

nums = []
for i in range(len(nums_str)):
    nums.append(int(nums_str[i]))

aver = sum(nums)//len(nums)

search = True
i = 0
while search:
  if (aver + i) in nums:
    search = False
    aver += i
  elif (aver - i) in nums:
    search = False
    aver -= i
  i += 1

counter = 0
for i in range(len(nums)):
    while nums[i]!= aver:
        if nums[i] > aver:
            nums[i] = nums[i] - 1
            counter += 1
        elif nums[i] < aver:
            nums[i] = nums[i] + 1
            counter += 1
print(counter)


