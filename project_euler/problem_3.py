def largest_prime_factor(z):
    num_list = []
    for i in range(2, z):
        if z == 1:
            return max(num_list)
        if z%i==0:
            num_list.append(i)
            z = z/i
    return max(num_list)


print(largest_prime_factor(600851475143))