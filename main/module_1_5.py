immutable_var = 1, 2.5, "Moon", False 
print(immutable_var)
# immutable_var [1] = 3   кортеж не поддерживает обращение по элементу
# print(immutable_var)  мы не можем добавить какой-то отдельно взятый элемент или изменить какой-то элемент внутри кортежа
mutable_list = [1, 2.5, "Moon"]
mutable_list [2] = "Sun"
print(mutable_list)
