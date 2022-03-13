#x = 1
#while x <= 10:
#    print(x)
#    x += 1
#else: 
#    print('Saliendo del bucle while..')

x = 0
while x < 10:
    x += 1
    if x == 5 or x == 7:
        continue
    print(x)
    
# Continue = saltarse las condicionales