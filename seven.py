input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum(filter(lambda x: x%5==0 or x%3==0, input_list))