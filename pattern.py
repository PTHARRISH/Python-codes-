# x patter number
# n = int(input())
# for i in range(0, n+1):
#     for j in range(1, n+1):
#         if i == j or i + j == n+1:
#             print(j,end="")
#         else:
#             print(" ",end='')
#     print()

# # diamond pattern
# n = int(input())
# # n=k+1
# for i in range(0, n+1):
#     for j in range(0, n - i):
#         print(" ", end="")
#     for j in range(0, i + 1):
#         print(i, end=" ")
#     print()
#     # n = n - 1
# # n = k+1
# for i in range(0, n):
#     for j in range(0, i+1):
#         print(" ", end="")
#     for j in range(0, n - i):
#         print(i, end=" ")
#     print()

# 2. diamond pattern
# n = int(input())
# # n=k+1
# for i in range(0, n + 1):
#     for j in range(0, n - i):
#         print(" ", end="")
#     for j in range(0, i + 1):
#         print(i, end=" ")
#     print()
#     # n = n - 1
# # n = k+1
# for i in range(n - 1, -1, -1):
#     for j in range(0, n - i):
#         print(" ", end="")
#     for j in range(0, i + 1):
#         print(i, end=" ")
#     print()

# x pattern name
# n = input()
# for i in range(0, len(n)):
#     for j in range(0, len(n)):
#         if i == j or i + j == len(n)-1:
#             print(n[j],end="")
#         else:
#             print(" ",end='')
#     print()

# Largest number
# n = [63, 84, 42, 24, 100]
# for i in n:
#     a = 0
#     if a < i:
#         a = i
# print(a)

# triangle pattern
# n = int(input())
# for i in range(0, n):
#     for j in range(0, n + 1):
#         print(" ", end="")
#     for j in range(0, i + 1):
#         print(i, end=" ")
#     print()
#     n = n - 1

# reverse triangle
# n = 6
# for i in range(0, n):
#     for j in range(0, i):
#         print(" ", end="")
#     for j in range(0, n - i):
#         print(i, end=" ")
#     print()

# greatest number
# list = (30, 50, 21, 16, 100, 80,6)
# a=0
# for i in list:
#     if a<i:
#        a = i
#        print(a)
# print(a)

#  least numbers
# list = (30, 50, 21, 16, 100, 80)
# for j in list:
#     print("j=",j)
#     for i in list:
#         print("i=",i)
#         if j>i:
#             k = i
# print(k)

# Least number
# l = list(map(int, input("Enter array elements:").split(" ")))
# l = (30, 50, 21, 16, 100, 80)
# print(l)
# min1 = l[0]
# for i in l:
#     if i < min1:
#         min1 = i
# print(min1)

a=3*4
print(a)