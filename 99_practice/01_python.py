def positive_sum(numbers):
    tmp = 0
    for number in numbers:
        if number > 0:
            tmp += number
    return tmp

print(positive_sum([1, -4, 7, 12]))
print(positive_sum([-1, -2, -3, -4]))