#lesson3 normal task 1

wage=[44185, 9936, 50492, 29990, 113643, 41842, 65242, 57838, 62388, 74948, 9041, 73975, 50542, 37934, 58413, 47168, 54572, 52221, 44624, 44358]
names=["Brook", "Houser", "Kayce", "Mooneyhan", "Cherie", "Zerbe", "Irene", "Wiechmann", "Reuben",
       "Height", "Pauline", "Babcock", "Nikita", "Cobbley", "Valentine", "Beagle", "Sondra", "Mccroy","Wilfred", "Gizzi"]
n=20

wages={}
j=0
for i in names:
    wages[i]=wage[j]
    j += 1

print(wages)

fname="wages.txt"

f = open(fname,'w+')

for i in range(n):
    x = wages.popitem()
    f.write(" %d %s - %d\n" % (i+1, x[0], x[1]))
f.close()


f = open(fname,'r')

f1 = f.readlines()
for i in f1:
    l = i.split(sep=" ")
    wage_i = int(l[4])-int(l[4])*0.13
    if int(l[4]) < 50000:
        print(l[2].upper(),"-", wage_i, "(-13%)")
    else:
        print(l[2].upper(),"-", "***HIDDEN*** (-13%)")

f.close()



#print(names)
