import random
class Iter_BottleBag:
    def __init__(self, start, rand1, rand2, amount):
        self.i = start
        self.rand1=rand1
        self.rand2=rand2
        self.amount=amount
        self.bag=[]
        random.seed


    def isnt_in(self,num):
        for i in self.bag:
            if i==num:
                return 0
        return 1

    def __next__(self):
        self.i += 1
        while True:
            k = random.randint(self.rand1,self.rand2)
            if self.isnt_in(k):
                self.k=k
                self.bag.append(k)
                break
        if self.i < self.amount+1:
            return self.k
        else:
            raise StopIteration

    def __iter__(self):
        return Iter_BottleBag(self.i,self.rand1,self.rand2,self.amount)


#gen carta
#obj1 = Iter_BottleBag(0,0,89,15)

class Card:
    def __init__(self):
        self.card1=[]
        self.obj1 = Iter_BottleBag(0,0,89,15)
        self.obj2 = Iter_BottleBag(0,0,8,4)
        for val in self.obj1:
            self.card1.append(val)

    def render(self):
        print ("================card1===============")
        self.line1=[]
#        print(list(self.obj2))
        for i in range (0,3):
            self.line1.clear()
            for j in range (0,5):
             self.line1.append(self.card1[i*5+j])

            for k in self.obj2:
                self.line1.insert(k,"#")

            #self.line1.sort()
            for i in self.line1:
                if i==255:
                    print("-",end=" ")
                    continue
                print (i,end=" ")
            print('\n')
        print ("================card1===============")

    def is_in(self,num):
        if num in self.card1:
            return True
        return False

    def mark(self,num):
        for i in range(0,len(self.card1)):
            if self.card1[i]==num:
                self.card1[i] = 255

#obj2 = Iter_BottleBag(0,0,89,15)

obj = Iter_BottleBag(0,0,89,90)
plcard = Card()

for el in obj:
    print("print number is",el)
    plcard.render()
    print("wanna mark y/n")
    if input()=="y":
        print ("whats number?")
        num = int(input())
        if plcard.is_in(num):
            plcard.mark(num)
        else:
            print("number you entered is not in card. bye")
            break;

