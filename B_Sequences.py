# points, tokens = [[3, 4, 5, 2, 3], "TEETT"]
# points, tokens = [[1,1,1,1], 'TTTT']


# def find(points, tokens):
#   n = len(points)
#   answer = 0
#   if n == 0:
#     return 0
#   if tokens[0] == 'T':
#     answer += points[0]
#   for i in range(1, n):

#     if tokens[i] == 'T':
#       answer += points[i]

#       if tokens[i - 1] == 'T':
#         answer += 1

#   return answer


# print(find(points, tokens))


# def find(S):
#     answer = 0
#     current = 0

#     for first in range(9 + 1):
#         current += first
#         if current > S:
#             current -= first
#             break

#         for second in range(9 + 1):
#             current += second
#             if current > S:
#                 current -= second
#                 break

#             for third in range(9 + 1):
#                 current += third
#                 if current > S:
#                     current -= third
#                     break

#                 for fourth in range(9 + 1):
#                     current += fourth
#                     if current > S:
#                         current -= fourth
#                         break

#                     if current == S:
#                         answer += 1

#                     current -= fourth

#                 current -= third
#             current -= second
#         current -= first

#     return answer


# # s = int(input())
# # print(find(s))


# # def find(S):
# #     answer = 0
# #     current = 0

# #     for first in range(9 + 1):
# #         current += first
# #         print('current', current)
# #         if current > S:
# #             print('current ', current, 's', S)
# #             break
# #         print(first)
# #         for second in range(9 + 1):
# #             current += second
# #             print('current', current)
# #             if current > S:
# #                 print('current ', current, 's', S)
# #                 break

# #             print(first, second)
# #             for third in range(9 + 1):
# #                 current += third
# #                 print('current', current)
# #                 if current > S:
# #                     print('current ', current, 's', S)
# #                     break

# #                 print(first, second, third)
# #                 for fourth in range(9 + 1):
# #                     current += fourth
# #                     print('current', current)
# #                     if current > S:
# #                         print('current ', current, 's', S)
# #                         break

# #                     print(first, second, third, fourth)
# #                     if current == S:
# #                         answer += 1

# #                     current -= fourth

# #                 current -= third
# #             current -= second
# #         current -= first

# #     return answer


# # s = int(input())
# # print(find(s))
