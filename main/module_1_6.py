#1
my_dict = {"David" : 1999}
print(my_dict)
print(my_dict.get("David"))
my_dict.update({"Max": 2000,
                "Ron": 1998})
print(my_dict)
del my_dict ["Ron"]
my_dict.get("Ron")
print(my_dict)


#2  не уверен что правильно сделал)
my_set = {300, "Sun", 3.14}
print(my_set)
my_set.add(11)
my_set.add(121)
my_set.remove(300)
print(my_set)
