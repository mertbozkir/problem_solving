def even_fibonacci_numbers(num):
    num_list = [1, 2]
    
    sum = 0

    first_num = num_list[0]
    sec_num = num_list[1]
    
    for i in range(num -2):
        
        temp_num = sec_num
        
        if sec_num > 4000000:
            return sum
        if sec_num %2 == 0:
            sum += sec_num
        num_list.append(first_num + sec_num)
        first_num = temp_num
        sec_num = num_list[-1]

    return sum

print(even_fibonacci_numbers(1000000))