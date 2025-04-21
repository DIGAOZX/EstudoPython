
x = 1
def escopo():
    global x
    x=10
    def funcao():
        z=3
        x=2
        print(x,z)
    funcao()
    print(x)

print(x)
escopo()
