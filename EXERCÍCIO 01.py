"""
Exercício 01 - 
A velocidade média de um veículo é dado pela expressão Vm= ∆S/∆t, onde: 
∆S: variação de espaço (ponto de chegada – ponto de partida) em quilômetros
∆t: variação de tempo (tempo final – tempo inicial) em horas
Escreva um programa para calcular a velocidade média dada a variação espacial e a variação temporal.

* A ideia é calcular a velocidade média de um veículo baseado na variação de espaço e tempo fornecidos pelo usuário.
*solicitar ao usuário que informe a variação de espaço e tempo, função "input".
As entradas as variáveis "dS" e "dt".
A velocidade média é calculada dividindo a variação de espaço pela variação de tempo, O resultado é a variável "vm", usando a função "print".
pra exibir duas casas decimais após a vírgula usar expressão "{:.2f}"."""

#entradas
dS = float(input('Variação de espaço (ponto de chegada - ponto de partida) em km:  '))
dt = float(input('Variação de tempo (tempo inicial - tempo final) em horas: '))

#processamento
vm = dS / dt

#saída
print (f'A velocidade média do veículo é de {vm:.2f} Km/h')