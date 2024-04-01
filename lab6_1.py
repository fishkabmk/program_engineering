input_str = input("Введите последовательность чисел, разделенныых пробелом: ")
out_list = []
out_list.append(tuple(int(x) for x in input_str.split(' ')))
print(out_list)