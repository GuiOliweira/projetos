total = prod1000 = menor = contador = 0
prodbarato = ''

while True:
    nome_produto = str(input("Digite o nome do produto: "))
    preco_produto = int(input("Agora digite o preco do produto: R$"))
    total += preco_produto
    if preco_produto > 1000:
        prod1000 += 1
    if contador == 1:
        menor = preco_produto
        prodbarato = nome_produto
    else:
        if preco_produto < menor:
            menor = preco_produto
            prodbarato = nome_produto
    pergunta = ' '
    pergunta = input("Voce deseja continuar? S/N ").strip().upper()[0]
    if pergunta == 'N':
        break
print("-" * 40)
print(f"O preco total da sua compra foi de R${total:.2f}.")
print(f"Os produtos que custaram mais de R$1000 foram: {prod1000} produtos.")
print(f"O produto mais barato foi a(o) {prodbarato} que custa R${menor}.")