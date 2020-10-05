nome_aluno = input('Digite o nome do aluno: ')
nota1 = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota:'))
media = (nota1 + nota2) / 2

if media >= 7:
    print('Aprovado')
else:
    print('Reprovado')

print('Média do aluno', nome_aluno,':', media)
