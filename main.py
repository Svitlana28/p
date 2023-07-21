#1
from itertools import count


def sec(n2)->None:
    print(sum(n2))

n2 = [7,9,8]
print(sec(n2))


#2

def namber(n1) ->None:
   print(min(n1))

n1 = [20,8,9]
print(namber(n1))

#3
def namber3(n1):
  print(n1[::2])



n1 = [3,7,9]
print(namber3(n1))


#4

def next(list,namber):
    count = 0
    for i in list:
       list.remove(i)
    count +=1
    return count



#5
def list(n1,n2):
    print(n1 + n2)


n1 = [4,76]
n2 = [8,8]
print(list(n1,n2))


#6

