""" EXERCÍCIO 03
O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos
impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os impostos
de 45%, escrever um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor.

Solicitar ao usuário que digite o 'valor do custo de fábrica' do carro e armazenar o valor em uma variável (=). Usar input() pra ler a entrada do usuário e função float() pra converter a entrada em numéros decimais (o que vem depois da vírgula) """

#ENTRADAS
cf = float(input('Digite o valor do custo de fábrica do carro: '))

#PROCESSAMENTO
dis = (cf / 100) * 28
imp = (cf / 100) * 45

#SAÍDA
final = cf + dis + imp

print (f'A porcentagem do distribuidor é de R$: {dis}.')
print (f'a porcentagem dos impostos é de R$: {imp}.')
print (f'O valor do veículo para o consumidor vai ser de R${final}')