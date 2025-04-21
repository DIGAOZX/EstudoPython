def func():
    x=1
    def fun1():
        z=3
        z=4
        print(x,z)
    fun1()
    print(x)

func()

def soma(x,y):
    return x+y

print(soma(4,5))