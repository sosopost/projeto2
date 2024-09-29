# entrada
ano = int(input("Digite o ano de nascimento: "))
# processamento
idade = 2023 - ano
print("A idade é", idade)
# carteira de motorista
if idade >= 18:
    print("Portanto, pode tirar a carteira de motorista")
else:
    print("Portanto, não pode tirar a carteira de motorista")
