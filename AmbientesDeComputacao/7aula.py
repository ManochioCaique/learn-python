'''
Título: 7ª aula
Função: Anotações da aula
Autor: Caique Manóchio
Data: 03/04/2024

'''
#Listas são conjuntos de dados, podendo ser numerica ou de string. posso qualquer coisa  dentro da lista, até mesmo outra lista
#para chamar uma lista dentro de outra lista[0][0
#Declaranod uma lista entre cholchetes []
nucleotideos = ["A", "T", "C", "G"]
print(nucleotideos)
#acessar um item
print(nucleotideos[0])

print(nucleotideos[1:2])

print(nucleotideos[:2])

print(nucleotideos[1:])

print(nucleotideos[-4:-1])
#imprimi todas os elementos da lista
print(nucleotideos[:])
#Exirbir todos os elementos de dois em dois
print(nucleotideos[::2])
#Invertento os elementos da minha lista 
print(nucleotideos[::-1])

#loop para percorrer uma lsta por posição
total_itens = len(nucleotideos)
for i in range(total_itens):
    print(nucleotideos[i])

#Para saber maior e menor

print(max(nucleotideos))
print(min(nucleotideos))

#Pertencimento a lista
if "T" in nucleotideos:
    print("DNA")
elif "U" in nucleotideos:
    print("RNA")

#Adicionar elementos com append
nucleotideos.append("U")
#Adicionar em uma posição especifica
nucleotideos.insert(0, "U")
#Deleta o valor selecionado 
del nucleotideos[0]
#Deleta o valor delimidado e para
nucleotideos.remove("U")
#Concatenar lstas
nucleotideos2 = ["A", "C", "A"]
mais_nucleotidios = nucleotideos + nucleotideos2
print(mais_nucleotidios)

#Tuplas é um conjunto de lista imputavel 
tupla = (1, 2, 3)

#Dicionarios são formados por um conjunto de valores e chave
dicionario = {"A" : "adenina",
              "T" : "timina", 
              "C" : "citosina",
              "G" : "guanina"}

