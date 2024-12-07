def print_params(a=1, b='строка', c=True):
    print(a, b, c)



print_params()
print_params(3, 2)
print_params(b = 25)
print_params(c = [1,2,3])
values_list = ["text", 4, True]
values_dict = {"a":3.1, "b":"slovo", "c":9}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [25, "slovo2"]
print_params(*values_list_2, 42)