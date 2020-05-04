# En primer lugar registraremos los datos de los diferentes valores del ADN mediante el uso de diccionarios

hair = {"black": "CCAGCAATCGC", "brown": "GCCAGTGCCG", "blonde": "TTAGCTATCGC"}
face = {"square": "GCCACGG", "round": "ACCACAA", "oval": "AGGCCTCA"}
eyes = {"blue": "TTGTGGTGGC", "green" : "GGGAGGTGGC", "brown" : "AAGTAGTGAC"}
gender = {"female": "TGAAGGACCTTC", "male" : "TGCAGGAACTTC"}
race = {"white": "AAAACCTCA", "black" : "CGACTACAG", "asian" : "CGCGGGCCG"}

# Creamos una lista con los datos de cada sospechoso

suspects = {"eva": ["Female", "white", "blonde", "blue", "oval"],
            "larisa": ["female", "white", "brown", "brown", "oval"],
            "matej": ["male", "white", "black", "blue", "oval"],
            "miha": ["male", "white", "brown", "green", "square"]}

# Una vez conocidos todos los datos y agrupados leeremos el archivo dna.txt

with open("dna.txt", "r") as dna_file:
    dna = dna_file.read()

person = []

for x in gender:                      # Analizamos todos los generos
    if gender[x] in dna:
        print(x)
        person.append(x)

for x in race:
    if race[x] in dna:
        print(x)
        person.append(x)

for x in eyes:
    if eyes[x] in dna:
        print(x)
        person.append(x)

for x in hair:
    if hair[x] in dna:
        print(x)
        person.append(x)

for x in face:
    if face[x] in dna:
        print(x)
        person.append(x)

"""
Contrastada la informacion del ADN de la cuchara ya tenemos los datos del sospechoso. Solo faltaría contrastarlo con 
los ADN de todas las personas.

"""
for y in suspects:
    if suspects[p] == person:
