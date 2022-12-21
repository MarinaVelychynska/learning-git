my_list = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
print(my_list[:4])

first_list = [i for i in range(101)] 

second_list = [i for i in first_list if i % 5==0]
print(second_list)

third_list = [i **3 for i in first_list]
print(third_list)
