# int(input) = tu poner los datos que quieras dentro de la consola
edad = int(input('¿Cúal es tu edad?'))

if edad <= 0:
    print ("Nadie puede tener esa edad, bro")
    
# elif = segunda condición 
# and = solo significa y para dos condiciones o más   
    
elif edad >= 1 and edad <= 17:
    print('Eres menor de edad.')
    
elif edad <= 100:
    print('Eres mayor de edad.')
    
else:
    print ('Edad no válida. orale, shu.')
    