""" Exercício 1 — Somar números

Faça uma lista:

[10, 20, 30, 40]

Use for para:

somar todos os números
mostrar o resultado final """

""" numero = [10,20,30,40]
soma = 0

for i in numero:
    soma += i

print(soma)

 """


""" Exercício 2 — Mostrar apenas pares

Lista:

[1, 2, 3, 4, 5, 6, 7, 8]

Mostre apenas os números pares. """

""" lista = [1,2,3,4,5,6,7,8]
par = []
impar = []

for i in lista:
    if i % 2== 0:
        par.append(i)
    else:
        impar.append(i)

print(par)
print(impar)
 """

""" Exercício 3 — Maior número

Lista:

[5, 99, 12, 45, 1]

Descubra o maior número sem usar max(). """

""" numero = [5,99,12,45,1]
maior = numero[0]

for i in numero:
    if i > maior:
        maior = i

print(maior)
 """

""" Exercício 4 — Trabalhando com dicionário

Crie:

pessoa = {
    "nome": "Carlos",
    "idade": 20,
    "cidade": "Porto Alegre"
}

Mostre:

nome
idade """

""" pessoa = {
    "nome": "Carlos",
    "idade": 20,
    "cidade": "Porto Alegre"
}

nome = pessoa["nome"]
idade = pessoa["idade"]

print(nome)
print("tem", idade, "anos de idade") """


""" Exercício 5 — Lista de dicionários

Crie:

alunos = [
    {"nome": "Ana", "nota": 8},
    {"nome": "Pedro", "nota": 5},
    {"nome": "Maria", "nota": 9}
]

Use for para mostrar:

nome dos alunos
nota de cada um """

""" alunos = [
    {"nome": "Ana", "nota": 8},
    {"nome": "Pedro", "nota": 5},
    {"nome": "Maria", "nota": 9}
]

for i in alunos:
    print(i["nome"])
    print(i["nota"])
 """