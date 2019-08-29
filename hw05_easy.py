# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

def getcurr_dir():
    return os.getcwd()

def show_fold(_path):
    #show folder
    for item in os.listdir(_path):
        print (item)
    return

def cd_dir(_path):
    try:
        os.chdir(_path)
    except:
        return -1
    return 0

def mk_dir(_name):
    try:
        os.mkdir(_name)
    except:
        return -1
    return 0

def rm_dir(_name):
    try:
        os.rmdir(_name)
    except:
        return -1
    return 0

#if __name__ == "__main__":

list_dir = ["dir_"+str(i) for i in range(1,10)]

cpath=os.getcwd()
print("current dir:",cpath)
show_fold(cpath)

print (list_dir)
print("#make")
for dir_ in list_dir:
    os.mkdir(dir_)

show_fold(cpath)

print("#remove")
for dir_ in list_dir:
    os.rmdir(dir_)

show_fold(cpath)

# Задача-2: got used in task#1. skipping
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import sys

fname=sys.argv[0]#get current path+name
print(fname)

base=os.path.basename(fname)#take name+ext
print (base)

foname=os.path.splitext(base)[0]+"_copy"+os.path.splitext(base)[1]#new file name

print(foname)

inp_f=open(fname,'r',encoding='utf8')#read
out_f=open(foname,'w',encoding='utf8')#write

#copy line by line fashion
for str_i in inp_f:
    print(str_i)
    out_f.write(str_i)

inp_f.close()
out_f.close()
#end
