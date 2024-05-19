# Counting to twenty

for i in range(1,21):
    print(i)

# making a list

numbers_list = list(range(1, 101))

for i in numbers_list:
    print(i)

# min max summing a million

print(min(numbers_list))
print(max(numbers_list))
print(sum(numbers_list))

# odd numbers
odd_list = list(range(1, 21, 2))

for num in odd_list:
    print(num)

# multiples of 3
threes = list(range(3, 30, 3))
print(threes)

# cubes
cubes = [cube**3 for cube in range(1, 10)]
print(cubes)