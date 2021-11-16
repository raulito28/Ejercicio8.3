import persistencia_json as
import json
lista_coches = json.load(open("Coches.txt", "r"))
json.dump(json.dumps(lista_coches), open("Coches.txt", "w"))
lista_coches = []
print("\nLista coches:\n", lista_coches)
lista_coches = json.loads(json.load(open("Coches.txt", "r")))
print("\nLista coches:\n", lista_coches)


lista_coches = json.load(open("Coches.txt", "r"))
while True:
    coche = {}
    marca = input("Marca de coche: ")
    if marca == "fin":
        break
    coche["Marca Coche"] = marca
    coche["Modelo"] = input("Modelo: ")
    coche["Combustible"] = input("Combustible: ")
    coche["Cilindrada"] = input("Cilindrada: ")
    lista_coches.append(coche)

for coche in lista_coches:
    print("Coche: ", coche)