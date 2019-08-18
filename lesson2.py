# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
import random
#rand gen init
random.seed()

#gen list
len = 16
inp_lst = []
for i in range(0,len):
    inp_lst.append(random.randint(-10,100))

print ("input list = ",inp_lst)

out_lst=[]
for i in inp_lst:
    if i>0:
        k = i**0.5
        if not(k % 1):
            out_lst.append(int(k))

print ("output list only (integer sqr root numbers) =",out_lst)


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
date ="01.01.2013"
data =date.split('.')
dic_dat = {}
dic_dat_day = {'первое': 1, 'второе': 2,'третье': 3}
dic_dat_mon = {'ноября': 11, 'декабря': 12, 'января': 1}

str_date=""
for i in dic_dat_day:
    if (int(data[0])== dic_dat_day.get(i)):
        str_date = i

for i in dic_dat_mon:
    if (int(data[1])== dic_dat_mon.get(i)):
        str_date += " " + i

str_date +=  " " + data[2] + " года"

print("дата",date)
print("дата прописью: = ",str_date)


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

#rand gen init
random.seed()

#gen list
len = 10
inp_lst = []
for i in range(0,len):
    inp_lst.append(random.randint(-10,10))

print ("random list = ",inp_lst)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

d={}
for i in inp_lst:
    d[i]=d.get(i,0)+1 #get from dict key val if nothing set the val to zero
        #if i in d:
         #   d[i] +=1
        #else:
         #   d[i]=1

print("number amount")
for i in sorted(d):
    print (i,d[i])

print("lst1 a)")
for i in sorted(d):
    print (i,end= " ")

print("\nlst2 b)")
for i in sorted(d):
    if d.get(i) == 1:
        print (i,end= " ")

#ready
