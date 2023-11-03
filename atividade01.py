import math

def combinacoes(n, m):
    grupo1 = m
    grupo2 = n - m
    combinacao = math.factorial(n) / (math.factorial(grupo1) * math.factorial(grupo2))
    return combinacao

n = int(input('Quantidade total de alunos: '))
m = int(input('Quantidade do primeiro grupo de alunos: '))

resultado = combinacoes(n, m)
print(f'O número de combinações possíveis é: {resultado}')
