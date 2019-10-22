'Laboratorio 7 de JLMC'

armas = ['pistola', 'escopeta']

cargadores = {
    'pistola': [10, 10],
    'escopeta': [2, 2, 2, 2, 2]
}

count = 0

for arma in armas:
    if arma == 'pistola' in cargadores:
        count += 1   
    elif arma == 'escopeta' in cargadores:
        count += 1

for i in armas:
    if i in cargadores:
        s = {sum(value) for key, value in cargadores.items()}
        balas = sum(cargadores['pistola']) + sum(cargadores['escopeta'])
        print(f"Las balas para mi {i} son: {cargadores[i]}")

print(f"\tTengo {count} armas")
print(f"\tTengo {balas} balas en total")
print(f"\n")

#########################################################################
# Ejercicio 1
armas = ['pistola', 'ametralladora', 'escopeta', 'fusil de francotirador']

cargadores = {
    'pistola': [12, 13, 4, 5, 20, 17],
    'ametralladora': [33, 40],
    'escopeta': [2, 2, 2, 1],
    'fusil de francotirador': [1, 2, 4]
}

count = 0

for arma in armas:
    if arma == 'pistola' in cargadores:
        count += 1
    elif arma == 'escopeta' in cargadores:
        count += 1
    elif arma == 'ametralladora' in cargadores:
        count += 1
    elif arma == 'fusil de francotirador' in cargadores:
        count += 1
    

balas = []
for i in armas:
    if i in cargadores:
        s = {sum(value) for key, value in cargadores.items()}
        balas = sum(cargadores['pistola']) + sum(cargadores['ametralladora']) + sum(cargadores['escopeta']) + sum(cargadores['fusil de francotirador'])
        print(f"Las balas para mi {i} son: {cargadores[i]} ")

print(f"\tTengo {count} armas")
print(f"\tTengo {balas} balas en total")
print(f"\n")

##########################################################################
# Ejercicio 2
armas = ['pistola', 'ametralladora', 'escopeta', 'fusil de francotirador']

cargadores = {
    'pistola': [12, 13, 4, 5, 20, 17],
    'ametralladora': [33, 40],
    'escopeta': [2, 2, 2, 1],
    'fusil de francotirador': [1, 2, 4],
    'bazoka': [1, 1]
}

count = 0

for arma in armas:
    if arma == 'pistola' in cargadores:
        count += 1
    elif arma == 'escopeta' in cargadores:
        count += 1
    elif arma == 'ametralladora' in cargadores:
        count += 1
    elif arma == 'fusil de francotirador' in cargadores:
        count += 1
    elif arma == 'bazoka' in cargadores:
        count += 1


balas = []
sobra = []
for i in armas:
    if i in cargadores:
        s = {sum(value) for key, value in cargadores.items()}
        balas = sum(cargadores['pistola']) + sum(cargadores['ametralladora']) + sum(
            cargadores['escopeta']) + sum(cargadores['fusil de francotirador'])
        sobra = sum(cargadores['bazoka'])
        print(f"Las balas para mi {i} son: {cargadores[i]}")

print(f"\tTengo {count} armas")
print(f"\tTengo {balas} balas para mis armas")
print(f"\tTengo {sobra} balas para un arma que me falta")
print(f"\n")

# Ejercicio 3

armas = ['pistola', 'ametralladora', 'escopeta', 'fusil de francotirador']

cargadores = {
    'pistola': [12, 13, 4, 5, 20, 17],
    'ametralladora': [33, 40],
    'escopeta': [2, 2, 2, 1]
}

count = 0
extra = 0

for arma in armas:
    if arma == 'pistola' in cargadores:
        count += 1
        extra += 0
    elif arma == 'escopeta' in cargadores:
        count += 1
        extra += 0
    elif arma == 'ametralladora' in cargadores:
        count += 1
        extra += 0
    else:
        extra += 1
    

balas = []
for i in armas:
    if i in cargadores:
        s = {sum(value) for key, value in cargadores.items()}
        balas = sum(cargadores['pistola']) + sum(cargadores['ametralladora']) + sum(
            cargadores['escopeta'])
        print(f"Las balas para mi {i} son: {cargadores[i]}")

print(f"\tTengo {count} armas")
print(f"\tTengo {balas} balas en total")
print(f"\tTengo {extra} arma(s) extra(s)")

