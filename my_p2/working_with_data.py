    # Работа со строками
string1 = "This is a string."
string2 = " This is another string."
print(string1+string2)
print(string1)
print(len(string1))         # определяет длину строки
print(string1.title())      # преобразует первый символ каждого слова в строке к верхнему регистру
print(string1.lower())      # символы строки преобразуются к нижнему регистру
print(string2.upper())      # символы строки преобразуются к верхнему регистру
print(string1.rstrip())     # удаляются пробелы в конце строки
print(string2.lstrip())     # удаляются пробелы в начале строки
print(string1.strip())      # удаляются пробелы с обоих концов
print(string1.strip("0"))   # удаляются с обоих концов указанные символы в параметре функции

    # Извлечение символов и подстрок
d = "qwerty"
ch = d[2]       # извлекается символ ‘e’
print(ch, d[1:3], d[1:], d[:3], d[:], d[1:5:2])
#d[2] = 'o'

    # Работа с числами
intNum1 = 50
intNum2 = 3
print(intNum1//intNum2, intNum1%intNum2, intNum1**intNum2)

param = "string" + str(15)
print(param)

    # Преобразование данных
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " = ", n3)

    # Форматирование строк
a = 1/3
print("{:7.3f}".format(a))

a = 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))

n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " = ", "{:7.3f}".format(n3))

    # Списки
list1 = [82, 8, 23, 97, 92, 44, 17, 39, 11, 12]
print(dir(list))

help(list.insert)
help(list.append)
help(list.sort)
help(list.remove)
help(list.reverse)

print(list1)
list1[3] = 24
list1[0] = 13
list1[8] = 15
print(list1)
list1.insert(10, 13)
print(list1)
list1.remove(8)
print(list1)
list1.append(22)
print(list1)
item = list1.pop()
print(list1, item)
del list1[4]
print(list1)

    # Cортировка элементов списка
list1.sort(reverse=True)
print(list1)
list = sorted(list1)
print(list)

list2 = [3, 5, 6, 2, 33, 6, 11]
print(list2)
lis = sorted(list2)
print(lis)

    # Кортежи
print((dir(tuple)))

help(tuple.index)
help(tuple.count)

seq = (2, 8, 23, 97, 92, 44, 17, 39, 11, 12)
print(seq.count(8))
print(seq.index(44))
listseq= list  # преобразование в список
print(listseq)
print(type(listseq))

    #Словари
D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}
print(D)
print(D['food'])
D['quantity'] += 10
print(D['quantity'] + 10)

dp = {}
key = input("Введите название ключа: ")
value = input("Введите значение: ")
dp[key] = value
print(dp)

    #Вложеность хранения данных
rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'},
        'job': ['dev', 'mgr'],
        'age': 25}
print(rec["name"]["firstname"], rec["name"]["lastname"])
print(rec["name"]["firstname"])
print(rec["job"])

rec['job'].append('janitor')
print(rec)