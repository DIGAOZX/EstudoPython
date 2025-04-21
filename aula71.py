# tuple

x,y,*resto=1,2,3,4,5

print(x,y, resto)

# args

def soma(*args):
    total=0
    for numero in args:
        print("Total ", total, numero)
        total=total+ numero
        print("Total", total)
    print(total)

soma(1,2,3,4,5)

numero1=1
for i in range(5):
    for j in range(1,6):
        if j<5:
          print(j,end=", ")
        else:
            print(j,end=" ")
    print()


