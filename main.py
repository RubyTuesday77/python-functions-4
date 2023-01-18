#1: Write a Python function called max_num()to find the maximum of three numbers:
def max_num(num1, num2, num3):
    return max((num1, num2, num3))

print(max_num(1, 5, 8))
print(max_num(-5, -8, -14))
print(max_num(200, 8, 1530))


#2: Write a Python function called mult_list() to multiply all the numbers in a list:
def mult_list(num_list):
    product = 1
    for number in num_list:
        product = product * number
    return product

num_list1 = [3, 2, 4]
num_list2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
num_list3 = [-4, -3, -2]
num_list4 = [5, 0, 20, 17]
print(mult_list(num_list1))
print(mult_list(num_list2))
print(mult_list(num_list3))
print(mult_list(num_list4))


#3: Write a Python function called rev_string() to reverse a string:
def rev_string(string):
    return string[::-1]

print(rev_string("Supercalifragilisticexpialidocious"))


#4: Write a Python function called num_within() to check whether a number falls in a given range:
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(num, lrange, urange):
    return num in range(lrange, urange + 1)

print(num_within(3, 2, 8))
print(num_within(9, 2, 8))
print(num_within(2, 2, 8))
print(num_within(8, 2, 8)) # Hmm, why is num = lrange TRUE and num = urange is False?


#5: Write a Python function called pascal() that prints out the first n rows of Pascal's triangle:
# The function accepts the number n, the number of rows to print.
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
def pascal(n):
    row1 = [1]
    row2 = [1, 1]
    triangle = [row1, row2]
    rowAll = []
    if n < 1:
        print('Invalid number of rows')
    elif n == 1:
        row1[0] = str(row1[0])
        print(' '.join(row1))
    elif n == 2:
        for o in triangle:
            for a in range(len(o)):
                o[a] = str(o[a])
            print((' ') * (2 - (a + 1)), (' '.join(o)))
    else:
        for i in range(2, n):
            triangle.append([1] * i)
            for j in range(1, i):
                triangle[i][j] = (triangle[i - 1][j - 1] + triangle[i - 1][j])
            triangle[i].append(1)
        for x in range(len(triangle)):
            for y in triangle[x]:
                s = str(y)
                rowAll.append(s)
            print((' ') * (n - (x + 1)), (' '.join(rowAll)))
            rowAll = []

pascal(0)
pascal(1)
pascal(2)
pascal(3)
pascal(4)
pascal(5)
pascal(6)