"""
Las listas:
-Son colecciones de datos
-Se construyen con 'items' separados por comas dentro de corchetes cuadrados []
-Son valores ordenados
-Son modificables
-Cualquier nuevo valor se pone siempre al final de la lista
-Admite valores repetidos
-Los items de las listas estan indexados, estando el primer ítem en la direccion [0], el segundo en [1], .....
-El indexado funciona con números negativos, siendo [-1] el último valor, [-2] penúltimo, [-3] antepenúltimo...
-Los items pueden ser de cualquier tipo de dato
"""



thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print("""
Si ponemos el índice [1] nos entrega el SEGUNDO 'item' de la lista que es:""", thislist[1])
print("""
Si ponemos el índice [-1] nos entrega el ÚLTIMO 'item' de la lista que es:""", thislist[-1])
txt=f'El tamaño de la LISTA es: {len(thislist)}'   #Usamos una variable F-String con un 'PLACEHOLDER'
print(txt)

print("""
Otra manera de hacerlo sin tanto pedo es:""")
print("El tamaño de la LISTA llamada 'thislist' es:", len(thislist))


print("""
Los items pueden ser de cualquier tipo de dato""")
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print("str ->", list1)
print("int ->", list2)
print("bool ->", list3)

print("""
Y lo mejor es que los puedes revolver, y Python no dice ni pío""")
list4 = ["abc", 34, True, 3.14159, "male"]
print("Lista toda chilaquilosa ->", list4)
