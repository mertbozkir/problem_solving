def largest_palindrome_product():
    import itertools
    pal_list = []
    numbers = list(itertools.product(range(999, 500, -1), range(999, 500, -1)))

    for number in numbers:
        z = str(number[0] * number[1])
        
        ix = len(z) // 2
        
        if z[:ix] == z[:-ix-1:-1]:
            pal_list.append(int(z))

    return max(pal_list)


print(largest_palindrome_product())