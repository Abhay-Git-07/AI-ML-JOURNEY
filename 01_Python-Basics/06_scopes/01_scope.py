username = "Ash"

def scope():
    username = "pikachu"   # Jbtk fn mai vairable present hai wo uski value whi se lega global se nhi
    print(username)

print(username)
scope()                  #Agr fn ke andr username ko comment krdo to fn value global se lega


x = 99
#def func(y):
  #  z = x + y
 #   return z
#result = func(1)
#print(result)  # Yha fn x ki value global se utha lega



#def func_2():
  #  global x
  #  x = 12
    
#func_2()    
#print(x)


def f1():
    x = 88
    def f2():  # Ye fn f1 wale x ko global manega agr wha nhi mila tb ye bhar jayega
        print(x)    
    return f2
Myresult = f1() 
Myresult()   


def chaicoder(num):
    def actual(x):
        return x**num
    return actual

K = chaicoder(2)
L = chaicoder(3)
print(K(3))
print(L(3))