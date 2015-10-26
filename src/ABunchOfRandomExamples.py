'''
Created on Jul 22, 2015

@author: jiahuan
'''

print ("Hello World!")

print (1 + 2*3)

a = 10
while a < 20 :
    a = a + 2
    print a
    

#define my own Function
def hello():
    print("\nHello from function hello()")
    return 12345

print hello()


a = [-1, 0, 2, 4, 6, 8, 10]
print ("\nbefore deletion, a is: ")
print(a)
del a[1]
print("after deletion, a is:")
print a


def greet(name):
    print("\nHello " + name + "!")
    
greet("Steve")
greet("Sophie")