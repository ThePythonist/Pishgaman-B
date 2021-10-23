numbers = [11,22,11,33,11,44,22]
# unique_numbers = []
#
# for number in numbers :
#     if number not in unique_numbers :
#         unique_numbers.append(number)
#
# print(unique_numbers)
#
unique_numbers = list(set(numbers))
print(unique_numbers)
