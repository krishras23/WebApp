def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


print(factorial(5))
print(factorial(6))


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# print(fib(100))
assert 55 == fib(10)
assert 6765 == fib(20)


def counting(n):
    if n == 0:
        return 0
    else:
        return counting(n - 1) + 1


assert 113 == counting(113)


# [20, 10, 30] index = 2
# 0, 1, 2 <-----
# list ^^, index = 2
# num[n] =
def sum_list(num, index):
    if index == 0:
        return num[index]
    # ith location
    return num[index] + sum_list(num, index - 1)


assert 60 == sum_list([10, 20, 30], 2)


def bunny_ears(num_of_bunnies):
    if num_of_bunnies == 0:
        return 0
    if num_of_bunnies == 1:
        return 2
    else:
        return 2 + bunny_ears(num_of_bunnies - 1)


assert 24 == bunny_ears(12)


def triangle(row):
    if row == 0 or row == 1:
        return row
    else:
        return row + triangle(row - 1)


assert 0 == triangle(0)
assert 1 == triangle(1)
assert 3 == triangle(2)
assert 6 == triangle(3)
assert 10 == triangle(4)


def powerN(base, exp):
    if exp == 0:
        return 0
    elif exp == 1:
        return base
    else:
        return base * powerN(base, exp - 1)


assert 16 == powerN(2,4)
