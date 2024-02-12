import random
nomes =[]
iniciativa=[]
print("quantos personagens são?")
qtdeDeInimigos = input()


print("nome dos personagens que estão na luta:")
for i in range(int(qtdeDeInimigos)):
    nomes.append(input())


for j in range(len(nomes)):
    print("iniciativa de "+nomes[j]+":")    
    iniciativa.append(input())

maping= dict(zip(iniciativa,nomes))

maping = dict(sorted(maping.items()))
print(maping)

