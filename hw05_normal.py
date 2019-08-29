# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import hw05_easy as lib_kon
str='''
======MENU=======
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Создать папку
# 4. Удалить папку
# 5. Exit
    '''
c_path=lib_kon.getcurr_dir()

while True:
    print(str)
    print (c_path,">",end=" ")
    choice = input()
    if choice == "1":
        #cd
        print("provide path:",end=" ")
        _path=input()
        if lib_kon.cd_dir(_path):
            print("unsuccessful")
        else:
            print("successfull..")
            c_path=_path

    elif choice == "2":
        #dir
        lib_kon.show_fold(c_path)
    elif choice == "3":
        #mkdir
        print("provide dir name:",end=" ")
        d_name=input()
        if lib_kon.mk_dir(c_path+"\\"+d_name):
            print("unsuccessful")
        else:
            print("successfull..")
    elif choice == "4":
        #rmdir
        print("provide dir name:",end=" ")
        d_name=input()
        if lib_kon.rm_dir(c_path+"\\"+d_name):
            print("unsuccessful")
        else:
            print("successfull..")
    elif choice == "5":
        print("exiting!")
        break


