## задача 1
a = 18
b = 'длинна мого хера'
masterDEN_says = [a, b, [b, a]]
print(masterDEN_says)
print(type(masterDEN_says))
print(type(a))
print(type(b))

## задача 2
list_MasterDen2 = [2, 12, 3, 13, 4, 14, 5, 15, 1.2, 106, ]
list_MasterDen2.sort()
print(list_MasterDen2)
# обратная сотрировка
list_MasterDen2.sort(reverse=True)
print(list_MasterDen2)
list_MasterDen2.append('text')
print(list_MasterDen2)
# попробуем создать еще 1 список и обьединить их
list_MasterDen3 = [333, 667, 1, 1.08]
print(list_MasterDen3)
final_list = list_MasterDen2 + list_MasterDen3
print(final_list)
final_list.remove('text')
print(final_list)
final_list.sort()
print(final_list)