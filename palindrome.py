# chislo = str(input())
# x = len(chislo)
# a = 0
# x = x - 1
# b = 0
# while x - a >= a:
#     if chislo[x - a] == chislo[a]:
#         a += 1
#     else:
#         b = 1
#         break
# if b == 1:
#     print("no")
# else:
#     print("true")


# num = int(input())
# rev_number = 0
# n = num
# while n != 0:
#     rem = n % 10
#     rev_number = rev_number * 10 + rem
#     n = int(n / 10)
#
# if num == rev_number:
#     print("True")
# else:
#     print("False")

# num = int(input())
# rev_number = 0
# while num != 0:
#     rem = num % 10
#     rev_number = rev_number * 10 + rem
#     num = int(num / 10)
#
# if num == rev_number:
#     print("True")
# else:
#     print("False")
while 1:
    x = input('введи число')
    print('Try' if x == x[::-1] else 'False')

