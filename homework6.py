# Словарь: логин : пароль
my_dict = {"Kongost" : 'Mozgodryg', "Zayac" : 'volk0921', "Pudzh" : 57894125}
print(my_dict)
my_dict["Zakat"] = "Tazik"
print(my_dict)
del my_dict["Kongost"]
print(my_dict)
my_dict.update({"mongust" : 78454318,
                "Ludoed" : "Kasha192812"})
print(my_dict)
print(my_dict.get("Pudzh"))
print(my_dict.get("zayka"))
a = my_dict.pop("Ludoed")
print(a)
print(my_dict)
print (" ")
# МНОЖЕСТВА
my_set = {1, 2, 7, 3, "Ramka", True, "Pullpy", (2, 4, 1), 1, "Pullpy", True, False}
print(my_set)
my_set.add((3, 2, 1))
print(my_set)
my_set.update({"Tvorez", "Ramka", "Zaraza"})
print(my_set)
my_set.remove((2, 4, 1))
print(my_set)


