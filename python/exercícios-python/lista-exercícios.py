""" Exercício 1 — Somando números maiores que 10
lista = [5, 12, 8, 20, 3, 15]
soma = 0

for i in lista:
    if i > 10:
        soma = soma + i
    
print(soma) """

""" Exercício 2 — Encontrar menor número

lista = [15, 3, 9, 1, 20]
menor = lista[0]

for i in lista:
    if i < menor:
        menor = i
print("o menor numero é ", menor) """


""" Exercício 3 — Aumento de salário
 
funcionario = {
    "nome": "Carlos",
    "salario": 2000
}

preco_novo = funcionario["salario"] * 1.10
print(preco_novo) """

""" Exercício 4 — Mostrar aprovados
 alunos = [
    {"nome": "Ana", "nota": 8},
    {"nome": "João", "nota": 5},
    {"nome": "Pedro", "nota": 7},
    {"nome": "Maria", "nota": 4}
]

for i in alunos:
    if i["nota"] >= 7:
        print(i) """


""" Exercício 5 — Média de vendas
lista = [100, 200, 300, 400, 500]
soma = 0
media = len(lista)
for i in lista:
    soma += i

media = soma / media

print(media) """