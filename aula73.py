""" *args empacotados e desempacotados 
    e se é par ou impar
"""

def mutiplication(*args):
    total=1
    for numbers in args:
        total *=numbers
        if numbers %2==0:
            print( numbers, "é par")
        else:
            print( numbers, "é impar ")
    return total
        
result=(mutiplication(1,2,3,4,5))
print("o resultado final é: ", result )