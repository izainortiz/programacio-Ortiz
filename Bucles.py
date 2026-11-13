
print("Hola, este es un ejemplo de bucles en Python.")
print("Vamos a ordenar una lista de números ingresados por el usuario.")
print("Por favor, ingrese tres números.")
print("Después de ingresarlos, los ordenaremos de menor a mayor.")
print("¡Comencemos!")
llista = []
print("Ingrese el primer nombre:")
llista.append(input())
print("Ingrese el segundo nombre:")
llista.append(input())
print("Ingrese el tercer nombre:")
llista.append(input())

print("Los nombres ingresados son:", llista)

for i in range(3) :
    llista.append(input("Ingrese otro nombre: "))

print('')
print(llista)
print('')

for i in range(17,101):
    if i%2 == 0:
        print(i, end=' ')
print("\n")

compt = 0
for i in llista[0]:
    if i == 'a':
        compt = +1
        print('la lletra a apareix',compt,'vegades')
    








