print('Hello ')
N = int(input('Please input the length of the pole : '))
print(f'The pole is {N} cm')
K =int(input('Please input the number of particles : '))
print(f'The number of particles are {K}')
numbers =[]
for i in range(1,K+1):
    x = int(input(f"The  number {i} : "))
    numbers.append(x)
print(f'The particles {numbers}')
furthest = max(numbers)
nearest = min(numbers)

if N-furthest > nearest:
    print(f"The earliest possible time is {N-furthest} cm/s")
else:
    print(f"The earliest possible time is {nearest} cm/s")


if furthest > 10-nearest:
    print(f"The latest possible time is {furthest + (furthest-((furthest+nearest)/2))} cm/s")
else:
    print(f"The latest possible time is {10-nearest +(10-nearest-((10-nearest+furthest)/2))} cm/sec")
print('hello')   
print('hello')   

