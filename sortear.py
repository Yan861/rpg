import random
nomes =['mogukann','claudia','mama','tailoar','gasolina','Helena','Jackson']

dupla1 = []
dupla2 = []
trio = []

dupla1.append(random.choice(nomes))

nomes = list(set(nomes) - set(dupla1))

dupla1.append(random.choice(nomes))

nomes = list(set(nomes) - set(dupla1))

dupla2.append(random.choice(nomes))

nomes = list(set(nomes) - set(dupla2))

dupla2.append(random.choice(nomes))

nomes = list(set(nomes) - set(dupla2))

trio.append(random.choice(nomes))

nomes = list(set(nomes) - set(trio))


trio.append(random.choice(nomes))

nomes = list(set(nomes) - set(trio))


trio.append(random.choice(nomes))

nomes = list(set(nomes) - set(trio))

print(dupla1)
print(dupla2)
print(trio)
print(nomes)