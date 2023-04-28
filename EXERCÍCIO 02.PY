"""EXERCÍCIO 02
 Efetuar a leitura de dois valores numéricos inteiros representados pelas variáveis A e B e apresentar
 o resultado da diferença A-B.

 *Solicitar ao usuário que digite dois valores numéricos inteiros (int) usando variáveis A e B.
 Calcule a diferença entre A e B e armazenar (=) o resultado na variável (dif).
 Exibir o resultado com a função 'print()'.
"""
#ENTRADAS
A = int(input('Digite o valor de A: '))
B = int(input('Digite o valor de B: '))

#PROCESSAMENTO
dif = A - B

#SAÍDA
print (f'A diferença entre A e B é = {dif}')
