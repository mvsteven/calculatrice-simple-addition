premier_nombre = input("Entrer un premier nombre: ")
second_nombre = input("Entrer un second nombre: ")

if premier_nombre.isdigit() and second_nombre.isdigit() == True:
    premier_nombre = int(premier_nombre)
    second_nombre = int(second_nombre)
    print(
        f"La somme de {premier_nombre} et {second_nombre} vaut: {premier_nombre + second_nombre}")
else:
    print("Veuillez entrer des nombre s'il vous plait!")
