def multiples_of_3_or_5(z):
    sum = 0
    number_list= range(1, z)
    for i in number_list:
        if (i%3 == 0 or i%5 == 0):
            sum += i
    return sum

print(multiples_of_3_or_5(1000))